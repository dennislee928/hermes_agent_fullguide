# Technical & Dev Examples

Runnable Python scripts that use Hermes (via Ollama) to assist with 20 technical development tasks across code quality, code generation, database tooling, DevOps, and debugging.

## Prerequisites

**Ollama running locally with the Hermes model:**
```bash
ollama serve
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

**Python dependencies:**
```bash
pip install -r requirements.txt
```

## Scripts

### code_tools.py
Code review, bug explanation, refactoring, and complexity analysis.

```bash
# Review a Python file
python code_tools.py review --file mycode.py

# Security-focused review
python code_tools.py review --file api_handler.py --focus security

# Review inline code
python code_tools.py review --code "def get_user(id): return db.query(f'SELECT * FROM users WHERE id={id}')"

# Explain a bug with an error message
python code_tools.py explain-bug \
  --file buggy.py \
  --error "IndexError: list index out of range"

# Explain a bug with inline code
python code_tools.py explain-bug \
  --code "def process(items): return [items[i] for i in range(len(items)+1)]" \
  --error "IndexError: list index out of range"

# Refactor a file
python code_tools.py refactor \
  --file messy.py \
  --goal "add type hints and replace manual loops with list comprehensions"

# Refactor with a specific pattern
python code_tools.py refactor \
  --file nested_conditions.py \
  --goal "apply early return pattern to reduce nesting depth"

# Analyze code complexity
python code_tools.py complexity --file mymodule.py

# Custom complexity threshold
python code_tools.py complexity --file mymodule.py --threshold 3
```

**Focus options for review:** `all`, `security`, `performance`, `style`

---

### code_generation.py
Unit test generation, docstring writing, shell script generation, and Dockerfile creation.

```bash
# Generate unit tests (pytest)
python code_generation.py tests --file mymodule.py --framework pytest

# Unit tests with edge case focus
python code_generation.py tests \
  --file payment.py \
  --framework pytest \
  --coverage edge-cases \
  --mock-deps

# Generate docstrings (Google style)
python code_generation.py docstrings --file mymodule.py

# NumPy style docstrings with examples
python code_generation.py docstrings \
  --file data_utils.py \
  --style numpy \
  --include-examples

# Generate a shell script
python code_generation.py shell \
  --task "backup PostgreSQL database to S3 daily at 2am with 7-day retention"

# Shell script with strict safety (dry-run mode + rollback)
python code_generation.py shell \
  --task "deploy Docker image to ECS and update service" \
  --safety strict

# Generate a Dockerfile
python code_generation.py dockerfile \
  --stack "python fastapi redis" \
  --target production

# Dockerfile with docker-compose
python code_generation.py dockerfile \
  --stack "node express postgres" \
  --target development \
  --compose

# Production Dockerfile with secret injection guidance
python code_generation.py dockerfile \
  --stack "python django celery redis" \
  --target production \
  --secrets \
  --port 8000
```

---

### database_tools.py
SQL query building and database schema design.

```bash
# Build a SQL query (PostgreSQL by default)
python database_tools.py query "find all users who signed up last month and made a purchase"

# Query with schema file
python database_tools.py query \
  "top 10 customers by revenue in last 90 days with order count" \
  --schema schema.sql

# MySQL query with explanation
python database_tools.py query \
  "monthly active users by signup cohort for the last 6 months" \
  --db mysql \
  --explain

# Design a database schema
python database_tools.py schema "e-commerce app with products, orders, users, and product reviews"

# Schema with options
python database_tools.py schema \
  "multi-tenant SaaS project management app" \
  --db postgres \
  --soft-deletes \
  --uuid \
  --include-migrations

# Simple SQLite schema
python database_tools.py schema "blog with posts, comments, tags, and authors" --db sqlite
```

**Supported databases:** `postgres`, `mysql`, `sqlite`, `mssql`, `bigquery` (query only), `snowflake` (query only)

---

### devops_tools.py
Git commit messages, CI/CD pipeline generation, architecture advice, and dependency analysis.

```bash
# Generate a commit message from staged changes
git diff --staged | python devops_tools.py commit-message

# From a diff file
python devops_tools.py commit-message --diff changes.diff

# With type and scope override
git diff --staged | python devops_tools.py commit-message --type fix --scope auth

