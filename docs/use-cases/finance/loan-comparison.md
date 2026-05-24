# Loan Comparison

## Description
Compare multiple loan options side-by-side with total cost analysis, monthly payment breakdown, amortization insights, and a clear recommendation based on your stated priorities. Covers mortgages, auto loans, personal loans, and student loan refinancing.

## Why Hermes
Loan comparison requires computing total cost of borrowing (not just monthly payment), understanding how rate differences compound over time, and translating APR differences into real dollar amounts. Hermes performs these calculations and presents them in a decision-ready format.

## Quickstart
```bash
python examples/finance/financial_advisor.py loans --amount 25000 --term 60 --options "Bank A:6.5%,Credit Union:5.9%,Online Lender:7.1%"
```

## Sample Input
```
Loan purpose: Personal loan (debt consolidation)
Amount: $25,000
Options:
  Bank A: 6.5% APR, 60 months
  Credit Union: 5.9% APR, 60 months
  Online Lender: 7.1% APR, 48 months
Priority: Lowest total cost
```

## Output Format
```
LOAN COMPARISON ANALYSIS
Amount: $25,000 | Purpose: Debt Consolidation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SIDE-BY-SIDE COMPARISON

| Lender          | APR   | Term  | Monthly Payment | Total Interest | Total Cost |
|-----------------|-------|-------|-----------------|----------------|------------|
| Credit Union    | 5.9%  | 60 mo | $483.06         | $3,983.60      | $28,983.60 |
| Bank A          | 6.5%  | 60 mo | $489.44         | $4,366.40      | $29,366.40 |
| Online Lender   | 7.1%  | 48 mo | $596.53         | $3,633.44      | $28,633.44 |

TOTAL INTEREST SPREAD
Credit Union vs. Bank A: $382.80 less interest (Credit Union wins at same term)
Online Lender (48-mo): Lowest total interest, but $113.47 higher monthly payment

ANALYSIS

Credit Union (5.9%, 60 months) — RECOMMENDED for budget-conscious approach
- Monthly payment is manageable at $483.06
- Total interest of $3,984 is reasonable for this loan size
- The difference vs. Bank A saves $382 over the life of the loan

Online Lender (7.1%, 48 months) — RECOMMENDED if minimizing total cost is priority
- Despite the higher rate, the shorter term means $350 LESS total interest vs. Bank A
- However: can you comfortably afford $596.53/month? If yes, this saves the most money.
- If the purpose is debt consolidation, verify this monthly payment is lower than current debt minimums.

Bank A (6.5%, 60 months) — Least attractive option
- Higher rate than Credit Union at the same term. No advantage unless Bank A offers relationship benefits (reduced rate for autopay, existing account holder discount).

RATE SENSITIVITY
Each 0.5% APR increase on a $25,000/60-month loan = ~$375 in additional total interest.
Improving your credit score by 50+ points before applying could move you to a lower rate tier.

DECISION FRAMEWORK
- If monthly cash flow is tight: Credit Union, 60 months
- If you can afford higher payments: Online Lender, 48 months (lowest total cost)
- Before choosing: Ask Bank A if they match Credit Union's 5.9% — often possible for existing customers.

DISCLAIMER: These calculations assume fixed-rate loans and no prepayment penalties. Verify all terms, including origination fees, with each lender before signing.
```

## Tips
- Always calculate total cost (not just monthly payment) — a longer term often costs thousands more.
- Ask about origination fees — a 1% origination fee on $25,000 = $250 added to your cost.
- Check if your credit union offers lower rates than banks for the same loan — they often do.
- Improving your credit score before applying can save hundreds to thousands in interest.
