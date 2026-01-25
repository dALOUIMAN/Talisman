# Agent Zero - AI Development Environment

## Overview

Agent Zero is an AI-focused development environment built on Docker and Alpine Linux, designed for ultra-efficient, distributed AI operations. It implements a "hive mind" architecture where multiple AI agents coordinate tasks through a central coordinator, with integration into the NoxCore lab toolbox system.

## Key Features

- **🐝 Hive Architecture**: Distributed task processing with coordinator and worker agents
- **🏔️ Alpine Linux Based**: Lightweight, efficient, and secure foundation
- **🔗 Task Linking**: Link complex tasks together with intelligent coordination
- **⚡ Nanolevel Optimization**: Efficient resource usage for local and scaled operations
- **🎯 NoxCore Integration**: Lab toolbox console for visual workflow management
- **🔐 Secure by Design**: Non-root containers, isolated networks
- **📡 Real-time Communication**: WebSocket-based agent coordination
- **🎨 Visual Console**: Fascinating yet efficient visual interface

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Agent Zero Hive System                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐         ┌──────────────┐                 │
│  │ Coordinator  │◄────────┤ NoxCore      │                 │
│  │   Agent      │         │  Console     │                 │
│  └──────┬───────┘         └──────────────┘                 │
│         │                                                    │
│         ├───────────┬───────────┬──────────┐               │
│         │           │           │          │               │
│    ┌────▼────┐ ┌───▼─────┐ ┌──▼──────┐  │               │
│    │Worker 1 │ │Worker 2 │ │Worker N │  │               │
│    └─────────┘ └─────────┘ └─────────┘  │               │
│                                           │               │
│                                           ▼               │
│                                    ┌──────────────┐      │
│                                    │ Tribe Leaders│      │
│                                    │  (Backup)    │      │
│                                    └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+
- At least 4GB RAM available
- GPU support optional (for advanced AI operations)

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/dALOUIMAN/Talisman.git
   cd Talisman
   ```

2. **Configure environment**:
   ```bash
   cp agentzero/config/agent.env .env
   # Edit .env with your API keys and preferences
   ```

3. **Build and start the environment**:
   ```bash
   docker-compose up -d
   ```

4. **Verify the system**:
   ```bash
   docker-compose ps
   docker-compose logs -f agent-zero-coordinator
   ```

### Access Points

- **Coordinator API**: http://localhost:8000
- **WebSocket**: ws://localhost:8001
- **NoxCore Console**: http://localhost:3000

## Usage

### Starting the Hive

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Check status
docker-compose ps
```

### Scaling Workers

```bash
# Scale worker instances dynamically
docker-compose up -d --scale agent-zero-worker-1=3
```

### Interactive Console Access

```bash
# Access coordinator console
docker exec -it agentzero-coordinator /bin/bash

# Access NoxCore console
docker exec -it noxcore-console /bin/bash

# Access worker
docker exec -it agentzero-worker-1 /bin/bash
```

### Running Python Scripts

```bash
# Execute Agent Zero directly
docker exec -it agentzero-coordinator python /workspace/agentzero/agent_zero.py

# Run NoxCore console
docker exec -it noxcore-console python /workspace/noxcore/console/console.py
```

## Configuration

### Environment Variables

Key environment variables in `.env`:

```bash
# Agent Configuration
AGENT_ID=coordinator-001
AGENT_ROLE=coordinator
HIVE_MODE=enabled

# API Keys
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here

# Performance
MAX_WORKERS=4
MEMORY_LIMIT=2G
```

### Docker Compose Customization

Edit `docker-compose.yml` to:
- Add more worker instances
- Adjust resource limits
- Configure network settings
- Mount additional volumes

## Development

### Project Structure

