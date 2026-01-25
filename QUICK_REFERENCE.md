# Agent Zero - Quick Reference Card

## Quick Start Commands

### Initial Setup
```bash
./setup.sh                    # Run complete setup
# OR using make
make setup                    # Alternative setup method
```

### Service Management
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# Restart services
docker-compose restart

# View logs
docker-compose logs -f

# Check status
docker-compose ps
```

### Access Containers
```bash
# Coordinator
docker exec -it agentzero-coordinator /bin/bash

# Worker
docker exec -it agentzero-worker-1 /bin/bash

# NoxCore Console
docker exec -it noxcore-console /bin/bash
```

### Run Applications
```bash
# Run Agent Zero coordinator
docker exec -it agentzero-coordinator python /workspace/agentzero/agent_zero.py

# Run NoxCore console
docker exec -it noxcore-console python /workspace/noxcore/console/console.py

# Python interactive mode
docker exec -it agentzero-coordinator python
```

### Scaling
```bash
# Scale workers
docker-compose up -d --scale agent-zero-worker-1=5

# Using make
make scale N=5
```

## Makefile Commands

```bash
make help           # Show all available commands
make setup          # Initial setup
make build          # Build images
make up             # Start services
make down           # Stop services
make restart        # Restart services
make logs           # View logs
make status         # Service status
make shell          # Access coordinator
make console        # Access NoxCore console
make test           # Run tests
make clean          # Clean up
make rebuild        # Full rebuild
make scale N=5      # Scale workers
```

## Port Map

| Service             | Port | Protocol |
|---------------------|------|----------|
| Coordinator API     | 8000 | HTTP     |
| WebSocket           | 8001 | WS       |
| NoxCore Console     | 3000 | HTTP     |

## File Structure

```
Talisman/
├── agentzero/              # Agent Zero core
│   ├── agent_zero.py       # Main agent
│   ├── agents/             # Agent modules
│   ├── tools/              # Agent tools
│   ├── hive/               # Hive coordination
│   └── config/             # Configuration
├── noxcore/                # NoxCore system
│   ├── console/            # Console UI
│   ├── protocols/          # Communication
│   └── config/             # Configuration
├── data/                   # Persistent data
├── logs/                   # Log files
├── Dockerfile              # Container image
├── docker-compose.yml      # Orchestration
├── requirements.txt        # Python deps
├── setup.sh               # Setup script
├── Makefile               # Make commands
├── README.md              # Main docs
├── GETTING_STARTED.md     # Setup guide
└── ARCHITECTURE.md        # Design docs
```

## Environment Variables

Key variables in `.env`:

```bash
# Agent
AGENT_ID=coordinator-001
AGENT_ROLE=coordinator
HIVE_MODE=enabled

# API Keys
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key

# Network
COORDINATOR_HOST=coordinator
COORDINATOR_PORT=8000

# Performance
MAX_WORKERS=4
MEMORY_LIMIT=2G
```

## Python Quick Usage

### Hive Manager
```python
from agentzero.hive.hive_manager import HiveManager, TaskPriority

hive = HiveManager()
hive.register_agent('agent-1', ['coding', 'analysis'])
task = hive.create_task('task-1', 'Test task', TaskPriority.HIGH)
status = hive.get_hive_status()
```

### Agent Tools
```python
from agentzero.tools.agent_tools import get_tool

tool = get_tool('code_analysis')
result = tool.analyze('print("hello")', 'python')
```

### NoxCore Protocol
```python
from noxcore.protocols.noxcore_protocol import NoxCoreProtocol, ProtocolMessage

protocol = NoxCoreProtocol()
protocol.create_channel('ch1', ProtocolType.COMMUNICATION)
```

## Common Issues

### Port in Use
```bash
# Change ports in docker-compose.yml
ports:
  - "8080:8000"  # Use 8080 instead
```

### Insufficient Memory
```bash
# Reduce worker count
docker-compose up -d --scale agent-zero-worker-1=2
```

### Build Fails
```bash
# Clean rebuild
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Documentation Links

- **README.md**: Overview and features
- **GETTING_STARTED.md**: Detailed setup guide
- **ARCHITECTURE.md**: System design
- **noxcore/config/noxcore.yml**: NoxCore configuration
- **agentzero/config/agent.env**: Agent configuration

## Support

For issues or questions:
1. Check logs: `docker-compose logs -f`
2. Review documentation
3. Check service status: `docker-compose ps`
4. Verify configuration files

---

**Agent Zero** - "To boldly build what no AI has ever built before" 🚀
