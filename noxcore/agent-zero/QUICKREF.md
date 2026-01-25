# NoxCore Agent Zero - Quick Reference

## Common Commands

### Start the Hive
```bash
cd noxcore/agent-zero
./start-hive.sh
```

Or manually:
```bash
docker compose up -d
```

### Stop the Hive
```bash
docker compose down
```

### View Logs
```bash
# All services
docker compose logs -f

# Coordinator only
docker compose logs -f coordinator

# Specific agent
docker compose logs -f agent-worker-1
```

### Check Status
```bash
docker compose ps
```

### Scale Workers
```bash
# Scale to 5 workers
docker compose up -d --scale agent-worker-1=5
```

### Restart Services
```bash
# Restart all
docker compose restart

# Restart specific service
docker compose restart coordinator
```

### Rebuild Images
```bash
docker compose build
docker compose up -d
```

### Clean Up
```bash
# Stop and remove containers
docker compose down

# Also remove volumes (data will be lost)
docker compose down -v

# Remove images
docker compose down --rmi all
```

## Monitoring

### Redis Connection
```bash
docker compose exec redis redis-cli ping
```

### Agent Status
```bash
docker compose exec coordinator python -c "import redis; r=redis.Redis(host='redis'); print(r.keys('agent:*'))"
```

### Resource Usage
```bash
docker stats
```

## Configuration

### Environment Variables

Edit `.env` file:
```bash
cp .env.example .env
nano .env
```

Key settings:
- `MAX_AGENTS` - Maximum agents in hive (default: 10)
- `LOG_LEVEL` - Logging verbosity (DEBUG/INFO/WARNING/ERROR)
- `REDIS_HOST` - Redis server hostname
- `REDIS_PORT` - Redis server port

### Agent Configuration

Edit `config/agent-config.yml` to customize:
- Hive settings
- Resource limits
- Communication protocols
- Performance tuning

## Troubleshooting

### Containers not starting
```bash
docker compose logs
```

### Redis connection issues
```bash
docker compose exec coordinator ping redis
```

### Port conflicts
Edit `docker-compose.yml` to change Redis port:
```yaml
ports:
  - "6380:6379"  # Changed from 6379
```

### Out of memory
Reduce `MAX_AGENTS` in `.env` or increase Docker memory limits.

## Development

### Adding Custom Agents

1. Create new agent file in `agents/`:
```python
from agents.base_agent import BaseAgent

class CustomAgent(BaseAgent):
    async def execute_task(self, task):
        # Your logic here
        pass
```

2. Update `agents/__init__.py`:
```python
from .custom_agent import CustomAgent
__all__ = ['BaseAgent', 'CustomAgent']
```

3. Rebuild:
```bash
docker compose build
docker compose up -d
```

### Testing Changes

1. Make your changes
2. Run validation:
```bash
./validate-setup.sh
```

3. Rebuild and test:
```bash
docker compose build
docker compose up -d
docker compose logs -f
```

## Integration

### External Services

Connect to Agent Zero from other applications:

**Redis PubSub:**
```python
import redis
r = redis.Redis(host='localhost', port=6379)

# Send task to specific agent
r.publish('agent:worker-1:tasks', json.dumps(task))

# Broadcast to all agents
r.publish('broadcast:tasks', json.dumps(task))

# Listen for results
pubsub = r.pubsub()
pubsub.subscribe('coordinator:results')
for message in pubsub.listen():
    print(message)
```

### API Integration (Future)

REST API endpoint (planned):
- `POST /api/tasks` - Submit new task
- `GET /api/status` - Get hive status
- `GET /api/agents` - List active agents
- `GET /api/tasks/:id` - Get task status

## Performance Tips

1. **Resource Optimization**
   - Start with 3 workers, scale as needed
   - Monitor with `docker stats`
   - Adjust `MAX_MEMORY_MB` in `.env`

2. **Network Optimization**
   - Use host network for low latency
   - Consider Redis cluster for large deployments

3. **Task Distribution**
   - Keep tasks small and focused
   - Use task priorities (future feature)
   - Monitor queue depth

## Security

1. **Network Isolation**
   - Use Docker networks
   - Restrict Redis access
   - Enable authentication (production)

2. **Resource Limits**
   - Set memory/CPU limits
   - Configure ulimits
   - Monitor resource usage

3. **Data Protection**
   - Backup `data/` directory
   - Use encrypted volumes (production)
   - Secure Redis with password

## Support

- Documentation: `README.md`
- Validation: `./validate-setup.sh`
- Issues: GitHub Issues
- Community: NoxCore Discord (if available)