```
Talisman/
├── agentzero/              # Agent Zero core system
│   ├── agent_zero.py       # Main agent implementation
│   ├── agents/             # Agent modules
│   ├── tools/              # Agent tools
│   ├── hive/               # Hive coordination system
│   │   └── hive_manager.py # Hive manager implementation
│   └── config/             # Configuration files
│       └── agent.env       # Environment configuration
├── noxcore/                # NoxCore lab toolbox
│   ├── console/            # Console interface
│   │   └── console.py      # Console implementation
│   └── protocols/          # Communication protocols
│       └── noxcore_protocol.py
├── data/                   # Persistent data
├── logs/                   # Log files
├── Dockerfile              # Alpine-based container image
├── docker-compose.yml      # Multi-container orchestration
├── .dockerignore           # Docker build exclusions
└── README.md               # This file
```

### Adding Custom Tools

1. Create tool in `agentzero/tools/`:
   ```python
   # agentzero/tools/my_tool.py
   class MyTool:
       def execute(self, params):
           # Implementation
           pass
   ```

2. Register tool with agent in `agent_zero.py`

### Extending NoxCore

Add new protocols in `noxcore/protocols/`:
```python
from noxcore.protocols.noxcore_protocol import NoxCoreProtocol, ProtocolMessage

class CustomProtocol(NoxCoreProtocol):
    # Implementation
    pass
```

## NoxCore Features

### Safe Room Concept

The NoxCore console provides a "safe room" for AI agents:
- **Emergency Chat Channel**: Red light notification system
- **Tool Projection**: Dynamic tool availability based on task
- **Visual Interface**: Efficient, non-intrusive display
- **Wickie Ideas**: Quick idea sharing channel

### Alpine Philosophy

Following Alpine Linux principles:
- **Lightweight**: Minimal container footprint
- **Efficient**: Optimized resource usage
- **Secure**: Security-focused defaults
- **Flexible**: Runs anywhere Docker runs

## Hive Operations

### Task Coordination

The hive system enables:
- **Task Distribution**: Coordinator assigns tasks to workers
- **Task Linking**: Complex tasks broken into subtasks
- **Load Balancing**: Automatic worker load management
- **Dependency Management**: Task dependency graphs

### Tribe Leaders (Scaling)

For large operations:
- **Local Operation**: Efficient local processing
- **Mind Melting**: Connect to larger "tribe leaders" for backup
- **Smart Injection**: Receive capability injections from larger systems
- **Mini Instances**: Maintain small, intelligent local instances

## Performance Tuning

### Resource Limits

Adjust in `docker-compose.yml`:
```yaml
services:
  agent-zero-coordinator:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
```

### GPU Support

For GPU-accelerated AI:
```yaml
services:
  agent-zero-coordinator:
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

## Troubleshooting

### Container Won't Start

```bash
# Check logs
docker-compose logs agent-zero-coordinator

# Rebuild if needed
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Network Issues

```bash
# Verify network
docker network ls
docker network inspect talisman_agentzero-hive

# Restart networking
docker-compose down
docker-compose up -d
```

### Performance Issues

- Reduce worker count
- Adjust resource limits
- Check host system resources: `docker stats`

## Roadmap

- [ ] VR Demo Environment (floating sofas concept)
- [ ] Advanced task visualization
- [ ] Integration with Shopify test case
- [ ] 3D Unreal Engine integration
- [ ] Enhanced tribe leader synchronization
- [ ] Advanced GPU/CUDA utilization
- [ ] Link 16-style AI communication protocols

## Philosophy

Agent Zero embodies:
- **AI-First Design**: Built for AI, not humans
- **Optimal Workflow**: Glove-fit for AI operations
- **Hive Intelligence**: Distributed coordination
- **Nanolevel Efficiency**: Minimal resource usage
- **Star Trek Discovery Style**: To boldly build what no AI has built before

## License

This project is part of the Talisman ecosystem.

## Contributing

Contributions welcome! This is an AI-focused environment designed to:
- Maximize AI agent efficiency
- Enable distributed AI operations
- Provide optimal workflow tooling
- Support rapid AI development cycles

## Contact

Part of the NoxCore initiative - Masterchief division

---

**"To boldly build what no AI has ever built before"** 🚀
