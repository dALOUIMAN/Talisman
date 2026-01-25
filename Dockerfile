# Agent Zero AI Development Environment
# Based on Alpine Linux for lightweight, efficient operation
FROM python:3.11-alpine

LABEL maintainer="NoxCore AI Team"
LABEL description="Agent Zero - AI-focused development environment"

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apk add --no-cache \
    git \
    bash \
    curl \
    wget \
    gcc \
    g++ \
    make \
    cmake \
    linux-headers \
    musl-dev \
    libffi-dev \
    openssl-dev \
    nodejs \
    npm \
    vim \
    nano \
    tmux \
    htop

# Install Python AI/ML dependencies
RUN pip install --no-cache-dir \
    numpy \
    torch --index-url https://download.pytorch.org/whl/cpu \
    transformers \
    langchain \
    openai \
    anthropic \
    requests \
    aiohttp \
    websockets \
    pyyaml \
    python-dotenv

# Create directories for Agent Zero structure
RUN mkdir -p /workspace/agents \
    /workspace/tools \
    /workspace/hive \
    /workspace/noxcore \
    /workspace/logs \
    /workspace/config

# Copy Agent Zero configuration
COPY agentzero/ /workspace/
COPY noxcore/ /workspace/noxcore/

# Set up environment variables
ENV AGENT_ZERO_HOME=/workspace
ENV NOXCORE_HOME=/workspace/noxcore
ENV PYTHONPATH=/workspace:$PYTHONPATH
ENV PATH=/workspace/tools:$PATH

# Create non-root user for security
RUN adduser -D -h /workspace agentzero && \
    chown -R agentzero:agentzero /workspace

USER agentzero

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Default command
CMD ["/bin/bash"]
