# Code Refactorer

## Description
Code Refactorer takes existing code and rewrites it according to a specified goal — adding type hints, improving readability, reducing complexity, applying a design pattern, or modernizing syntax. It returns the refactored code alongside an explanation of every change made.

## Why Hermes
Hermes applies refactoring goals precisely and consistently across an entire file without introducing new bugs or deviating from the original logic. It explains each transformation, making the refactor a learning opportunity rather than a black-box rewrite.

## Quickstart
```bash
python examples/technical/code_tools.py refactor \
  --file messy.py \
  --goal "add type hints and replace loops with list comprehensions"
```

## Sample Input
```python
def process(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    total = 0
    for r in result:
        total = total + r
    return total
```

Goal: Add type hints, use list comprehensions, use built-ins

## Expected Output Format
```python
def process(data: list[int | float]) -> int | float:
    """Return double the sum of all positive values in data."""
    positive_doubled = [item * 2 for item in data if item > 0]
    return sum(positive_doubled)
```

Changes Made:
1. Added type hints to parameter and return value.
2. Replaced the filtering+mapping loop with a single list comprehension.
3. Replaced the manual summation loop with the built-in `sum()`.
4. Added a docstring describing the function's purpose.
5. No behavioral changes — output is identical for all inputs.

## Tips
- Be specific in `--goal`: "add type hints", "extract magic numbers to constants", "apply strategy pattern".
- Use `--verify` to ask Hermes to include a comment noting which behaviors are preserved.
- For large files, refactor one function at a time for safer incremental changes.
- Combine with Unit Test Generator: generate tests first, then refactor, then confirm tests still pass.
