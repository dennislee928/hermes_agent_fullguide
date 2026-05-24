# Error Message Decoder

## Description
Error Message Decoder translates cryptic error messages, stack traces, and system errors into plain English explanations with step-by-step debugging guidance. It works across languages, frameworks, operating systems, and cloud platforms.

## Why Hermes
Hermes has deep knowledge of error taxonomies across the full software stack — from OS-level SIGSEGV to ORM-specific exceptions to cloud provider error codes — and provides root cause context plus ranked debugging steps rather than just rephrasing the error message.

## Quickstart
```bash
python examples/technical/debugging_tools.py decode-error \
  "SegmentationFault 11 in libssl"
python examples/technical/debugging_tools.py decode-error \
  --file stacktrace.txt
```

## Sample Input
```
Error:
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError)
FATAL: remaining connection slots are reserved for non-replication superuser connections

Context: FastAPI app deployed on Heroku, PostgreSQL on Heroku Postgres (Hobby plan)
```

## Expected Output Format
```
Error Decoded: PostgreSQL Connection Limit Exhausted

PLAIN ENGLISH
Your application is trying to open more database connections than PostgreSQL allows.
The database has hit its maximum connection limit, and the only remaining slots
are reserved for administrative superuser connections.

ROOT CAUSE
Heroku Postgres Hobby plan allows a maximum of 25 connections. Each gunicorn worker
or async thread creates its own SQLAlchemy connection pool. With default pool settings
(5 connections per pool) and multiple workers, you can exhaust this quickly.

WHY IT HAPPENS NOW
- Heroku scales dynos (workers) under load, each opening new connection pools
- Connection pools are not properly closed/reused on request end
- SQLAlchemy's default pool_size=5 was not tuned for a shared-plan database

DEBUGGING STEPS
1. Check current connections:
   SELECT count(*) FROM pg_stat_activity;

2. Check max_connections:
   SHOW max_connections;

3. If connections are not being released, look for missing session.close()
   or context manager misuse in your database session handling.

FIXES (ranked by impact)
1. Install PgBouncer (connection pooler) — handles 100s of app connections with
   a few actual DB connections. Best long-term fix.

2. Reduce SQLAlchemy pool_size:
   engine = create_engine(DB_URL, pool_size=2, max_overflow=3)

3. Use NullPool for serverless/request-scoped connections:
   engine = create_engine(DB_URL, poolclass=NullPool)

4. Upgrade Heroku Postgres plan (Standard-0 gives 120 connections).
```

## Tips
- Include your stack, framework, and hosting environment in the query for targeted advice.
- Paste the full stack trace, not just the last line — earlier frames often contain the real cause.
- Use `--language` to specify the language/runtime when it can't be inferred.
- For cloud errors (AWS, GCP, Azure), include the full error code (e.g., "AccessDeniedException", "ResourceNotFoundException").
