# OKR Goal Setter

## Description
OKR Goal Setter transforms strategic intent, team missions, or rough goal ideas into well-formed Objectives and Key Results following OKR best practices. It ensures objectives are aspirational and qualitative while key results are specific, measurable, and time-bound.

## Why Hermes
Hermes understands the OKR framework's nuances — objectives should inspire, key results should be unambiguous metrics — and applies this consistently even when given vague input. It avoids the common trap of writing tasks as key results.

## Quickstart
```bash
python examples/work-productivity/project_management.py okr \
  --team "Engineering" \
  --quarter Q3 \
  --themes "reliability, developer velocity, customer trust"
```

## Sample Input
```
Team: Customer Success
Quarter: Q4
Strategic context: Company goal is to reduce churn by 20% this year
Rough ideas:
  - Improve onboarding
  - Get customers to use more features
  - Respond to customers faster
  - Better QBRs
```

## Expected Output Format
```
OKRs — Customer Success Team | Q4

OBJECTIVE 1: Deliver an onboarding experience that drives early customer success
  KR 1.1: Increase 30-day feature adoption rate from 45% to 65%
  KR 1.2: Reduce time-to-first-value from 14 days to 7 days
  KR 1.3: Achieve NPS > 50 from customers in their first 90 days

OBJECTIVE 2: Expand product engagement across the existing customer base
  KR 2.1: Increase average features used per account from 2.1 to 3.5
  KR 2.2: Run expansion conversations with 80% of accounts in health score tier 1
  KR 2.3: Generate $150k in expansion revenue from existing accounts

OBJECTIVE 3: Build a proactive, fast-response support culture
  KR 3.1: Achieve first-response time < 2 hours for all P1 issues
  KR 3.2: Resolve 90% of support tickets within SLA
  KR 3.3: Complete QBRs for 100% of strategic accounts by end of quarter

Alignment note: These OKRs directly support the company's 20% churn reduction goal
through earlier value realization (O1), deeper stickiness (O2), and faster resolution (O3).
```

## Tips
- Provide company-level goals with `--company-goal` so Hermes can align team OKRs vertically.
- Use `--objectives 2` to limit scope if the team is small or the quarter is short.
- Key results should have a baseline metric; include current numbers in `--themes` for better KRs.
- Review key results for the "confidence test": each KR should be achievable but require stretch.