# Design a GitHub Actions CI/CD pipeline
python devops_tools.py cicd-advisor \
  --stack "python fastapi pytest docker deploy-to-ecs" \
  --platform github-actions \
  --envs "staging,production"

# GitLab CI pipeline with security focus
python devops_tools.py cicd-advisor \
  --stack "node typescript jest docker kubernetes" \
  --platform gitlab-ci \
  --envs "dev,staging,production" \
  --security-focused

# Architecture review
python devops_tools.py architecture-advisor \
  --description "Monolithic Django app, single PostgreSQL instance, 100k users, 4.2s p99 response time" \
  --goal "improve performance to under 500ms p99" \
  --team "4 engineers" \
  --scale "100k users, ~500 concurrent peak"

# Greenfield architecture
python devops_tools.py architecture-advisor \
  --description "Building a real-time collaborative document editor" \
  --goal "scalable from day 1, small team" \
  --mode greenfield

# Analyze Python dependencies
python devops_tools.py analyze-deps --file requirements.txt --ecosystem python

# Node dependencies with license check
python devops_tools.py analyze-deps \
  --file package.json \
  --ecosystem node \
  --licenses commercial
```

---

### debugging_tools.py
Regex generation, log analysis, error decoding, security scanning, and API documentation.

```bash
# Generate a regex pattern
python debugging_tools.py regex "match email addresses"
python debugging_tools.py regex "extract IPv4 addresses from text"
python debugging_tools.py regex "US phone number in any common format"

# Regex for a specific language
python debugging_tools.py regex "match ISO 8601 datetime strings" --language javascript

# Anchored regex (full string match)
python debugging_tools.py regex "valid hexadecimal color code" --anchored

# Analyze a log file
python debugging_tools.py analyze-log --file app.log

# Last 200 lines, errors only
python debugging_tools.py analyze-log --file production.log --last 200 --level error

# Decode an error message
python debugging_tools.py decode-error "OperationalError: FATAL: remaining connection slots reserved for superuser"

# Decode from a stack trace file
python debugging_tools.py decode-error --file stacktrace.txt

# Decode with context
python debugging_tools.py decode-error \
  "AttributeError: 'NoneType' object has no attribute 'id'" \
  --context "Happens in the payment webhook handler after a refund" \
  --language python

# Security scan
python debugging_tools.py scan-security --file mycode.py

# OWASP Top 10 focused scan
python debugging_tools.py scan-security --file api_routes.py --focus owasp-top10

# Generate API docs (Markdown)
python debugging_tools.py api-docs --file routes/users.py --format markdown

# Generate OpenAPI YAML
python debugging_tools.py api-docs \
  --file routes/orders.py \
  --format openapi \
  --base-url "https://api.myapp.com/v1"
```

---

## Tips

- All scripts stream output in real-time.
- Use `--help` for full options:
  ```bash
  python code_tools.py --help
  python code_tools.py review --help
  ```
- **For code input**: most tools accept `--file` (reads the whole file) or `--code` (inline snippet). Files give better context.
- **Piping**: `commit-message` and `analyze-log` accept stdin for easy shell integration.
- **Combine tools**: Review first, then refactor based on findings. Generate tests before refactoring to confirm behavior is preserved.

## Common Workflows

**Before submitting a PR:**
```bash
python code_tools.py review --file src/feature.py --focus security
python code_generation.py tests --file src/feature.py --framework pytest
git diff --staged | python devops_tools.py commit-message
```

**Debugging a production incident:**
```bash
python debugging_tools.py analyze-log --file production.log --last 500 --level error
python debugging_tools.py decode-error --file stacktrace.txt --context "payment service, AWS Lambda"
```

**Setting up a new service:**
```bash
python code_generation.py dockerfile --stack "python fastapi postgres redis" --target production --compose
python devops_tools.py cicd-advisor --stack "python fastapi docker" --platform github-actions
python database_tools.py schema "user accounts, sessions, subscription plans" --uuid --soft-deletes
```

## Troubleshooting

**"Cannot connect to Ollama"**: Run `ollama serve` in a separate terminal.

**Model not found**: Pull the model with `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`

**Slow responses**: The 8B model runs on CPU if no GPU is available. First response may take 30-60 seconds.

**Large files**: For very large source files, consider passing specific functions rather than the whole file for faster, more focused results.
