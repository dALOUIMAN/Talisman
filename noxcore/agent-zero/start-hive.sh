#!/bin/bash
# NoxCore Agent Zero - Quick Start Script
# Launches the Agent Zero hive environment

set -e

echo "=========================================="
echo "  NoxCore Agent Zero - AI Environment"
echo "=========================================="
echo ""

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed"
    echo "Please install Docker first: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check for Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "Error: Docker Compose is not installed"
    echo "Please install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# Navigate to agent-zero directory
cd "$(dirname "$0")"

echo "Starting Agent Zero Hive..."
echo ""

# Build and start containers
docker-compose up -d --build

echo ""
echo "Agent Zero Hive is starting up!"
echo ""
echo "Services:"
echo "  - Redis:       localhost:6379"
echo "  - Coordinator: noxcore-coordinator"
echo "  - Workers:     noxcore-agent-1, noxcore-agent-2, noxcore-agent-3"
echo ""
echo "Useful commands:"
echo "  View logs:     docker-compose logs -f"
echo "  Check status:  docker-compose ps"
echo "  Stop hive:     docker-compose down"
echo ""
echo "Monitor coordinator:"
echo "  docker-compose logs -f coordinator"
echo ""

# Wait a moment for services to start
sleep 5

# Show status
echo "Current status:"
docker-compose ps

echo ""
echo "=========================================="
echo "Agent Zero Hive is ready!"
echo "=========================================="
