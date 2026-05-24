# Log Analyzer

## Description
Log Analyzer processes application log files to surface errors, anomalies, frequency patterns, and potential root causes. It turns hundreds of raw log lines into a prioritized incident summary with actionable insights.

## Why Hermes
Hermes identifies meaningful patterns in log noise — correlating repeated error types, noting timing clusters that suggest cascading failures, and distinguishing expected warnings from unusual error signatures — without being given pre-configured rules.

## Quickstart
```bash
python examples/technical/debugging_tools.py analyze-log \
  --file app.log \
  --last 100
```

## Sample Input
```
[2024-10-15 14:22:01] INFO  Request GET /api/users 200 45ms
[2024-10-15 14:22:03] ERROR DB connection timeout after 5000ms (attempt 1/3)
[2024-10-15 14:22:08] ERROR DB connection timeout after 5000ms (attempt 2/3)
[2024-10-15 14:22:13] ERROR DB connection timeout after 5000ms (attempt 3/3)
[2024-10-15 14:22:13] ERROR Failed to process request: DB unavailable
[2024-10-15 14:22:14] ERROR Failed to process request: DB unavailable
[2024-10-15 14:22:15] WARN  Circuit breaker OPEN for database connections
[2024-10-15 14:22:16] ERROR 503 returned to client: service unavailable
[2024-10-15 14:22:17] ERROR 503 returned to client: service unavailable
...
[2024-10-15 14:25:01] INFO  DB connection restored
[2024-10-15 14:25:02] INFO  Circuit breaker CLOSED
```

## Expected Output Format
```
Log Analysis — app.log (last 100 lines)

INCIDENT SUMMARY
  Severity: HIGH
  Duration: 14:22:03 – 14:25:01 (approx. 3 minutes)
  Impact: Service returned 503 errors to clients during the window.

ROOT CAUSE HYPOTHESIS
  Primary: Database connection timeout starting at 14:22:03.
  The retry mechanism exhausted 3 attempts (15 seconds), then the circuit
  breaker opened at 14:22:15, causing all subsequent requests to fail fast
  with 503. The DB recovered at 14:25:01 and the circuit breaker closed.

ERROR FREQUENCY
  | Error Type                  | Count | First Seen  |
  |-----------------------------|-------|-------------|
  | DB connection timeout       |   3   | 14:22:03    |
  | Failed to process request   |   2   | 14:22:13    |
  | 503 returned to client      |  14   | 14:22:16    |

INVESTIGATION LEADS
  1. Why did the DB become unavailable at 14:22:03? Check DB server logs.
  2. Was this a network blip or a DB overload? Check DB CPU/connection metrics.
  3. 14 clients received 503 in 3 minutes — were retries implemented client-side?

NORMAL ACTIVITY
  - GET /api/users 200 responses observed before and after incident — service healthy.
```

## Tips
- Use `--last N` to analyze only the most recent N lines for performance.
- Use `--level error` to filter to only error/warning lines before analysis.
- For multi-service logs, combine files: `--file service1.log --file service2.log`.
- Works with common formats: JSON logs, Apache/Nginx access logs, application logs.
