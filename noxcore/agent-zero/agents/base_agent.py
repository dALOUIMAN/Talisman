"""
Base Agent - Core AI Agent implementation
Lightweight, efficient, and designed for hive coordination
"""

import os
import asyncio
import logging
from typing import Dict, Any, Optional
import redis.asyncio as redis
import json
from datetime import datetime


class BaseAgent:
    """Base Agent implementation for NoxCore Agent Zero system"""
    
    def __init__(self, agent_id: str, agent_type: str = 'worker'):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.logger = logging.getLogger(f'Agent-{agent_id}')
        
        # Redis connection for hive communication
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = int(os.getenv('REDIS_PORT', 6379))
        
        self.redis_client: Optional[redis.Redis] = None
        self.redis_host = redis_host
        self.redis_port = redis_port
        
        # Agent state
        self.running = False
        self.current_task: Optional[Dict[str, Any]] = None
        
        self.logger.info(f"Agent initialized: {agent_id} ({agent_type})")
    
    async def connect_redis(self):
        """Connect to Redis for hive communication"""
        try:
            self.redis_client = await redis.from_url(
                f"redis://{self.redis_host}:{self.redis_port}",
                decode_responses=True
            )
            await self.redis_client.ping()
            self.logger.info("Connected to Redis hive")
        except Exception as e:
            self.logger.error(f"Failed to connect to Redis: {e}")
            raise
    
    async def register_with_hive(self):
        """Register agent with the hive coordinator"""
        if not self.redis_client:
            return
        
        agent_info = {
            'id': self.agent_id,
            'type': self.agent_type,
            'status': 'active',
            'timestamp': datetime.utcnow().isoformat()
        }
        
        await self.redis_client.setex(
            f"agent:{self.agent_id}",
            300,  # 5 minutes TTL
            json.dumps(agent_info)
        )
        
        self.logger.info(f"Registered with hive as {self.agent_id}")
    
    async def heartbeat(self):
        """Send periodic heartbeat to maintain hive registration"""
        while self.running:
            try:
                await self.register_with_hive()
                await asyncio.sleep(60)  # Heartbeat every minute
            except Exception as e:
                self.logger.error(f"Heartbeat failed: {e}")
                await asyncio.sleep(5)
    
    async def listen_for_tasks(self):
        """Listen for tasks from the coordinator"""
        if not self.redis_client:
            return
        
        pubsub = self.redis_client.pubsub()
        await pubsub.subscribe(f"agent:{self.agent_id}:tasks", "broadcast:tasks")
        
        self.logger.info("Listening for tasks...")
        
        async for message in pubsub.listen():
            if message['type'] != 'message':
                continue
            
            try:
                task_data = json.loads(message['data'])
                self.logger.info(f"Received task: {task_data.get('task_id', 'unknown')}")
                await self.execute_task(task_data)
            except Exception as e:
                self.logger.error(f"Task processing error: {e}")
    
    async def execute_task(self, task: Dict[str, Any]):
        """Execute a task received from coordinator"""
        task_id = task.get('task_id', 'unknown')
        task_type = task.get('type', 'unknown')
        
        self.logger.info(f"Executing task {task_id} of type {task_type}")
        
        self.current_task = task
        
        try:
            # Simulate task execution
            # In a real implementation, this would route to specific handlers
            await asyncio.sleep(1)
            
            # Report completion
            result = {
                'task_id': task_id,
                'agent_id': self.agent_id,
                'status': 'completed',
                'timestamp': datetime.utcnow().isoformat()
            }
            
            if self.redis_client:
                await self.redis_client.publish(
                    'coordinator:results',
                    json.dumps(result)
                )
            
            self.logger.info(f"Task {task_id} completed")
            
        except Exception as e:
            self.logger.error(f"Task execution failed: {e}")
            
            # Report failure
            if self.redis_client:
                result = {
                    'task_id': task_id,
                    'agent_id': self.agent_id,
                    'status': 'failed',
                    'error': str(e),
                    'timestamp': datetime.utcnow().isoformat()
                }
                await self.redis_client.publish(
                    'coordinator:results',
                    json.dumps(result)
                )
        finally:
            self.current_task = None
    
    async def start(self):
        """Start the agent"""
        self.running = True
        self.logger.info(f"Starting agent {self.agent_id}")
        
        await self.connect_redis()
        await self.register_with_hive()
        
        # Start background tasks
        tasks = [
            asyncio.create_task(self.heartbeat()),
            asyncio.create_task(self.listen_for_tasks())
        ]
        
        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            self.logger.info("Agent tasks cancelled")
        finally:
            self.running = False
            if self.redis_client:
                await self.redis_client.close()
    
    async def stop(self):
        """Stop the agent"""
        self.logger.info(f"Stopping agent {self.agent_id}")
        self.running = False
