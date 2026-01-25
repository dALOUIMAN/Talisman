# NoxCore Agent Zero - AI Environment

## Overview

Agent Zero is an ultra-lightweight, AI-focused distributed agent system built for the NoxCore project. It provides a hive-based architecture where multiple AI agents coordinate through a central coordinator to handle complex tasks efficiently.

## Architecture

### Components

1. **Hive Coordinator** - Central coordination hub that manages agent registration, task distribution, and hive intelligence
2. **Worker Agents** - Lightweight AI agents that execute tasks assigned by the coordinator
3. **Redis** - Communication backbone for the agent hive
4. **Docker** - Containerization for consistent deployment

### Design Philosophy

- **Ultra-lightweight**: Built on Alpine Linux, minimal dependencies
- **AI-focused**: Designed specifically for AI agent operations
- **Distributed**: Hive architecture allows horizontal scaling
- **Efficient**: Optimized for low resource usage (CPU, GPU, memory)
- **Flexible**: Can run locally or connect to larger "tribe leaders"

## Quick Start

### Prerequisites

- Docker
- Docker Compose
- 512MB RAM minimum
- Linux/macOS/Windows with WSL2

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dALOUIMAN/Talisman.git
cd Talisman/noxcore/agent-zero
```

2. Configure environment (optional):
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Start the hive:
```bash
docker-compose up -d
```

4. Check status:
```bash
docker-compose ps
docker-compose logs -f coordinator
```

### Stopping the Hive

```bash
docker-compose down
```

To also remove volumes:
```bash
docker-compose down -v
```

## Configuration

### Environment Variables

- `AGENT_MODE`: Operating mode (local/distributed)
- `AGENT_HIVE`: Enable hive coordination (enabled/disabled)
- `REDIS_HOST`: Redis server hostname
- `REDIS_PORT`: Redis server port
- `MAX_AGENTS`: Maximum number of agents in the hive
- `LOG_LEVEL`: Logging level (DEBUG/INFO/WARNING/ERROR)

### Scaling

To add more worker agents:

```bash
docker-compose up -d --scale agent-worker-1=5
```

Or edit `docker-compose.yml` to add more worker services.

## Architecture Details

### Hive Communication

Agents communicate through Redis pub/sub channels:

- `agent:<id>:tasks` - Individual agent task channel
- `broadcast:tasks` - Broadcast channel for all agents
- `coordinator:results` - Results channel to coordinator

### Task Flow

1. Coordinator generates or receives tasks
2. Tasks are added to the internal queue
3. Coordinator distributes tasks to available agents
4. Agents execute tasks and report results
5. Coordinator tracks completion and updates statistics

### Agent Lifecycle

1. **Startup**: Agent connects to Redis and registers with hive
2. **Heartbeat**: Periodic updates maintain registration (every 60s)
3. **Task Listening**: Agent subscribes to task channels
4. **Execution**: Tasks are executed as received
5. **Shutdown**: Clean disconnect and deregistration

## Development

### Project Structure

```
noxcore/agent-zero/
├── Dockerfile              # Alpine-based container image
├── docker-compose.yml      # Multi-container orchestration
├── requirements.txt        # Python dependencies
├── agent-zero-runner.py    # Main entry point
├── agents/                 # Agent implementations
│   ├── __init__.py
│   └── base_agent.py       # Base agent class
├── coordinator/            # Hive coordinator
│   ├── __init__.py
│   └── hive_coordinator.py
├── tools/                  # Utility tools
│   ├── __init__.py
│   └── agent_tools.py
└── config/                 # Configuration files
    └── agent-config.yml
```

### Adding Custom Agents

Create a new agent class extending `BaseAgent`:

```python
from agents.base_agent import BaseAgent

class CustomAgent(BaseAgent):
    async def execute_task(self, task):
        # Your custom logic here
        pass
```

### Adding New Tools

Add tools to `tools/agent_tools.py`:

```python
class CustomTool:
    @staticmethod
    async def process(data):
        # Your tool logic
        return result
```

## NoxCore Integration

This Agent Zero environment is part of the larger NoxCore project:

- **Safe Room**: Provides isolated AI workspace
- **Lab Toolbox**: Tools and utilities for AI development
- **Flexible Deployment**: Runs on everything from laptops to servers
- **Based on Alpine Linux**: Following Mazak philosophy of lightweight, efficient systems

## Performance

### Resource Usage (per agent)

- **Memory**: ~50-100 MB
- **CPU**: <5% idle, 10-30% under load
- **Disk**: ~100 MB Docker image
- **Network**: Minimal (Redis pub/sub)

### Scaling Capabilities

- **Local Mode**: 3-10 agents on typical laptop
- **Server Mode**: 50+ agents on dedicated hardware
- **Distributed Mode**: Unlimited with proper Redis cluster

## Troubleshooting

### Agents not connecting

Check Redis connectivity:
```bash
docker-compose logs redis
docker-compose exec coordinator ping redis
```

### High resource usage

1. Reduce number of agents
2. Adjust `MAX_MEMORY_MB` and `MAX_CPU_PERCENT` in `.env`
3. Check for memory leaks in custom agents

### Tasks not executing

Check coordinator logs:
```bash
docker-compose logs -f coordinator
```

Check agent logs:
```bash
docker-compose logs -f agent-worker-1
```

## Future Enhancements

- [ ] Web UI for monitoring hive status
- [ ] Advanced task scheduling algorithms
- [ ] GPU/CUDA support for ML workloads
- [ ] Integration with external AI APIs
- [ ] VR visualization interface
- [ ] Enhanced security and authentication
- [ ] Persistent task storage
- [ ] Advanced metrics and monitoring

## Contributing

This is part of the NoxCore project. For contributions:

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

Part of the Talisman/NoxCore project.

## Contact

For questions or support regarding Agent Zero, contact the NoxCore team.

---

*"To boldly build what no AI has ever built"* - NoxCore Philosophy
