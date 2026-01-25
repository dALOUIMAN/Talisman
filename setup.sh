#!/bin/bash
# Agent Zero Setup Script
# Quick setup for the Agent Zero AI development environment

set -e

echo "================================================"
echo "   Agent Zero - AI Development Environment"
echo "   Setup Script"
echo "================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"

if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed${NC}"
    echo "Please install Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}Error: Docker Compose is not installed${NC}"
    echo "Please install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

echo -e "${GREEN}✓ Docker found: $(docker --version)${NC}"
echo -e "${GREEN}✓ Docker Compose found: $(docker-compose --version)${NC}"
echo ""

# Create necessary directories
echo -e "${YELLOW}Creating directory structure...${NC}"
mkdir -p agentzero/agents agentzero/tools agentzero/hive agentzero/config
mkdir -p noxcore/console noxcore/protocols noxcore/config
mkdir -p data logs

echo -e "${GREEN}✓ Directories created${NC}"
echo ""

# Setup environment file
if [ ! -f .env ]; then
    echo -e "${YELLOW}Creating .env file...${NC}"
    if [ -f agentzero/config/agent.env ]; then
        cp agentzero/config/agent.env .env
        echo -e "${GREEN}✓ .env file created${NC}"
        echo -e "${YELLOW}Please edit .env and add your API keys${NC}"
    else
        echo -e "${RED}Warning: Template file agentzero/config/agent.env not found${NC}"
        echo -e "${YELLOW}Please create .env manually${NC}"
    fi
else
    echo -e "${GREEN}✓ .env file already exists${NC}"
fi
echo ""

# Build Docker images
echo -e "${YELLOW}Building Docker images...${NC}"
docker-compose build

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Docker images built successfully${NC}"
else
    echo -e "${RED}✗ Failed to build Docker images${NC}"
    exit 1
fi
echo ""

# Start services
echo -e "${YELLOW}Starting Agent Zero services...${NC}"
docker-compose up -d

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Services started successfully${NC}"
else
    echo -e "${RED}✗ Failed to start services${NC}"
    exit 1
fi
echo ""

# Wait for services to be ready
echo -e "${YELLOW}Waiting for services to initialize...${NC}"
sleep 5

# Check service status
echo -e "${YELLOW}Service status:${NC}"
docker-compose ps
echo ""

# Display access information
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}   Agent Zero is ready!${NC}"
echo -e "${GREEN}================================================${NC}"
echo ""
echo -e "Access points:"
echo -e "  - Coordinator API:  http://localhost:8000"
echo -e "  - WebSocket:        ws://localhost:8001"
echo -e "  - NoxCore Console:  http://localhost:3000"
echo ""
echo -e "Useful commands:"
echo -e "  - View logs:        docker-compose logs -f"
echo -e "  - Stop services:    docker-compose down"
echo -e "  - Restart:          docker-compose restart"
echo -e "  - Console access:   docker exec -it agentzero-coordinator /bin/bash"
echo ""
echo -e "${GREEN}Happy AI development! 🚀${NC}"
