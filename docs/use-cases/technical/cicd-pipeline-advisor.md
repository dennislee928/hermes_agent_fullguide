# CI/CD Pipeline Advisor

## Description
CI/CD Pipeline Advisor reviews your current deployment workflow and generates an optimized pipeline configuration with best practices for testing, security scanning, caching, environment promotion, and rollback strategies. It supports GitHub Actions, GitLab CI, CircleCI, and Jenkins.

## Why Hermes
Hermes understands the tradeoffs in CI/CD design — parallelism vs. cost, fast feedback vs. thorough coverage, trunk-based vs. branch-based deployment — and generates pipeline YAML that reflects your specific stack and team maturity rather than a generic template.

## Quickstart
```bash
python examples/technical/devops_tools.py cicd-advisor \
  --stack "python fastapi, pytest, docker, deploy to ECS" \
  --platform github-actions \
  --envs "staging, production"
```

## Sample Input
```
Current state:
  - Manual deploys by running `./deploy.sh` locally
  - Tests run manually before deploy (sometimes skipped)
  - Docker image built and pushed to ECR manually
  - No staging environment
  - No rollback process

Stack: FastAPI, pytest, Docker, AWS ECS
Platform: GitHub Actions
Goals: Automate everything, add staging, prevent broken deploys
```

## Expected Output Format
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    name: Test & Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements*.txt') }}
      - run: pip install -r requirements-dev.txt
      - run: ruff check .
      - run: pytest tests/ -v --tb=short

  security-scan:
    name: Security Scan
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - run: pip install bandit safety
      - run: bandit -r app/
      - run: safety check

  build-and-push:
    name: Build & Push Docker Image
    runs-on: ubuntu-latest
    needs: [test, security-scan]
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker build -t $ECR_REGISTRY/myapp:${{ github.sha }} .
          docker push $ECR_REGISTRY/myapp:${{ github.sha }}

  deploy-staging:
    name: Deploy to Staging
    needs: build-and-push
    # [ECS update-service steps...]

  deploy-production:
    name: Deploy to Production
    needs: deploy-staging
    environment: production  # requires manual approval
    # [ECS update-service steps with canary rollout...]
```

Recommendations:
1. Store ECR URL and cluster names in GitHub Secrets, not hardcoded.
2. Add a smoke test job after staging deploy before promoting to production.
3. Implement a rollback job triggered manually or on health check failure.

## Tips
- Describe your current state honestly — even "no CI" is a valid starting point.
- Specify `--platform` to get directly usable YAML syntax for your CI system.
- Add `--cost-optimize` to get advice on reducing CI compute costs (parallelism, caching).
- Use `--security-focused` to include SBOM generation, SLSA provenance, and secret scanning.
