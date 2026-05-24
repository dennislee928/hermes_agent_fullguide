# Shell Script Generator

## Description
Shell Script Generator produces production-quality Bash scripts for any described automation task, including error handling, logging, argument parsing, and safety checks. It turns a plain English description of a workflow into a runnable, maintainable script.

## Why Hermes
Hermes writes shell scripts with proper defensive patterns — `set -euo pipefail`, input validation, trap-based cleanup, meaningful exit codes — that most ad-hoc scripts lack. It handles edge cases (missing arguments, file not found, permission errors) without being told to.

## Quickstart
```bash
python examples/technical/code_generation.py shell \
  --task "backup postgres db daily at 2am"
```

## Sample Input
```
Task: Create a deployment script that:
  1. Pulls latest code from main branch
  2. Runs tests, exits if any fail
  3. Builds Docker image with current git SHA as tag
  4. Pushes to ECR
  5. Updates the ECS task definition and deploys
  6. Sends a Slack notification on success or failure
```

## Expected Output Format
```bash
#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# deploy.sh — Production deployment script
# Usage: ./deploy.sh [--env production|staging]
# ============================================================

# --- Configuration ---
AWS_REGION="${AWS_REGION:-us-east-1}"
ECR_REPO="${ECR_REPO:?ECR_REPO env var is required}"
ECS_CLUSTER="${ECS_CLUSTER:?ECS_CLUSTER env var is required}"
ECS_SERVICE="${ECS_SERVICE:?ECS_SERVICE env var is required}"
SLACK_WEBHOOK="${SLACK_WEBHOOK:-}"
GIT_SHA=$(git rev-parse --short HEAD)
IMAGE_TAG="${ECR_REPO}:${GIT_SHA}"

# --- Logging ---
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }
err() { log "ERROR: $*" >&2; }

# --- Slack notification ---
notify_slack() {
    local status="$1" message="$2"
    [[ -z "$SLACK_WEBHOOK" ]] && return 0
    curl -s -X POST "$SLACK_WEBHOOK" \
        -H 'Content-type: application/json' \
        --data "{\"text\":\"Deploy ${status}: ${message} (${GIT_SHA})\"}"
}

# --- Cleanup on exit ---
trap 'notify_slack "FAILED" "Deployment failed at line $LINENO"' ERR

log "Starting deployment of ${GIT_SHA}"

# Step 1: Pull latest
log "Pulling latest from main..."
git fetch origin main
git checkout main
git pull origin main

# Step 2: Run tests
log "Running test suite..."
if ! python -m pytest tests/ -q; then
    err "Tests failed. Aborting deployment."
    exit 1
fi

# [Steps 3-6 continue...]

log "Deployment complete."
notify_slack "SUCCESS" "Deployed to ${ECS_SERVICE}"
```

## Tips
- Describe the task in natural language; include tools, environment, and requirements.
- Add `--safety strict` to always include rollback logic and dry-run mode.
- Use `--shell zsh` if your team uses zsh; default is bash.
- Always review generated scripts before running in production, especially those using `rm` or destructive operations.
