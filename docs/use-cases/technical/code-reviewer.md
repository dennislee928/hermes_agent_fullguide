# Code Reviewer

## Description
Code Reviewer analyzes source code files and returns structured feedback covering correctness, security issues, performance concerns, style violations, and maintainability. It gives developers senior-level code review comments without waiting for a teammate.

## Why Hermes
Hermes identifies non-obvious code issues — off-by-one errors, missing error handling, N+1 query patterns, insecure defaults — and explains the why behind each comment rather than just flagging a line number. Its output follows a consistent format that mirrors real code review culture.

## Quickstart
```bash
python examples/technical/code_tools.py review --file mycode.py
python examples/technical/code_tools.py review --code "def divide(a, b): return a/b"
```

## Sample Input
```python
def get_user_data(user_id):
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()
```

## Expected Output Format
```
Code Review — get_user_data()

CRITICAL
[Line 4] SQL Injection Vulnerability
  Using f-string interpolation in SQL queries allows an attacker to inject
  arbitrary SQL. If user_id = "1; DROP TABLE users;--" the query executes
  the DROP statement.
  Fix: Use parameterized queries:
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

HIGH
[Line 2] Database connection never closed
  The connection is opened but never closed or committed. Under load this
  will exhaust the connection pool.
  Fix: Use a context manager: `with psycopg2.connect(DB_URL) as conn:`

MEDIUM
[Line 3] SELECT * is fragile
  Selecting all columns couples the function to schema changes and fetches
  unnecessary data.
  Fix: Specify only the columns you need.

LOW
[Line 1] No type hints or docstring
  Fix: Add `def get_user_data(user_id: int) -> list[dict]:` and a docstring.

SUMMARY: 1 critical, 1 high, 1 medium, 1 low issue found.
```

## Tips
- Pass the full file with `--file` for context-aware reviews that catch cross-function issues.
- Use `--focus security` to get a security-only review, or `--focus performance` for perf.
- Add `--language python` explicitly if the language cannot be auto-detected.
- Combine with Refactorer: review first, then refactor based on feedback.
