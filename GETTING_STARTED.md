# Agent Zero - Getting Started Guide

This guide will help you get up and running with the Agent Zero AI development environment.

## What is Agent Zero?

Agent Zero is a Docker-based AI development environment that implements a "hive mind" architecture for distributed AI operations. It's built on Alpine Linux for maximum efficiency and is designed to be AI-first, not human-first.

## Key Concepts

### 1. Hive Architecture
- **Coordinator**: Central agent that distributes tasks
- **Workers**: Agent instances that process tasks
- **Task Linking**: Connect related tasks for coordinated execution

### 2. NoxCore Integration
- **Console**: Visual interface for monitoring and control
- **Protocols**: Communication standards based on Alpine Linux philosophy
- **Safe Room**: Isolated environment for efficient AI operations

### 3. Tribe Leaders
- **Local Operation**: Run efficiently on local hardware
- **Mind Melting**: Connect to larger systems for backup processing
- **Smart Injection**: Receive capability boosts from distributed systems

## Installation Steps

### Step 1: Prerequisites

Ensure you have:
- Docker 20.10 or later
- Docker Compose 2.0 or later
- At least 4GB available RAM
- (Optional) NVIDIA GPU with drivers for GPU acceleration

Check installations:
```bash
docker --version
docker-compose --version
```

### Step 2: Clone and Setup

```bash
# If not already in the Talisman directory
cd Talisman

# Run the setup script
./setup.sh
```

This script will:
1. Verify Docker installation
2. Create necessary directories
3. Set up environment configuration
4. Build Docker images
5. Start all services

### Step 3: Configure Environment

Edit the `.env` file to add your API keys:

```bash
nano .env
```

Important settings:
```bash
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
HIVE_MODE=enabled
MAX_WORKERS=4
```

### Step 4: Start Services

If using setup.sh, services are already started. Otherwise:

```bash
docker-compose up -d
```

### Step 5: Verify Installation

Check service status:
```bash
docker-compose ps
```

All services should show "Up" status.

View logs:
```bash
docker-compose logs -f agent-zero-coordinator
```

## Basic Usage

### Accessing the Coordinator

Interactive shell:
```bash
docker exec -it agentzero-coordinator /bin/bash
```

Run Agent Zero:
```bash
docker exec -it agentzero-coordinator python /workspace/agentzero/agent_zero.py
```

### Accessing NoxCore Console

Interactive shell:
```bash
docker exec -it noxcore-console /bin/bash
```

Start console:
```bash
docker exec -it noxcore-console python /workspace/noxcore/console/console.py
```

### Scaling Workers

Add more worker instances:
```bash
docker-compose up -d --scale agent-zero-worker-1=5
```

This creates 5 worker instances for parallel processing.

### Viewing Logs

All services:
```bash
docker-compose logs -f
```

Specific service:
```bash
docker-compose logs -f agent-zero-coordinator
docker-compose logs -f noxcore-console
```

## Common Operations

### Stop Services
```bash
docker-compose down
```

### Restart Services
```bash
docker-compose restart
```

### Rebuild After Changes
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Clean Everything
```bash
docker-compose down -v
docker system prune -a
```

## Testing the Hive

### Python Interactive Test

```bash
docker exec -it agentzero-coordinator python
```

In Python:
```python
from agentzero.hive.hive_manager import HiveManager, TaskPriority

# Create hive manager
hive = HiveManager()

# Register an agent
hive.register_agent('test-agent-1', ['coding', 'analysis'])

# Create a task
task = hive.create_task(
    'task-001',
    'Test task for the hive',
    TaskPriority.HIGH
)

# Check status
print(hive.get_hive_status())
```

## Next Steps

1. **Explore the Code**: Check out the implementation in `agentzero/` and `noxcore/`
2. **Add Custom Tools**: Create new tools in `agentzero/tools/`
3. **Configure NoxCore**: Adjust settings in `noxcore/config/noxcore.yml`
4. **Scale Up**: Add more workers for larger operations
5. **Integrate APIs**: Add your AI API keys for full functionality

## Troubleshooting

### Services Won't Start

Check Docker resources:
```bash
docker stats
```

View detailed logs:
```bash
docker-compose logs
```

### Port Conflicts

Edit `docker-compose.yml` to change ports:
```yaml
ports:
  - "8080:8000"  # Change 8080 to available port
```

### Permission Issues

Ensure current user has Docker permissions:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

## Advanced Configuration

### GPU Support

For GPU acceleration, add to `docker-compose.yml`:
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

### Custom Networks

Modify network configuration in `docker-compose.yml`:
```yaml
networks:
  agentzero-hive:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
```

## Support and Documentation

- Main README: `README.md`
- Configuration: `agentzero/config/agent.env`
- NoxCore Config: `noxcore/config/noxcore.yml`

## Philosophy

Agent Zero is designed with these principles:
- **AI-First**: Optimized for AI operations, not human interaction
- **Efficient**: Nanolevel optimization for resource usage
- **Distributed**: Hive architecture for scalable operations
- **Flexible**: Runs locally or connects to larger systems
- **Alpine-Based**: Following Alpine Linux philosophy

---

Happy building! 🚀 "To boldly build what no AI has ever built before"
