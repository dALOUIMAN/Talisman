# NoxCore Agent Zero - Installation Notes

## Network Requirements

The Docker build process requires internet access to:
- Download Alpine Linux base image
- Install Python packages from PyPI
- Pull Redis image from Docker Hub

If you're in a restricted network environment:

### Option 1: Pre-built Images (Coming Soon)
Pre-built images will be available on Docker Hub:
```bash
docker pull noxcore/agent-zero:latest
```

### Option 2: Offline Build
1. Download dependencies on a connected machine
2. Create a local package repository
3. Configure Docker to use local mirrors

### Option 3: Simplified Dependencies
The current setup uses minimal dependencies to reduce build complexity:
- `aiohttp` - Async HTTP
- `websockets` - WebSocket support
- `redis` - Redis client
- `pydantic` - Data validation
- `python-dotenv` - Environment config
- `pyyaml` - YAML parsing

## Troubleshooting Build Issues

### Alpine Package Issues
If you see errors about Alpine packages:
```bash
# Use a different base image
# Edit Dockerfile, change FROM line to:
FROM python:3.11-slim
# Or
FROM python:3.11
```

### Python Package Installation
If pip fails:
```bash
# Build with verbose output
docker compose build --progress=plain

# Try without cache
docker compose build --no-cache
```

### Network Timeouts
If builds timeout:
```bash
# Increase timeout
export COMPOSE_HTTP_TIMEOUT=300
docker compose build
```

## Validated Environment

The Agent Zero setup has been validated to have:
- ✓ Correct file structure
- ✓ Valid Python syntax
- ✓ Valid YAML configuration
- ✓ Valid Docker Compose configuration

The actual Docker build and runtime testing requires:
1. Network access to Docker Hub and PyPI
2. Sufficient system resources (512MB+ RAM)
3. Docker daemon running

## Testing Without Docker

You can run the agents locally without Docker:

```bash
# Install dependencies
pip install -r requirements.txt

# Start Redis (using local installation or Docker)
redis-server

# In one terminal - start coordinator
export AGENT_TYPE=coordinator
export AGENT_ID=coordinator-1
export REDIS_HOST=localhost
python agent-zero-runner.py

# In another terminal - start worker
export AGENT_TYPE=worker
export AGENT_ID=worker-1
export REDIS_HOST=localhost
python agent-zero-runner.py
```

## Production Deployment

For production environments:

1. **Use Docker Swarm or Kubernetes**
   - Better orchestration
   - Auto-scaling
   - Health monitoring

2. **Redis Cluster**
   - High availability
   - Horizontal scaling
   - Data persistence

3. **Monitoring**
   - Prometheus metrics
   - Grafana dashboards
   - Log aggregation

4. **Security**
   - Redis authentication
   - Network isolation
   - TLS/SSL encryption

## Support

If you encounter issues:
1. Run `./validate-setup.sh` to check the setup
2. Check logs with `docker compose logs`
3. Review README.md and DEVELOPMENT.md
4. Open an issue on GitHub with details
