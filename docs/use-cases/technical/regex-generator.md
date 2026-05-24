# Regex Generator

## Description
Regex Generator produces correct, well-commented regular expressions for any described pattern, along with test cases and an explanation of each component. It eliminates the trial-and-error cycle of writing regex from scratch.

## Why Hermes
Hermes translates natural language pattern descriptions into correct regex with precise grouping, anchoring, and quantifier choices. It proactively flags edge cases (Unicode, multiline, greedy vs. lazy) and explains what each token does so developers understand and maintain the pattern.

## Quickstart
```bash
python examples/technical/debugging_tools.py regex "match email addresses"
python examples/technical/debugging_tools.py regex "extract all IPv4 addresses from text"
```

## Sample Input
```
Pattern: Match a US phone number in any of these formats:
  (555) 123-4567
  555-123-4567
  555.123.4567
  +1 555 123 4567
  5551234567
```

## Expected Output Format
```
Pattern: US Phone Number (flexible format)

REGEX (Python):
  \+?1?\s*[\s.\-]?\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4}

Explained:
  \+?1?         — Optional country code (+1)
  \s*           — Optional whitespace
  [\s.\-]?      — Optional separator (space, dot, dash)
  \(?           — Optional opening parenthesis
  \d{3}         — Area code (3 digits)
  \)?           — Optional closing parenthesis
  [\s.\-]?      — Optional separator
  \d{3}         — Exchange (3 digits)
  [\s.\-]?      — Optional separator
  \d{4}         — Subscriber number (4 digits)

TEST CASES (all should match):
  "(555) 123-4567"   -> match
  "555-123-4567"     -> match
  "555.123.4567"     -> match
  "+1 555 123 4567"  -> match
  "5551234567"       -> match
  "55-1234"          -> NO match (too short)
  "abc"              -> NO match

PYTHON USAGE:
  import re
  pattern = re.compile(r'\+?1?\s*[\s.\-]?\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4}')
  matches = pattern.findall(text)

NOTES:
  - Add anchors (^...$) if matching whole string only.
  - This is intentionally permissive; invalid numbers like (000) 000-0000 will match.
    Use a phone validation library (phonenumbers) for strict validation.
```

## Tips
- Describe edge cases explicitly: "should NOT match partial numbers in longer strings".
- Add `--language javascript` to get the regex in JS syntax (different escape rules).
- Use `--anchored` to get a version that matches the whole string, not substring.
- Always review the test cases section — run them in a regex tester before deploying to production.
