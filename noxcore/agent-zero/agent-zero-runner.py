#!/usr/bin/env python3
"""
Agent Zero Runner - Main entry point for AI agents
NoxCore Agent Zero Environment - Lightweight distributed AI system
"""

import os
import sys
import asyncio
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('AgentZero')

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.base_agent import BaseAgent
from coordinator.hive_coordinator import HiveCoordinator


async def main():
    """Main entry point for Agent Zero"""
    agent_type = os.getenv('AGENT_TYPE', 'worker')
    agent_id = os.getenv('AGENT_ID', 'agent-1')
    
    logger.info(f"Starting Agent Zero - Type: {agent_type}, ID: {agent_id}")
    
    try:
        if agent_type == 'coordinator':
            logger.info("Initializing Hive Coordinator")
            coordinator = HiveCoordinator(agent_id)
            await coordinator.start()
        else:
            logger.info("Initializing Worker Agent")
            agent = BaseAgent(agent_id, agent_type)
            await agent.start()
            
    except KeyboardInterrupt:
        logger.info("Shutdown signal received")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)
    finally:
        logger.info("Agent Zero shutdown complete")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(0)
