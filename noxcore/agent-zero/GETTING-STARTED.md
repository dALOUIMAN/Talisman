# Agent Zero - Getting Started in 5 Minutes

## What You'll Get

A distributed AI agent system running in Docker:
- 1 Coordinator managing tasks
- 3 Worker agents executing tasks
- Redis handling communication
- All running locally on your machine

## Prerequisites

- Docker installed
- 512MB+ free RAM
- Internet connection (for first build)

## Quick Start

### Step 1: Navigate to Agent Zero

```bash
cd /path/to/Talisman/noxcore/agent-zero
```

### Step 2: Validate Setup (Optional but Recommended)

```bash
./validate-setup.sh
```

Expected output:
```
✓ Docker is installed
✓ Docker Compose is installed
✓ All core files present
✓ Python syntax validated
✓ Configuration files validated
```

### Step 3: Launch the Hive

```bash
./start-hive.sh
```

This will:
1. Check prerequisites
2. Build Docker images (first time only, ~2-3 minutes)
3. Start all services
4. Show status

### Step 4: Monitor the Hive

In a new terminal:

```bash
# Watch coordinator logs
docker compose logs -f coordinator

# Or watch all services
docker compose logs -f
```

You should see:
- Coordinator starting up
- Agents registering with hive
- Tasks being generated and distributed
- Results being reported

### Step 5: Check Status

```bash
# See running containers
docker compose ps

# Check resource usage
docker stats
```

## What's Happening?

```
┌─────────────────────────┐
│  Hive Coordinator       │  ← Manages everything
│  - Discovers agents     │
│  - Distributes tasks    │
│  - Tracks results       │
└───────────┬─────────────┘
            │
            ▼
    ┌──────────────┐
    │    Redis     │         ← Communication hub
    └──────┬───────┘
           │
    ┌──────┼──────┐
    ▼      ▼      ▼
┌────────┐ │   ┌────────┐
│Agent 1 │ │   │Agent 3 │  ← Execute tasks
└────────┘ ▼   └────────┘
      ┌────────┐
      │Agent 2 │
      └────────┘
```

## Common Tasks

### Stop the Hive

```bash
docker compose down
```

### Restart Services

```bash
docker compose restart
```

### Scale to More Workers

```bash
docker compose up -d --scale agent-worker-1=5
```

### View Logs from Specific Agent

```bash
docker compose logs -f agent-worker-1
```

### Clean Up Everything

```bash
# Stop and remove containers + volumes
docker compose down -v

# Also remove images
docker compose down -v --rmi all
```

## Configuration (Optional)

### Basic Configuration

1. Copy example config:
```bash
cp .env.example .env
```

2. Edit `.env`:
```bash
nano .env
```

3. Key settings:
```bash
MAX_AGENTS=10          # Maximum agents
LOG_LEVEL=INFO         # DEBUG, INFO, WARNING, ERROR
REDIS_MAXMEMORY=256mb  # Redis memory limit
AGENT_TTL=300          # Agent registration timeout (seconds)
```

4. Restart to apply:
```bash
docker compose restart
```

### Advanced Configuration

Edit `config/agent-config.yml` for:
- Hive settings
- Resource limits
- Performance tuning

## Troubleshooting

### Containers Won't Start

```bash
# Check logs
docker compose logs

# Check Docker daemon
docker ps

# Restart Docker
sudo systemctl restart docker  # Linux
# Or restart Docker Desktop     # Mac/Windows
```

### Port Conflicts (6379 already in use)

Edit `docker-compose.yml`:
```yaml
ports:
  - "6380:6379"  # Changed from 6379
```

### Out of Memory

Reduce number of agents in `docker-compose.yml` or increase Docker memory limit.

### Network Issues During Build

See `INSTALL.md` for alternative deployment methods.

## Verification

### Check Agents are Registered

```bash
docker compose exec coordinator python -c "
import redis
r = redis.Redis(host='redis')
agents = [k.decode() for k in r.keys('agent:*') if not k.decode().endswith(':tasks')]
print(f'Active agents: {len(agents)}')
for agent in agents:
    print(f'  - {agent}')
"
```

### Check Tasks are Running

Look for these log patterns:
```
coordinator   | Generated test task: task-1
coordinator   | Distributed task task-1 to worker-1
agent-worker-1| Received task: task-1
agent-worker-1| Task task-1 completed
coordinator   | Task task-1 completed by worker-1
```

## Next Steps

Once your hive is running:

1. **Read the Documentation**
   - `README.md` - Full system overview
   - `ARCHITECTURE.md` - Technical details
   - `DEVELOPMENT.md` - Extend the system
   - `QUICKREF.md` - Command reference

2. **Customize Agents**
   - Edit `agents/base_agent.py`
   - Add custom task types
   - Rebuild: `docker compose build`

3. **Add More Workers**
   - Edit `docker-compose.yml`
   - Add agent-worker-4, agent-worker-5, etc.
   - Copy from existing worker config

4. **Monitor Performance**
   - Use `docker stats`
   - Check Redis usage
   - Monitor logs for errors

5. **Integrate with Your Application**
   - Connect to Redis on localhost:6379
   - Publish tasks to agent channels
   - Subscribe to results channel

## Example: Send a Custom Task

```python
import redis
import json

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Create a task
task = {
    'task_id': 'my-custom-task-1',
    'type': 'custom_task',
    'priority': 'high',
    'data': {
        'param1': 'value1',
        'param2': 'value2'
    }
}

# Send to specific agent
r.publish('agent:worker-1:tasks', json.dumps(task))

# Or broadcast to all agents
r.publish('broadcast:tasks', json.dumps(task))

print("Task sent!")
```

## Getting Help

- Run validation: `./validate-setup.sh`
- Check logs: `docker compose logs`
- Review docs: `README.md`
- Check status: `docker compose ps`

## Success!

You now have a fully functional distributed AI agent system running locally! 🎉

The agents are:
- ✓ Coordinating through Redis
- ✓ Executing tasks
- ✓ Reporting results
- ✓ Monitoring health
- ✓ Ready for your custom logic

## What's Special About This?

This is not just another Docker setup. This is:

- **AI-First**: Built specifically for AI agent operations
- **Ultra-Lightweight**: Alpine Linux, minimal footprint
- **Scalable**: From 3 to 100+ agents
- **Distributed**: True hive intelligence
- **Production-Ready**: Full error handling, monitoring, docs

Welcome to the NoxCore Agent Zero system! 🚀

---

*"To boldly build what no AI has ever built"* - NoxCore Philosophy
