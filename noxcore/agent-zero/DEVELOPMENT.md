# Agent Zero Development Guide

## Architecture Overview

### Components

```
┌─────────────────────────────────────────────────────┐
│                    Hive Coordinator                  │
│  - Task Distribution                                 │
│  - Agent Registry                                    │
│  - Health Monitoring                                 │
└──────────────────┬──────────────────────────────────┘
                   │
           ┌───────┴───────┐
           │     Redis     │ (Communication Backbone)
           └───────┬───────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
┌───▼───┐     ┌───▼───┐     ┌───▼───┐
│Agent 1│     │Agent 2│     │Agent 3│
│Worker │     │Worker │     │Worker │
└───────┘     └───────┘     └───────┘
```

### Communication Flow

1. **Task Submission**
   - Coordinator receives/generates tasks
   - Tasks added to internal queue
   - Coordinator tracks task state

2. **Task Distribution**
   - Coordinator checks available agents
   - Tasks distributed round-robin
   - Published to agent-specific channels

3. **Task Execution**
   - Agent receives task via Redis pubsub
   - Task executed asynchronously
   - Results published to coordinator

4. **Result Handling**
   - Coordinator receives results
   - Updates statistics
   - Triggers follow-up actions

## Code Structure

### Base Agent (`agents/base_agent.py`)

**Key Methods:**
- `connect_redis()` - Establish hive connection
- `register_with_hive()` - Register agent availability
- `heartbeat()` - Maintain registration (every 60s)
- `listen_for_tasks()` - Subscribe to task channels
- `execute_task()` - Task execution logic
- `start()` - Agent lifecycle startup
- `stop()` - Graceful shutdown

**Extension Points:**
```python
class CustomAgent(BaseAgent):
    async def execute_task(self, task):
        # Override for custom task handling
        task_type = task.get('type')
        
        if task_type == 'my_custom_task':
            result = await self.handle_custom_task(task)
        else:
            result = await super().execute_task(task)
        
        return result
    
    async def handle_custom_task(self, task):
        # Your custom logic
        pass
```

### Hive Coordinator (`coordinator/hive_coordinator.py`)

**Key Methods:**
- `discover_agents()` - Find active agents
- `monitor_agents()` - Health check loop
- `listen_for_results()` - Process task results
- `distribute_tasks()` - Assign tasks to agents
- `generate_test_tasks()` - Demo task generation

**Extension Points:**
```python
class CustomCoordinator(HiveCoordinator):
    async def distribute_tasks(self):
        # Override for custom distribution logic
        # e.g., priority-based, load-balanced, etc.
        pass
    
    async def handle_agent_failure(self, agent_id):
        # Custom failure handling
        pass
```

### Tools (`tools/agent_tools.py`)

**AgentTools Class:**
- `analyze_task()` - Task complexity analysis
- `validate_task()` - Task structure validation
- `execute_ai_task()` - AI-specific execution

**HiveProtocol Class:**
- `format_message()` - Message serialization
- `parse_message()` - Message deserialization

## Adding New Features

### Adding a New Task Type

1. **Define task structure:**
```python
task = {
    'task_id': 'unique-id',
    'type': 'my_new_task',
    'priority': 'high',
    'data': {
        'param1': 'value1',
        'param2': 'value2'
    }
}
```

2. **Create handler in agent:**
```python
# agents/custom_agent.py
async def handle_my_new_task(self, task):
    data = task.get('data', {})
    # Process task
    result = do_something(data)
    return {
        'success': True,
        'result': result
    }
```

3. **Update executor:**
```python
async def execute_task(self, task):
    task_type = task.get('type')
    
    if task_type == 'my_new_task':
        return await self.handle_my_new_task(task)
    # ... other handlers
```

### Adding a New Communication Channel

1. **Define channel pattern:**
```python
CHANNEL_PATTERN = 'custom:channel:{agent_id}'
```

2. **Subscribe in agent:**
```python
await pubsub.subscribe(
    f"custom:channel:{self.agent_id}"
)
```

