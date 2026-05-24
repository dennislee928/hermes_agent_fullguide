# Git Commit Message Writer

## Description
Git Commit Message Writer reads a git diff and generates a well-structured, conventional commit message that accurately describes the changes. It follows the Conventional Commits specification and includes a body when the change complexity warrants one.

## Why Hermes
Hermes understands code semantics well enough to describe what a diff does, not just what files it touches. It correctly identifies the type (feat, fix, refactor, chore), scope, and the "why" of a change to produce messages that are useful for future developers reading git log.

## Quickstart
```bash
# Pipe git diff directly
git diff --staged | python examples/technical/devops_tools.py commit-message

# From a file
python examples/technical/devops_tools.py commit-message --diff changes.diff
```

## Sample Input
```diff
diff --git a/auth/middleware.py b/auth/middleware.py
index a1b2c3d..e4f5g6h 100644
--- a/auth/middleware.py
+++ b/auth/middleware.py
@@ -12,7 +12,11 @@ class AuthMiddleware:
     def authenticate(self, request):
-        token = request.headers.get('Authorization')
-        if not token:
-            return None
-        return self.decode_token(token)
+        auth_header = request.headers.get('Authorization')
+        if not auth_header:
+            return None
+        if not auth_header.startswith('Bearer '):
+            raise AuthenticationError("Invalid token format")
+        token = auth_header[7:]  # Strip "Bearer " prefix
+        return self.decode_token(token)
```

## Expected Output Format
```
fix(auth): validate Bearer token prefix before decoding

Previously, the auth middleware accepted any non-empty Authorization header
value and passed it directly to the token decoder. This caused confusing
decode errors when clients sent malformed headers (e.g., missing "Bearer "
prefix or sending raw tokens).

Now explicitly checks for the "Bearer " prefix and raises a clear
AuthenticationError with a descriptive message for malformed headers.

Affected: AuthMiddleware.authenticate()
```

## Tips
- Use `git diff --staged` (not `git diff`) to include only staged changes.
- Add `--type feat` to override the inferred commit type if Hermes chooses incorrectly.
- Use `--scope auth` to set the conventional commit scope explicitly.
- For large diffs touching multiple concerns, Hermes will suggest splitting into separate commits.
