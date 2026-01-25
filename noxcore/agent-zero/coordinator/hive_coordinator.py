"""
Hive Coordinator - Central coordination system for distributed agents
Manages task distribution, agent health, and hive intelligence
"""

import os
import asyncio
import logging
from typing import Dict, List, Any, Optional
import redis.asyncio as redis
import json
from datetime import datetime
from collections import defaultdict


class HiveCoordinator:
    """Hive Coordinator for managing distributed Agent Zero instances"""
    
    def __init__(self, coordinator_id: str = 'coordinator-1'):
        self.coordinator_id = coordinator_id
        self.logger = logging.getLogger('HiveCoordinator')
        
        # Redis connection
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = int(os.getenv('REDIS_PORT', 6379))
        
        self.redis_client: Optional[redis.Redis] = None
        self.redis_host = redis_host
        self.redis_port = redis_port
        
        # Hive state
        self.running = False
        self.agents: Dict[str, Dict[str, Any]] = {}
        self.task_queue: List[Dict[str, Any]] = []
        self.active_tasks: Dict[str, Dict[str, Any]] = {}
        self.max_agents = int(os.getenv('MAX_AGENTS', 10))
        
        # Statistics
        self.stats = defaultdict(int)
        
        self.logger.info(f"Hive Coordinator initialized: {coordinator_id}")
    
    async def connect_redis(self):
        """Connect to Redis"""
        try:
            self.redis_client = await redis.from_url(
                f"redis://{self.redis_host}:{self.redis_port}",
                decode_responses=True
            )
            await self.redis_client.ping()
            self.logger.info("Coordinator connected to Redis")
        except Exception as e:
            self.logger.error(f"Failed to connect to Redis: {e}")
            raise
    
    async def discover_agents(self):
        """Discover active agents in the hive"""
        if not self.redis_client:
            return
        
        try:
            # Scan for agent keys
            keys = []
            async for key in self.redis_client.scan_iter(match="agent:*", count=100):
                if not key.endswith(':tasks'):
                    keys.append(key)
            
            # Get agent info
            new_agents = {}
            for key in keys:
                agent_data = await self.redis_client.get(key)
                if agent_data:
                    agent_info = json.loads(agent_data)
                    agent_id = agent_info.get('id')
                    if agent_id:
                        new_agents[agent_id] = agent_info
            
            # Update agent registry
            self.agents = new_agents
            self.logger.debug(f"Discovered {len(self.agents)} active agents")
            
        except Exception as e:
            self.logger.error(f"Agent discovery failed: {e}")
    
    async def monitor_agents(self):
        """Monitor agent health and status"""
        while self.running:
            try:
                await self.discover_agents()
                
                # Log hive status
                active_count = len(self.agents)
                self.logger.info(
                    f"Hive Status - Active Agents: {active_count}, "
                    f"Queue: {len(self.task_queue)}, "
                    f"Active Tasks: {len(self.active_tasks)}"
                )
                
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                self.logger.error(f"Agent monitoring error: {e}")
                await asyncio.sleep(5)
    
    async def listen_for_results(self):
        """Listen for task results from agents"""
        if not self.redis_client:
            return
        
        pubsub = self.redis_client.pubsub()
        await pubsub.subscribe('coordinator:results')
        
        self.logger.info("Listening for task results...")
        
        async for message in pubsub.listen():
            if message['type'] != 'message':
                continue
            
            try:
                result = json.loads(message['data'])
                task_id = result.get('task_id')
                status = result.get('status')
                agent_id = result.get('agent_id')
                
                self.logger.info(
                    f"Task {task_id} {status} by {agent_id}"
                )
                
                # Update statistics
                self.stats[f'tasks_{status}'] += 1
                
                # Remove from active tasks
                if task_id in self.active_tasks:
                    del self.active_tasks[task_id]
                
            except Exception as e:
                self.logger.error(f"Result processing error: {e}")
    
    async def distribute_tasks(self):
        """Distribute tasks to available agents"""
        while self.running:
            try:
                # Check if we have tasks and agents
                if not self.task_queue or not self.agents:
                    await asyncio.sleep(1)
                    continue
                
                # Get available agents (not at capacity)
                available_agents = [
                    agent_id for agent_id in self.agents.keys()
                    if agent_id != self.coordinator_id
                ]
                
                if not available_agents:
                    await asyncio.sleep(1)
                    continue
                
                # Distribute tasks round-robin
                while self.task_queue and available_agents:
                    task = self.task_queue.pop(0)
                    agent_id = available_agents.pop(0)
                    
                    # Send task to agent
                    if self.redis_client:
                        await self.redis_client.publish(
                            f"agent:{agent_id}:tasks",
                            json.dumps(task)
                        )
                        
                        self.active_tasks[task['task_id']] = {
                            'task': task,
                            'agent_id': agent_id,
                            'started': datetime.utcnow().isoformat()
                        }
                        
                        self.logger.info(
                            f"Distributed task {task['task_id']} to {agent_id}"
                        )
                    
                    # Put agent back in rotation
                    available_agents.append(agent_id)
                
                await asyncio.sleep(0.1)
                
            except Exception as e:
                self.logger.error(f"Task distribution error: {e}")
                await asyncio.sleep(1)
    
    async def generate_test_tasks(self):
        """Generate test tasks for demonstration"""
        task_counter = 0
        
        while self.running:
            await asyncio.sleep(10)  # Generate a task every 10 seconds
            
            if len(self.task_queue) < 5:  # Keep queue small
                task_counter += 1
                task = {
                    'task_id': f'task-{task_counter}',
                    'type': 'demo_task',
                    'created': datetime.utcnow().isoformat(),
                    'data': {
                        'message': f'Demo task #{task_counter}'
                    }
                }
                self.task_queue.append(task)
                self.logger.info(f"Generated test task: {task['task_id']}")
    
    async def start(self):
        """Start the hive coordinator"""
        self.running = True
        self.logger.info("Starting Hive Coordinator")
        
        await self.connect_redis()
        
        # Start coordination tasks
        tasks = [
            asyncio.create_task(self.monitor_agents()),
            asyncio.create_task(self.listen_for_results()),
            asyncio.create_task(self.distribute_tasks()),
            asyncio.create_task(self.generate_test_tasks()),
        ]
        
        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            self.logger.info("Coordinator tasks cancelled")
        finally:
            self.running = False
            if self.redis_client:
                await self.redis_client.close()
    
    async def stop(self):
        """Stop the coordinator"""
        self.logger.info("Stopping Hive Coordinator")
        self.running = False