3. **Publish from coordinator:**
```python
await self.redis_client.publish(
    f"custom:channel:{agent_id}",
    json.dumps(message)
)
```

### Adding Metrics/Monitoring

1. **Add metrics collection:**
```python
# agents/base_agent.py
self.metrics = {
    'tasks_completed': 0,
    'tasks_failed': 0,
    'avg_execution_time': 0.0
}
```

2. **Update metrics:**
```python
async def execute_task(self, task):
    start = time.time()
    try:
        # Execute task
        self.metrics['tasks_completed'] += 1
    except:
        self.metrics['tasks_failed'] += 1
    finally:
        duration = time.time() - start
        # Update avg_execution_time
```

3. **Report metrics:**
```python
async def report_metrics(self):
    await self.redis_client.set(
        f"metrics:{self.agent_id}",
        json.dumps(self.metrics)
    )
```

## Testing

### Unit Testing

Create `tests/test_agent.py`:
```python
import pytest
from agents.base_agent import BaseAgent

@pytest.mark.asyncio
async def test_agent_creation():
    agent = BaseAgent('test-agent-1', 'worker')
    assert agent.agent_id == 'test-agent-1'
    assert agent.agent_type == 'worker'

@pytest.mark.asyncio
async def test_task_execution():
    agent = BaseAgent('test-agent-1', 'worker')
    task = {
        'task_id': 'test-1',
        'type': 'demo_task',
        'data': {}
    }
    # Mock Redis, test execution
```

### Integration Testing

Create `tests/test_integration.py`:
```python
import pytest
import docker

@pytest.mark.asyncio
async def test_hive_startup():
    client = docker.from_env()
    # Start services
    # Verify connectivity
    # Check agent registration
```

### Manual Testing

```bash
# Terminal 1: Start hive
./start-hive.sh

# Terminal 2: Monitor logs
docker compose logs -f

# Terminal 3: Check agent registry
docker compose exec coordinator python -c "
import redis
r = redis.Redis(host='redis')
agents = r.keys('agent:*')
print(f'Active agents: {len(agents)}')
for agent in agents:
    print(r.get(agent))
"
```

## Performance Optimization

### Agent Performance

1. **Reduce heartbeat frequency:**
```python
await asyncio.sleep(120)  # 2 minutes instead of 1
```

2. **Batch operations:**
```python
# Instead of individual publishes
await self.redis_client.pipeline()
```

3. **Connection pooling:**
```python
self.redis_client = await redis.from_url(
    url,
    max_connections=10
)
```

### Coordinator Performance

1. **Parallel task distribution:**
```python
await asyncio.gather(*[
    distribute_to_agent(agent, task)
    for agent, task in zip(agents, tasks)
])
```

2. **Caching agent registry:**
```python
# Cache for 30 seconds
if time.time() - self.last_discovery < 30:
    return self.cached_agents
```

## Best Practices

### Code Style

- Follow PEP 8
- Use type hints
- Document with docstrings
- Keep functions focused

### Error Handling

```python
try:
    result = await execute_task(task)
except SpecificError as e:
    logger.error(f"Specific error: {e}")
    # Handle specifically
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    # General handling
finally:
    # Cleanup
```

### Logging

```python
# Use appropriate levels
logger.debug("Detailed info")
logger.info("General info")
logger.warning("Warning")
logger.error("Error", exc_info=True)
```

### Resource Management

```python
async def cleanup(self):
    try:
        if self.redis_client:
            await self.redis_client.close()
    except Exception as e:
        logger.error(f"Cleanup error: {e}")
```

## Deployment

### Development
```bash
docker compose up
```

### Production
```bash
docker compose -f docker-compose.prod.yml up -d
```

### Monitoring
- Prometheus + Grafana
- ELK Stack
- Custom dashboards

## Contributing

1. Fork repository
2. Create feature branch
3. Write tests
4. Update documentation
5. Submit PR

## Resources

- Python AsyncIO: https://docs.python.org/3/library/asyncio.html
- Redis Python: https://redis-py.readthedocs.io/
- Docker Compose: https://docs.docker.com/compose/
- Pydantic: https://docs.pydantic.dev/
