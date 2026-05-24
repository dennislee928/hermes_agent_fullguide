# Dockerfile Generator

## Description
Dockerfile Generator creates optimized, production-ready Dockerfiles and optional docker-compose configurations for any application stack. It applies layer caching best practices, multi-stage builds, and security hardening automatically.

## Why Hermes
Hermes generates Dockerfiles that follow production best practices by default — non-root users, minimal base images, build cache optimization via dependency installation ordering, and `.dockerignore` recommendations — rather than producing naive single-stage examples.

## Quickstart
```bash
python examples/technical/code_generation.py dockerfile \
  --stack "python fastapi redis" \
  --target production
```

## Sample Input
```
Stack: Node.js 20, Express API, connects to PostgreSQL
Purpose: Production API server
Requirements: Should be small, run as non-root, handle graceful shutdown
Environment: Deployed to Kubernetes
```

## Expected Output Format
```dockerfile
# ============================================================
# Multi-stage build: Node.js Express API
# ============================================================

# --- Stage 1: Dependencies ---
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --only=production && npm cache clean --force

# --- Stage 2: Build (if TypeScript) ---
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# --- Stage 3: Production ---
FROM node:20-alpine AS production
WORKDIR /app

# Security: run as non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Copy only what's needed
COPY --from=deps /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package.json ./

EXPOSE 3000

# Graceful shutdown support
STOPSIGNAL SIGTERM
CMD ["node", "dist/index.js"]
```

Recommended .dockerignore:
```
node_modules
.git
*.log
.env
dist
coverage
```

Notes:
- Alpine base keeps image ~50MB vs ~400MB for full node image.
- Multi-stage keeps secrets and dev dependencies out of final image.
- STOPSIGNAL SIGTERM enables Kubernetes pod graceful shutdown with preStop hooks.

## Tips
- Use `--target development` for a dev Dockerfile with hot-reload and dev dependencies.
- Specify `--compose` to also generate a docker-compose.yml for local development.
- Add `--secrets` to get guidance on injecting environment secrets at runtime (not baked in).
- For monorepos, provide `--context path/to/service` to generate service-specific Dockerfiles.
