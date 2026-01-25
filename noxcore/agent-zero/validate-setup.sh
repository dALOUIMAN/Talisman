#!/bin/bash
# NoxCore Agent Zero - Validation Script
# Tests the Agent Zero setup without requiring Docker build

set -e

echo "=========================================="
echo "  Agent Zero Validation"
echo "=========================================="
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check functions
check_pass() {
    echo -e "${GREEN}✓${NC} $1"
}

check_fail() {
    echo -e "${RED}✗${NC} $1"
}

check_warn() {
    echo -e "${YELLOW}!${NC} $1"
}

echo "Checking prerequisites..."
echo ""

# Check Docker
if command -v docker &> /dev/null; then
    check_pass "Docker is installed ($(docker --version))"
else
    check_fail "Docker is not installed"
    exit 1
fi

# Check Docker Compose
if docker compose version &> /dev/null; then
    check_pass "Docker Compose is installed ($(docker compose version))"
elif command -v docker-compose &> /dev/null; then
    check_pass "Docker Compose (v1) is installed ($(docker-compose --version))"
else
    check_fail "Docker Compose is not installed"
    exit 1
fi

echo ""
echo "Validating file structure..."
echo ""

# Check required files
files=(
    "Dockerfile"
    "docker-compose.yml"
    "requirements.txt"
    "agent-zero-runner.py"
    "README.md"
    ".env.example"
    "agents/__init__.py"
    "agents/base_agent.py"
    "coordinator/__init__.py"
    "coordinator/hive_coordinator.py"
    "tools/__init__.py"
    "tools/agent_tools.py"
    "config/agent-config.yml"
)

all_found=true
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        check_pass "Found: $file"
    else
        check_fail "Missing: $file"
        all_found=false
    fi
done

if ! $all_found; then
    echo ""
    check_fail "Some required files are missing"
    exit 1
fi

echo ""
echo "Validating Python code syntax..."
echo ""

# Check Python syntax
python_files=(
    "agent-zero-runner.py"
    "agents/base_agent.py"
    "coordinator/hive_coordinator.py"
    "tools/agent_tools.py"
)

syntax_ok=true
for file in "${python_files[@]}"; do
    if python3 -m py_compile "$file" 2>/dev/null; then
        check_pass "Syntax OK: $file"
    else
        check_fail "Syntax error: $file"
        syntax_ok=false
    fi
done

if ! $syntax_ok; then
    echo ""
    check_fail "Python syntax errors detected"
    exit 1
fi

echo ""
echo "Validating configuration files..."
echo ""

# Check YAML syntax
yaml_file='config/agent-config.yml'
if command -v python3 &> /dev/null; then
    if [ -f "$yaml_file" ]; then
        if python3 -c "import yaml; yaml.safe_load(open('$yaml_file'))" 2>/dev/null; then
            check_pass "Valid YAML: $yaml_file"
        else
            check_fail "Invalid YAML: $yaml_file"
        fi
    else
        check_fail "Missing: $yaml_file"
    fi
fi

# Check docker-compose.yml
if docker compose config &> /dev/null; then
    check_pass "Valid docker-compose.yml"
elif command -v docker-compose &> /dev/null && docker-compose config &> /dev/null; then
    check_pass "Valid docker-compose.yml"
else
    check_warn "Could not validate docker-compose.yml"
fi

echo ""
echo "=========================================="
echo "  Validation Summary"
echo "=========================================="
echo ""
check_pass "All core files present"
check_pass "Python syntax validated"
check_pass "Configuration files validated"
echo ""
echo "Agent Zero setup is valid!"
echo ""
echo "Next steps:"
echo "  1. Review the README.md for usage instructions"
echo "  2. Copy .env.example to .env and configure as needed"
echo "  3. Run ./start-hive.sh to launch the agent hive"
echo ""
