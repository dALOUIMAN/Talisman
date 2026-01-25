# Agent Zero AI Environment - Alpine Linux Base
# Lightweight AI-focused container for distributed agent system

FROM python:3.11-alpine

LABEL maintainer="NoxCore Team"
LABEL description="Agent Zero AI Environment - Ultra-lightweight distributed AI agent system"

# Install system dependencies - minimal footprint
RUN apk add --no-cache \
    bash \
    git \
    curl \
    build-base \
    libffi-dev \
    openssl-dev \
    && rm -rf /var/cache/apk/*

# Set working directory
WORKDIR /agent-zero

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY agents/ ./agents/
COPY config/ ./config/
COPY tools/ ./tools/
COPY coordinator/ ./coordinator/
COPY agent-zero-runner.py .

# Create volume for persistent data
VOLUME ["/agent-zero/data"]

# Environment variables
ENV AGENT_MODE=local \
    AGENT_HIVE=enabled \
    COORDINATOR_ENABLED=true \
    LOG_LEVEL=INFO

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Run the agent
CMD ["python", "agent-zero-runner.py"]
