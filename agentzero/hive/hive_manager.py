"""
Hive Manager - Coordinates distributed AI agent operations
Implements the "hive mind" concept for linking tasks across agents
"""

import asyncio
import logging
from typing import Dict, List, Set, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class TaskPriority(Enum):
    """Task priority levels"""
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4


@dataclass
class HiveTask:
    """Distributed task across the hive"""
    task_id: str
    description: str
    priority: TaskPriority
    subtasks: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    assigned_agents: Set[str] = field(default_factory=set)
    status: str = "pending"
    created_at: datetime = field(default_factory=datetime.now)


class HiveManager:
    """
    Manages the hive system - coordinates multiple agents
    Implements task linking and distribution across the network
    """
    
    def __init__(self):
        self.tasks: Dict[str, HiveTask] = {}
        self.agents: Dict[str, Dict] = {}
        self.task_graph: Dict[str, List[str]] = {}
        logger.info("Hive Manager initialized")
        
    def register_agent(self, agent_id: str, capabilities: List[str]):
        """Register an agent with the hive"""
        self.agents[agent_id] = {
            'capabilities': capabilities,
            'status': 'active',
            'load': 0,
            'last_seen': datetime.now()
        }
        logger.info(f"Agent registered: {agent_id} with capabilities: {capabilities}")
        
    def create_task(self, task_id: str, description: str, 
                   priority: TaskPriority, subtasks: List[str] = None) -> HiveTask:
        """Create a new task in the hive"""
        task = HiveTask(
            task_id=task_id,
            description=description,
            priority=priority,
            subtasks=subtasks or []
        )
        self.tasks[task_id] = task
        
        # Build task graph for dependencies
        if subtasks:
            self.task_graph[task_id] = subtasks
            
        logger.info(f"Hive task created: {task_id} - {description}")
        return task
        
    def link_tasks(self, parent_task_id: str, child_task_ids: List[str]):
        """Link tasks together - implements the coordinator pattern"""
        if parent_task_id not in self.tasks:
            logger.error(f"Parent task {parent_task_id} not found")
            return
            
        parent_task = self.tasks[parent_task_id]
        parent_task.subtasks.extend(child_task_ids)
        
        # Add to task graph
        if parent_task_id not in self.task_graph:
            self.task_graph[parent_task_id] = []
        self.task_graph[parent_task_id].extend(child_task_ids)
        
        logger.info(f"Linked tasks: {parent_task_id} -> {child_task_ids}")
        
    async def assign_task(self, task_id: str) -> Optional[str]:
        """Assign a task to the most suitable agent"""
        if task_id not in self.tasks:
            logger.error(f"Task {task_id} not found")
            return None
            
        task = self.tasks[task_id]
        
        # Find agent with lowest load
        available_agents = [
            (agent_id, info) 
            for agent_id, info in self.agents.items() 
            if info['status'] == 'active'
        ]
        
        if not available_agents:
            logger.warning("No available agents for task assignment")
            return None
            
        # Sort by load and assign
        available_agents.sort(key=lambda x: x[1]['load'])
        selected_agent = available_agents[0][0]
        
        task.assigned_agents.add(selected_agent)
        task.status = "assigned"
        self.agents[selected_agent]['load'] += 1
        
        logger.info(f"Task {task_id} assigned to agent {selected_agent}")
        return selected_agent
        
    def get_hive_status(self) -> Dict:
        """Get overall hive status"""
        return {
            'total_agents': len(self.agents),
            'active_agents': len([a for a in self.agents.values() if a['status'] == 'active']),
            'total_tasks': len(self.tasks),
            'pending_tasks': len([t for t in self.tasks.values() if t.status == 'pending']),
            'active_tasks': len([t for t in self.tasks.values() if t.status == 'assigned']),
            'completed_tasks': len([t for t in self.tasks.values() if t.status == 'completed']),
            'task_graph_size': len(self.task_graph)
        }
        
    def visualize_task_graph(self) -> str:
        """Generate a text representation of the task graph"""
        lines = ["Task Dependency Graph:", "=" * 50]
        
        for parent, children in self.task_graph.items():
            lines.append(f"\n{parent}")
            for child in children:
                lines.append(f"  └─> {child}")
                
        return "\n".join(lines)
