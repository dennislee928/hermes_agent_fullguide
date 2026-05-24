# API Doc Generator

## Description
API Doc Generator reads source code, route definitions, or function signatures and produces clear, complete API documentation in Markdown or OpenAPI format. It documents endpoints, parameters, request/response schemas, authentication requirements, and error codes.

## Why Hermes
Hermes infers request/response shapes from handler code accurately, documents implicit behaviors (authentication checks, default values, error conditions), and produces documentation that reflects what the code actually does rather than what a developer intended to document.

## Quickstart
```bash
python examples/technical/debugging_tools.py api-docs \
  --file routes/users.py \
  --format markdown
```

## Sample Input
```python
@router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    include_orders: bool = False,
    current_user: User = Depends(get_current_user)
):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    result = user.dict()
    if include_orders:
        result["orders"] = await db.get_orders(user_id)
    return result
```

## Expected Output Format
```markdown
## GET /users/{user_id}

Retrieve a user by their unique ID. Admins can access any user; non-admins can
only access their own profile.

**Authentication:** Bearer token required

**Path Parameters**
| Name    | Type | Required | Description       |
|---------|------|----------|-------------------|
| user_id | int  | Yes      | Unique user ID    |

**Query Parameters**
| Name           | Type | Default | Description                              |
|----------------|------|---------|------------------------------------------|
| include_orders | bool | false   | When true, includes the user's order list|

**Responses**
| Status | Description                                  |
|--------|----------------------------------------------|
| 200    | User object, optionally with orders array    |
| 403    | Forbidden — non-admin accessing another user |
| 404    | User not found                               |

**Example Response (200)**
```json
{
  "id": 42,
  "email": "user@example.com",
  "created_at": "2024-01-15T10:30:00Z",
  "orders": []
}
```
```

## Tips
- Pass the full router file with `--file` to document all endpoints in one pass.
- Use `--format openapi` to get YAML output compatible with Swagger UI.
- Add `--base-url https://api.example.com` to include full URL examples.
- Combine with the Docstring Writer to document both the HTTP interface and internal code.
