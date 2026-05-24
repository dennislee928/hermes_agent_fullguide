# Code Complexity Explainer

## Description
Code Complexity Explainer analyzes code to identify high-complexity areas, explains why they are complex, and suggests concrete simplification strategies. It helps developers understand and reduce technical debt before it becomes a maintenance burden.

## Why Hermes
Hermes explains complexity in human terms — not just a cyclomatic complexity score, but why deeply nested conditionals are hard to test, why long parameter lists signal design problems, and what specific pattern (strategy, early return, decomposition) would simplify each case.

## Quickstart
```bash
python examples/technical/code_tools.py complexity \
  --file mycode.py
```

## Sample Input
```python
def process_order(order, user, config, payment_gateway):
    if order:
        if user:
            if user.is_active:
                if not user.is_banned:
                    if order.total > 0:
                        if config.get('payments_enabled'):
                            if payment_gateway.is_available():
                                result = payment_gateway.charge(order.total)
                                if result.success:
                                    order.status = 'paid'
                                    return order
                                else:
                                    return None
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None
```

## Expected Output Format
```
Complexity Analysis — process_order()

METRICS
  Cyclomatic Complexity: 9 (HIGH — target is < 5)
  Nesting Depth: 9 levels (HIGH — target is < 3)
  Lines of Code: 25 (manageable but masking intent)

ISSUES
1. Arrow Anti-pattern (Pyramid of Doom)
   Nine levels of nesting make this function nearly impossible to reason about.
   The happy path is buried at the deepest level; failure paths are scattered.

2. Guard clauses should be inverted
   Each check returns None on failure — these are guard conditions, not branches.

3. Four parameters is borderline (suggest reviewing if all are necessary)

REFACTORED VERSION (Early Return Pattern)
  def process_order(order, user, config, payment_gateway):
      if not order or not user:
          return None
      if not user.is_active or user.is_banned:
          return None
      if order.total <= 0:
          return None
      if not config.get('payments_enabled') or not payment_gateway.is_available():
          return None

      result = payment_gateway.charge(order.total)
      if not result.success:
          return None

      order.status = 'paid'
      return order

Result: Nesting depth reduced from 9 to 2. Cyclomatic complexity reduced to 6.
Each guard condition now has a single, obvious location.
```

## Tips
- Pass the full file to see a complexity leaderboard — which functions are worst.
- Use `--threshold 5` to only flag functions with cyclomatic complexity above a custom threshold.
- Combine with Refactorer: use complexity output as the `--goal` input for targeted refactoring.
- Complexity is a signal, not a verdict — some inherently complex logic cannot be simplified without losing correctness.
