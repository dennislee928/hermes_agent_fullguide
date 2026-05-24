#!/usr/bin/env python3
"""
database_tools.py — SQL query building and database schema design using Hermes

Usage:
  python database_tools.py query "find all users who signed up last month and made a purchase"
  python database_tools.py query "top 10 products by revenue last 90 days" --schema schema.sql
  python database_tools.py query "monthly active users by cohort" --db mysql
  python database_tools.py schema "e-commerce app with products, orders, users, reviews"
  python database_tools.py schema "project management SaaS" --db postgres --include-migrations
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"


def stream_chat(system_prompt: str, user_message: str) -> None:
    """Send a chat request to Ollama and stream the response to stdout."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "stream": True,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=180)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print(
            "Error: Cannot connect to Ollama at http://localhost:11434.\n"
            "Make sure Ollama is running: `ollama serve`",
            file=sys.stderr,
        )
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"Error: Ollama returned HTTP {e.response.status_code}", file=sys.stderr)
        sys.exit(1)

    for line in response.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = data.get("message", {}).get("content", "")
        if content:
            print(content, end="", flush=True)
        if data.get("done"):
            print()
            break


def read_file(path: str) -> str:
    """Read a file and return its content."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Error reading file '{path}': {e}", file=sys.stderr)
        sys.exit(1)


def cmd_query(args: argparse.Namespace) -> None:
    """Build a SQL query from a natural language description."""
    db_dialects = {
        "postgres": "PostgreSQL 15",
        "mysql": "MySQL 8.0",
        "sqlite": "SQLite 3",
        "mssql": "SQL Server (T-SQL)",
        "bigquery": "Google BigQuery (standard SQL)",
        "snowflake": "Snowflake SQL",
    }

    db_label = db_dialects.get(args.db.lower(), args.db)

    system_prompt = (
        f"You are a senior database engineer and SQL expert specializing in {db_label}. "
        "Translate natural language questions into correct, optimized SQL queries. "
        "Always: "
        "1. Write clean, readable SQL with proper formatting and alignment "
        "2. Add a comment explaining what the query does "
        "3. Use CTEs instead of nested subqueries for readability when appropriate "
        "4. Use explicit JOIN conditions (never implicit comma joins) "
        "5. Note any assumptions you made about the schema or business logic "
        "6. Suggest indexes that would help this query perform well "
        "7. Note dialect-specific syntax alternatives if relevant "
        "Never SELECT * in production queries — specify columns."
    )

    schema_text = ""
    if args.schema:
        schema_text = read_file(args.schema)

    user_message = f"Write a {db_label} SQL query for:\n\n{args.question}\n\n"

    if schema_text:
        user_message += f"Schema:\n```sql\n{schema_text}\n```\n\n"
    else:
        user_message += (
            "Note: No schema was provided. "
            "Infer reasonable table and column names from the question, "
            "and state your schema assumptions clearly.\n\n"
        )

    if args.explain:
        user_message += "Also provide a plain-English explanation of what each clause does.\n"

    user_message += (
        "Format:\n"
        "1. The SQL query (formatted, with a comment header)\n"
        "2. Notes section (assumptions, alternatives, dialect variants)\n"
        "3. Performance tip (index recommendation)"
    )

    print(f"\n--- SQL Query Builder ({db_label}) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_schema(args: argparse.Namespace) -> None:
    """Design a database schema from an application description."""
    db_dialects = {
        "postgres": "PostgreSQL",
        "mysql": "MySQL",
        "sqlite": "SQLite",
        "mssql": "SQL Server",
    }

    db_label = db_dialects.get(args.db.lower(), args.db)

    system_prompt = (
        f"You are a senior database architect specializing in {db_label} schema design. "
        "Design normalized, production-ready relational database schemas. "
        "Always apply: "
        "1. 3NF normalization (avoid data duplication) "
        "2. Appropriate primary key strategy (UUIDs for distributed, auto-increment for simple) "
        "3. Foreign key constraints with proper ON DELETE behavior "
        "4. Performance indexes on foreign keys and frequently queried columns "
        "5. Timestamps: created_at, updated_at on all main entities "
        "6. Soft deletes via deleted_at where appropriate "
        "7. Many-to-many relationships via junction tables "
        "Generate complete CREATE TABLE DDL statements with all constraints. "
        "Add design rationale comments for non-obvious decisions."
    )

    user_message = (
        f"Design a {db_label} database schema for:\n\n{args.description}\n\n"
        f"Requirements:\n"
    )

    if args.soft_deletes:
        user_message += "- Include soft deletes (deleted_at) on main entities\n"

    if args.uuid:
        user_message += "- Use UUIDs as primary keys\n"
    else:
        user_message += "- Use auto-incrementing integer primary keys unless UUIDs are clearly better\n"

    user_message += (
        "\nProvide:\n"
        "1. Complete CREATE TABLE statements (all tables, all constraints)\n"
        "2. CREATE INDEX statements for performance\n"
        "3. ER diagram description (text-based: table -> relationship -> table)\n"
        "4. Design decisions section (explain non-obvious choices)"
    )

    if args.include_migrations:
        user_message += (
            "\n5. Sample migration file structure "
            "(Alembic for Python/SQLAlchemy, or Flyway naming convention for Java)"
        )

    print(f"\n--- Database Schema Designer ({db_label}) ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="SQL query building and database schema design with Hermes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- query ---
    query_p = subparsers.add_parser("query", help="Build a SQL query from natural language")
    query_p.add_argument("question", help="Natural language description of the query you need")
    query_p.add_argument("--schema", default=None, help="Path to schema file (SQL or text)")
    query_p.add_argument(
        "--db",
        default="postgres",
        choices=["postgres", "mysql", "sqlite", "mssql", "bigquery", "snowflake"],
        help="Target database engine (default: postgres)",
    )
    query_p.add_argument(
        "--explain",
        action="store_true",
        help="Include plain-English explanation of each clause",
    )
    query_p.set_defaults(func=cmd_query)

    # --- schema ---
    schema_p = subparsers.add_parser("schema", help="Design a database schema")
    schema_p.add_argument("description", help="Application description to base schema on")
    schema_p.add_argument(
        "--db",
        default="postgres",
        choices=["postgres", "mysql", "sqlite", "mssql"],
        help="Target database engine (default: postgres)",
    )
    schema_p.add_argument(
        "--soft-deletes",
        action="store_true",
        help="Include soft delete columns",
    )
    schema_p.add_argument(
        "--uuid",
        action="store_true",
        help="Use UUID primary keys",
    )
    schema_p.add_argument(
        "--include-migrations",
        action="store_true",
        help="Include migration file structure",
    )
    schema_p.set_defaults(func=cmd_schema)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
