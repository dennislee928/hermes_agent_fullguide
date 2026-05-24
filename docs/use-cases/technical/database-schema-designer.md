# Database Schema Designer

## Description
Database Schema Designer generates normalized relational database schemas from a high-level description of an application's data model. It produces CREATE TABLE statements, indexes, foreign key constraints, and design rationale for any described system.

## Why Hermes
Hermes applies normalization principles, identifies natural many-to-many relationships, selects appropriate column types, and adds performance-critical indexes without being explicitly instructed to do so — producing schemas that are correct by design rather than requiring multiple rounds of revision.

## Quickstart
```bash
python examples/technical/database_tools.py schema \
  "e-commerce app with products, orders, users, reviews"
```

## Sample Input
```
Application: Project management SaaS
Entities: organizations, users, projects, tasks, comments, file attachments, labels/tags
Requirements:
  - Users belong to organizations
  - Projects belong to organizations
  - Tasks have assignees, due dates, priority, status
  - Tasks can have parent tasks (subtasks)
  - Comments and attachments on tasks
  - Many-to-many: tasks can have multiple labels
  - Soft deletes on all main entities
Database: PostgreSQL
```

## Expected Output Format
```sql
-- ============================================================
-- Project Management Schema — PostgreSQL
-- ============================================================

CREATE TABLE organizations (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        VARCHAR(255) NOT NULL,
    slug        VARCHAR(100) UNIQUE NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at  TIMESTAMPTZ
);

CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id          UUID NOT NULL REFERENCES organizations(id),
    email           VARCHAR(255) UNIQUE NOT NULL,
    display_name    VARCHAR(255) NOT NULL,
    role            VARCHAR(50) NOT NULL DEFAULT 'member',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
CREATE INDEX idx_users_org ON users(org_id) WHERE deleted_at IS NULL;

-- [tasks, projects, comments, attachments, labels tables continue...]

-- Many-to-many: tasks <-> labels
CREATE TABLE task_labels (
    task_id     UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
    label_id    UUID NOT NULL REFERENCES labels(id) ON DELETE CASCADE,
    PRIMARY KEY (task_id, label_id)
);
```

Design Notes:
- UUIDs used for IDs to support future sharding and avoid sequential ID enumeration.
- Soft deletes via `deleted_at` timestamp on all main entities.
- Self-referential `parent_task_id` on tasks table handles subtasks.
- Partial indexes exclude soft-deleted rows for query efficiency.

## Tips
- Describe relationships explicitly: "users belong to organizations" gives more accurate FKs.
- Mention database engine; PostgreSQL, MySQL, and SQLite have different type and feature sets.
- Use `--include-migrations` to get Alembic or Flyway migration files alongside schema DDL.
- For complex schemas, generate in sections: core tables first, then junction/audit tables.
