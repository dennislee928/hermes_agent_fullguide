# SOP Writer

## Description
SOP Writer converts a rough description of a business process into a formal Standard Operating Procedure document with numbered steps, decision points, roles, and success criteria. It ensures institutional knowledge is captured in a reusable, auditable format.

## Why Hermes
Hermes reliably transforms informal process descriptions into precise, unambiguous procedural text with correct structure — numbered steps, conditional branches (if/else logic), and role assignments. It doesn't over-engineer simple processes or under-specify complex ones.

## Quickstart
```bash
python examples/work-productivity/meetings_and_docs.py sop \
  --process "Customer refund handling" \
  --department "Customer Support" \
  --tools "Stripe, Intercom, Jira"
```

## Sample Input
```
Process: Monthly close process for finance
Department: Finance & Accounting
Tools: QuickBooks, Google Sheets, Slack
Roles involved: Accountant, Finance Manager, CFO
Steps (rough): reconcile accounts, categorize transactions, generate P&L, review with manager, send to CFO, archive
```

## Expected Output Format
```
STANDARD OPERATING PROCEDURE
Title: Monthly Financial Close Process
Department: Finance & Accounting
Version: 1.0 | Effective Date: [DATE]
Owner: Finance Manager

1. PURPOSE
   To ensure accurate, timely financial close each month-end.

2. SCOPE
   Applies to: Accountant, Finance Manager, CFO

3. PROCEDURE

   Step 1 — Reconcile All Accounts (Accountant)
   1.1 Log into QuickBooks and pull the current month transaction report.
   1.2 Cross-reference each account against bank statements.
   1.3 Flag any discrepancies > $50 in the Reconciliation Log sheet.
   Decision: If discrepancy cannot be resolved within 4 hours, escalate to Finance Manager.

   Step 2 — Categorize Transactions (Accountant)
   2.1 Apply correct expense categories per the Chart of Accounts.
   2.2 Tag all transactions with project codes where applicable.

   [Steps 3-6 continue...]

4. SUCCESS CRITERIA
   - All accounts reconciled with < $10 variance.
   - P&L delivered to CFO by the 5th business day of following month.

5. REVISION HISTORY
   | Version | Date | Author | Change Summary |
```

## Tips
- Describe the process chronologically in `--process`, even if rough; Hermes handles restructuring.
- Include `--roles` so ownership is correctly assigned at each step.
- Use `--format iso` for ISO 9001-compliant formatting requirements.
- Have the process owner verify step accuracy before publishing — Hermes structures, you verify.
