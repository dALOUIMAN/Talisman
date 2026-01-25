# Makefile for Agent Zero AI Development Environment
# Convenience commands for common operations

.PHONY: help setup build up down restart logs clean status shell test

# Default target
help:
	@echo "Agent Zero - AI Development Environment"
	@echo "========================================"
	@echo ""
	@echo "Available commands:"
	@echo "  make setup      - Initial setup (build and start)"
	@echo "  make build      - Build Docker images"
	@echo "  make up         - Start all services"
	@echo "  make down       - Stop all services"
	@echo "  make restart    - Restart all services"
	@echo "  make logs       - View logs (all services)"
	@echo "  make status     - Check service status"
	@echo "  make shell      - Access coordinator shell"
	@echo "  make console    - Access NoxCore console shell"
	@echo "  make test       - Run basic tests"
	@echo "  make clean      - Clean up containers and volumes"
	@echo "  make scale N=5  - Scale workers (N=number of workers)"
	@echo ""

# Initial setup
setup:
	@echo "Setting up Agent Zero environment..."
	@./setup.sh

# Build images
build:
	@echo "Building Docker images..."
	@docker-compose build

# Start services
up:
	@echo "Starting services..."
	@docker-compose up -d
	@echo "Services started!"
	@make status

# Stop services
down:
	@echo "Stopping services..."
	@docker-compose down

# Restart services
restart:
	@echo "Restarting services..."
	@docker-compose restart
	@make status

# View logs
logs:
	@docker-compose logs -f

# View coordinator logs
logs-coordinator:
	@docker-compose logs -f agent-zero-coordinator

# View console logs
logs-console:
	@docker-compose logs -f noxcore-console

# Check status
status:
	@echo "Service Status:"
	@docker-compose ps

# Access coordinator shell
shell:
	@docker exec -it agentzero-coordinator /bin/bash

# Access NoxCore console shell
console:
	@docker exec -it noxcore-console /bin/bash

# Access worker shell
shell-worker:
	@docker exec -it agentzero-worker-1 /bin/bash

# Run Agent Zero
run-agent:
	@docker exec -it agentzero-coordinator python /workspace/agentzero/agent_zero.py

# Run NoxCore console
run-console:
	@docker exec -it noxcore-console python /workspace/noxcore/console/console.py

# Scale workers
scale:
	@echo "Scaling workers to $(N) instances..."
	@docker-compose up -d --scale agent-zero-worker-1=$(N)

# Run tests
test:
	@echo "Running basic tests..."
	@docker exec agentzero-coordinator python -c "from agentzero.hive.hive_manager import HiveManager; hm = HiveManager(); print('Hive Manager OK')"
	@docker exec agentzero-coordinator python -c "from agentzero.tools.agent_tools import get_tool; print('Tools OK')"
	@echo "Tests completed!"

# Clean up
clean:
	@echo "Cleaning up..."
	@docker-compose down -v
	@echo "Cleanup complete!"

# Full rebuild
rebuild:
	@echo "Full rebuild..."
	@make down
	@docker-compose build --no-cache
	@make up

# Show Docker stats
stats:
	@docker stats

# Show hive status (if running)
hive-status:
	@docker exec agentzero-coordinator python -c "from agentzero.hive.hive_manager import HiveManager; hm = HiveManager(); import json; print(json.dumps(hm.get_hive_status(), indent=2))"
