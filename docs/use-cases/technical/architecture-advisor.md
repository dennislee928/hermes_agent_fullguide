# Architecture Advisor

## Description
Architecture Advisor evaluates your system's current architecture and produces recommendations for scalability, reliability, security, and maintainability. It helps teams make informed technical decisions before investing in large-scale changes.

## Why Hermes
Hermes reasons about architectural tradeoffs in context — your team size, scale requirements, budget, and existing stack — rather than recommending the most complex solution by default. It explains the "why" behind each recommendation and flags common over-engineering traps.

## Quickstart
```bash
python examples/technical/devops_tools.py architecture-advisor \
  --description "monolith rails app, 50k users, single postgres db, struggling with perf" \
  --goal "improve scalability without full rewrite"
```

## Sample Input
```
Current architecture:
  - Monolithic Django app (1 repo, 150k LOC)
  - Single PostgreSQL database (500GB, no read replicas)
  - Deployed on 1 large EC2 instance (c5.4xlarge)
  - File uploads stored on EC2 local disk
  - Cron jobs run on same instance as web server
  - 100k users, 500 concurrent during peak
  - p99 response time: 4.2 seconds (target: < 500ms)

Goal: Improve performance and reliability without a full rewrite
Team: 4 engineers, 6 months runway
```

## Expected Output Format
```
Architecture Advisory — Django Monolith Performance & Reliability

CURRENT STATE ASSESSMENT
Risk Level: HIGH
Critical Issues:
1. Single point of failure: 1 EC2 instance — any hardware failure = total downtime
2. Local file storage: data loss risk if instance is terminated
3. Background jobs competing with web requests for CPU/memory
4. No read replicas: all 500 concurrent users hitting one DB for reads and writes

RECOMMENDED IMPROVEMENTS (Prioritized by Impact/Effort)

Priority 1 — Quick Wins (1-4 weeks, high impact)
  a) Add PostgreSQL read replica
     - Route read-heavy queries to replica via Django's DATABASE_ROUTERS
     - Expected: 40-60% reduction in primary DB load
     - Effort: Low (RDS Console + ~1 day code change)

  b) Move file uploads to S3
     - Replace local disk with django-storages + S3
     - Eliminates data loss risk immediately
     - Enables CDN in future
     - Effort: 2-3 days

  c) Separate background jobs to dedicated worker instance
     - Move celery workers to separate EC2 or use AWS SQS + Lambda
     - Frees web server resources, improves p99 latency significantly
     - Effort: 3-5 days if Celery already in use

Priority 2 — Reliability (1-2 months)
  a) Put app behind a load balancer (ALB) with 2+ instances
  b) Add Redis caching for expensive query results
  c) Implement application-level performance profiling (py-spy, Django Debug Toolbar)

Priority 3 — Scale (2-6 months, consider only if needed)
  a) Extract high-traffic read endpoints to a lightweight FastAPI service
     (only if traffic continues to grow)
  b) Evaluate Aurora PostgreSQL for auto-scaling read capacity

WHAT NOT TO DO
- Do not migrate to microservices with a 4-person team and 6-month runway.
  Monolith optimizations above will get you to < 500ms p99 at far lower cost.
- Do not add Kubernetes yet — operational overhead will slow you down.

ESTIMATED IMPACT
After Priority 1 changes: p99 likely drops to 800ms-1.2s
After Priority 2 changes: p99 likely drops to 300-500ms (target met)
```

## Tips
- Be specific about scale numbers (users, RPS, data size) for accurate recommendations.
- Include team size and runway constraints — good architecture is contextual, not universal.
- Use `--goal reliability` or `--goal cost-reduction` or `--goal scalability` to focus advice.
- For greenfield projects, use `--mode greenfield` to get starting architecture recommendations.
