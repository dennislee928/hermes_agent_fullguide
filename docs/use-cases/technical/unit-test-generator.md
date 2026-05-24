# Unit Test Generator

## Description
Unit Test Generator produces comprehensive test suites for Python functions and modules, covering happy paths, edge cases, and error conditions. It saves developers the tedious work of writing boilerplate test scaffolding and ensures important failure modes are covered.

## Why Hermes
Hermes identifies non-obvious edge cases — empty inputs, type mismatches, boundary values, concurrency hazards — beyond what developers typically test first. It generates idiomatic test code for pytest or unittest that is ready to run with minimal modification.

## Quickstart
```bash
python examples/technical/code_generation.py tests \
  --file mymodule.py \
  --framework pytest
```

## Sample Input
```python
def calculate_discount(price: float, discount_pct: float, is_member: bool) -> float:
    """Apply a percentage discount, with extra 5% for members."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    discount = price * (discount_pct / 100)
    if is_member:
        discount += price * 0.05
    return round(price - discount, 2)
```

## Expected Output Format
```python
import pytest
from mymodule import calculate_discount


class TestCalculateDiscount:

    def test_basic_discount(self):
        assert calculate_discount(100.0, 10.0, False) == 90.0

    def test_member_gets_extra_5_percent(self):
        assert calculate_discount(100.0, 10.0, True) == 85.0

    def test_zero_discount(self):
        assert calculate_discount(100.0, 0.0, False) == 100.0

    def test_100_percent_discount(self):
        assert calculate_discount(100.0, 100.0, False) == 0.0

    def test_rounding_to_two_decimals(self):
        result = calculate_discount(99.99, 10.0, False)
        assert result == 89.99

    def test_negative_price_raises_value_error(self):
        with pytest.raises(ValueError, match="Price cannot be negative"):
            calculate_discount(-10.0, 10.0, False)

    def test_zero_price(self):
        assert calculate_discount(0.0, 10.0, False) == 0.0

    def test_member_with_zero_base_discount(self):
        assert calculate_discount(100.0, 0.0, True) == 95.0

    @pytest.mark.parametrize("pct", [0, 10, 50, 99, 100])
    def test_various_discount_percentages(self, pct):
        result = calculate_discount(100.0, pct, False)
        assert result == round(100.0 - pct, 2)
```

## Tips
- Pass the full module file for better context; Hermes will generate tests for all public functions.
- Use `--framework unittest` or `--framework pytest` to match your project setup.
- Add `--coverage edge-cases` to bias toward boundary conditions and error paths.
- Generated tests will need mocks for functions that call external APIs or databases — add `--mock-deps` for that.
