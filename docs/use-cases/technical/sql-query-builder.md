# SQL Query Builder

## Description
SQL Query Builder translates natural language questions into correct, optimized SQL queries for a given schema. It handles joins, subqueries, window functions, aggregations, and CTEs from plain English descriptions without requiring the user to know SQL syntax.

## Why Hermes
Hermes accurately maps natural language intent to SQL semantics — correctly distinguishing "users who made a purchase last month" (filter on purchase date) from "users who signed up last month" (filter on signup date) — and generates queries that follow performance best practices by default.

## Quickstart
```bash
python examples/technical/database_tools.py query \
  "find all users who signed up last month and made a purchase"
```

## Sample Input
```
Schema:
  users(id, email, created_at, plan_type)
  orders(id, user_id, amount, status, created_at)
  order_items(id, order_id, product_id, quantity, unit_price)

Question: Show me the top 10 users by total spend in the last 90 days,
          including their email, plan type, and number of orders.
```

## Expected Output Format
```sql
-- Top 10 users by total spend in the last 90 days
SELECT
    u.email,
    u.plan_type,
    COUNT(DISTINCT o.id)        AS order_count,
    SUM(o.amount)               AS total_spend
FROM users u
JOIN orders o
    ON o.user_id = u.id
WHERE o.status    = 'completed'
  AND o.created_at >= NOW() - INTERVAL '90 days'
GROUP BY
    u.id,
    u.email,
    u.plan_type
ORDER BY total_spend DESC
LIMIT 10;
```

Notes:
- Filters on `status = 'completed'` to exclude refunded/cancelled orders.
  If you want all orders regardless of status, remove the WHERE clause condition.
- `NOW() - INTERVAL '90 days'` is PostgreSQL syntax.
  For MySQL use: `DATE_SUB(NOW(), INTERVAL 90 DAY)`
- Add an index on `orders(user_id, created_at, status)` for this query to perform well at scale.

## Tips
- Always provide your schema with `--schema schema.sql` or inline it in the question.
- Mention the database engine (`--db postgres`, `--db mysql`, `--db sqlite`) for dialect-correct syntax.
- Ask for CTEs explicitly if you want readable multi-step queries: "write this as a CTE".
- Use `--explain` to get a plain-English explanation of what each clause does.
