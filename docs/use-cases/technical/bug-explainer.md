# Bug Explainer

## Description
Bug Explainer takes a code snippet and error message (or just a suspicious function) and produces a plain-English explanation of what is wrong, why it happens, and how to fix it. It bridges the gap between cryptic stack traces and understanding.

## Why Hermes
Hermes accurately traces execution paths through code to identify root causes, explains runtime errors in accessible language, and distinguishes between the location where an error surfaces and the actual source of the bug — a distinction many tools miss.

## Quickstart
```bash
python examples/technical/code_tools.py explain-bug \
  --code "def foo(): return 1/0" \
  --error "ZeroDivisionError: division by zero"
```

## Sample Input
```python
def process_items(items):
    results = []
    for i in range(len(items) + 1):
        results.append(items[i] * 2)
    return results

# Error: IndexError: list index out of range
```

## Expected Output Format
```
Bug Explanation — IndexError in process_items()

WHAT IS HAPPENING
The function iterates from index 0 to len(items) inclusive (range(len(items) + 1)).
For a list of 3 items [a, b, c], valid indices are 0, 1, 2. The loop runs 0, 1, 2, 3.
On the 4th iteration, items[3] is accessed but does not exist — Python raises IndexError.

ROOT CAUSE
Off-by-one error: `range(len(items) + 1)` goes one step too far.
The +1 was likely intended to be "length" but is actually "length + 1 iterations".

THE FIX
Option 1 — Fix the range (simplest):
  for i in range(len(items)):  # Remove the + 1

Option 2 — Use idiomatic Python (preferred):
  results = [item * 2 for item in items]

WHY IT DIDN'T FAIL IN TESTING
If tests only used empty lists or were never run, the bug would not surface until
a non-empty list was passed. Add a test with items = [1, 2, 3] to catch this.

RELATED BUGS TO CHECK
- Any other loops in this file using range(len(...) + 1) likely have the same issue.
```

## Tips
- Always include the error message and stack trace with `--error` for faster diagnosis.
- Use `--context surrounding_code` if the bug involves multiple functions calling each other.
- Works well for race conditions, type errors, and async/await bugs — just paste the relevant code.
- Combine with Unit Test Generator: after fixing, generate tests to prevent regression.
