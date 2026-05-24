# Expense Categorizer

## Description
Expense Categorizer takes a list of raw expense entries and assigns each to the correct accounting or budget category, flags unusual items, and produces a clean categorized summary ready for bookkeeping or expense reports. It eliminates the manual sorting step in expense management.

## Why Hermes
Hermes accurately infers expense categories from merchant names and descriptions using real-world business context — correctly categorizing "Zoom Pro" as Software/SaaS and "Uber Eats — client dinner" as Meals & Entertainment without needing a rules lookup table.

## Quickstart
```bash
python examples/work-productivity/business_tools.py categorize-expenses \
  --file expenses.txt \
  --categories "Travel, Software, Meals, Office Supplies, Marketing, Other"
```

## Sample Input
```
Expense list (raw bank/card export):
Date       | Merchant                | Amount
2024-10-01 | Delta Airlines          | $487.00
2024-10-02 | Marriott Chicago        | $342.00
2024-10-03 | Uber Eats - team lunch  | $89.50
2024-10-05 | AWS                     | $1,240.00
2024-10-06 | Zoom Pro Annual         | $179.00
2024-10-07 | Staples                 | $43.20
2024-10-08 | Google Ads              | $2,100.00
2024-10-10 | Personal - Grocery      | $67.00
```

## Expected Output Format
```
Expense Categorization — October 2024

CATEGORIZED EXPENSES
| Date       | Merchant               | Amount    | Category            |
|------------|------------------------|-----------|---------------------|
| 2024-10-01 | Delta Airlines         | $487.00   | Travel — Airfare    |
| 2024-10-02 | Marriott Chicago       | $342.00   | Travel — Hotel      |
| 2024-10-03 | Uber Eats - team lunch | $89.50    | Meals & Entertainment|
| 2024-10-05 | AWS                    | $1,240.00 | Software/Cloud Infra|
| 2024-10-06 | Zoom Pro Annual        | $179.00   | Software/SaaS       |
| 2024-10-07 | Staples                | $43.20    | Office Supplies     |
| 2024-10-08 | Google Ads             | $2,100.00 | Marketing/Advertising|

FLAGGED — Requires Review
| 2024-10-10 | Personal - Grocery     | $67.00    | PERSONAL — not a business expense |

SUMMARY BY CATEGORY
| Category              | Total     |
|-----------------------|-----------|
| Travel                | $829.00   |
| Software/SaaS & Cloud | $1,419.00 |
| Marketing             | $2,100.00 |
| Meals & Entertainment | $89.50    |
| Office Supplies       | $43.20    |
| Total (business)      | $4,480.70 |
```

## Tips
- Paste your bank export directly into `--file`; Hermes handles varying column formats.
- Use `--categories` to match your company's chart of accounts categories.
- Items flagged as personal are never categorized as business — review before submitting.
- For recurring expenses, create a reference list and add it to `--context` for consistency.
