# Invoice Generator

## Description
Invoice Generator creates professional, correctly formatted invoice text from project details, line items, and client information. It handles calculations, formatting, and standard invoice fields so you can generate a billable document in seconds.

## Why Hermes
Hermes accurately processes structured billing data — line items, rates, quantities, taxes — and produces clean, professional invoice text with correct arithmetic. It adapts to different invoice formats (hourly, project-based, milestone-based) from the same simple input.

## Quickstart
```bash
python examples/work-productivity/business_tools.py invoice \
  --client "Acme Corp" \
  --items "Web Design:40hrs:$150, Project Management:10hrs:$120" \
  --due-days 30
```

## Sample Input
```
Freelancer: Jane Smith Design Studio
Client: BuildRight Inc.
Invoice number: INV-2024-047
Services:
  - Brand identity design: 1 project @ $2,500
  - Logo variations (3): 1 set @ $500
  - Brand guidelines document: 1 @ $800
  - Rush delivery surcharge: 20%
Payment terms: Net 15
Notes: Please reference project code BR-2024-09 in payment
```

## Expected Output Format
```
INVOICE

From:                          Invoice #: INV-2024-047
Jane Smith Design Studio       Date: [TODAY]
jane@janedesign.com           Due Date: [TODAY + 15 days]
[Address]

To:
BuildRight Inc.
[Client Address]

SERVICES
| Description                  | Qty | Unit Price | Amount    |
|------------------------------|-----|------------|-----------|
| Brand identity design        |  1  | $2,500.00  | $2,500.00 |
| Logo variations (3-pack)     |  1  |   $500.00  |   $500.00 |
| Brand guidelines document    |  1  |   $800.00  |   $800.00 |
| Rush delivery surcharge (20%)|  1  |   $760.00  |   $760.00 |
|------------------------------|-----|------------|-----------|
| SUBTOTAL                     |     |            | $4,560.00 |
| TAX (0%)                     |     |            |     $0.00 |
| TOTAL DUE                    |     |            | $4,560.00 |

Payment Reference: BR-2024-09
Bank Transfer: [Account details]
Due by: [DATE]

Thank you for your business!
```

## Tips
- Provide all line items in `--items` as `"Description:qty:unit_price"` format.
- Use `--tax 8.5` to apply a sales tax percentage to the total.
- Add `--currency EUR` for international invoices.
- The output is text-based; copy into a Word template or invoice tool for final formatting.
