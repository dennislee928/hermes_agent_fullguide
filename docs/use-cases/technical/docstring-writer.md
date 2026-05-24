# Docstring Writer

## Description
Docstring Writer generates accurate, complete docstrings for Python functions, classes, and modules in Google, NumPy, or reStructuredText style. It infers parameter types, descriptions, and return value documentation directly from the code without requiring manual annotation.

## Why Hermes
Hermes reads function signatures and bodies to infer parameter semantics accurately — it doesn't just repeat variable names, it explains what each parameter represents. It handles complex return types, exceptions, and class hierarchies in a single pass.

## Quickstart
```bash
python examples/technical/code_generation.py docstrings \
  --file mymodule.py \
  --style google
```

## Sample Input
```python
def paginate_query(queryset, page, page_size=20):
    offset = (page - 1) * page_size
    return queryset[offset:offset + page_size], queryset.count()
```

## Expected Output Format
```python
def paginate_query(queryset, page, page_size=20):
    """Paginate a Django queryset and return a page of results with total count.

    Calculates the correct offset for the given page number and slices the
    queryset accordingly. Does not execute the full count query until called.

    Args:
        queryset: A Django QuerySet to paginate. Must be orderable for
            consistent pagination results.
        page (int): The 1-indexed page number to retrieve. Page 1 returns
            the first `page_size` results.
        page_size (int, optional): Number of items per page. Defaults to 20.

    Returns:
        tuple: A 2-tuple of:
            - QuerySet: The sliced queryset for the requested page.
            - int: Total count of objects in the unsliced queryset.

    Example:
        >>> items, total = paginate_query(User.objects.all(), page=2, page_size=10)
        >>> print(f"Showing items 11-20 of {total}")
    """
    offset = (page - 1) * page_size
    return queryset[offset:offset + page_size], queryset.count()
```

## Tips
- Use `--style numpy` for scientific/data projects, `--style google` for general Python, `--style sphinx` for API docs.
- Pass the full file to get consistent docstrings that reference each other where relevant.
- Add `--include-examples` to always generate usage examples in docstrings.
- For classes, Hermes will generate both the class-level docstring and all method docstrings.
