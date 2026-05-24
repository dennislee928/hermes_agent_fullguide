# Report Writer

## Description
Report Writer takes raw data points, findings, or bullet notes and produces a fully structured business report with executive summary, body sections, and recommendations. It turns your raw analysis into a polished deliverable without requiring manual formatting work.

## Why Hermes
Hermes maintains consistent professional prose across multi-section documents and correctly interprets data relationships to write coherent narratives — not just bullet expansions. It also adapts the report structure to audience type (executive vs. technical) based on a single instruction.

## Quickstart
```bash
python examples/work-productivity/meetings_and_docs.py report \
  --title "Q2 Performance Report" \
  --audience executive \
  --data "Revenue up 12% YoY, churn down 3%, support tickets up 18%, NPS score 42"
```

## Sample Input
```
Title: Monthly Marketing Performance Report — May
Audience: Marketing Director
Data points:
  - Website traffic: 48,200 visits (+7% MoM)
  - Conversion rate: 2.4% (down from 2.8% last month)
  - Email campaign open rate: 31%
  - Cost per lead: $18.50
  - Top source: organic search (42%)
  - Paid ads ROI: 3.1x
```

## Expected Output Format
```
# Monthly Marketing Performance Report — May

## Executive Summary
May showed continued traffic growth of 7% month-over-month, reaching 48,200 visits.
However, conversion rate declined from 2.8% to 2.4%, indicating a gap between
traffic quality and landing page performance that warrants investigation.

## Key Metrics
| Metric              | May Value | Change     |
|---------------------|-----------|------------|
| Website Traffic     | 48,200    | +7% MoM    |
| Conversion Rate     | 2.4%      | -0.4pp MoM |
| Email Open Rate     | 31%       | —          |
| Cost Per Lead       | $18.50    | —          |
| Paid Ads ROI        | 3.1x      | —          |

## Analysis
...

## Recommendations
1. A/B test landing pages targeting organic search visitors.
2. Review paid ad targeting given strong 3.1x ROI — consider increasing budget.
```

## Tips
- Provide numeric data with context (vs. prior period, target, or benchmark) for richer analysis.
- Use `--audience technical` for detailed methodology sections, `--audience executive` for brevity.
- The `--tone` flag (`formal`, `conversational`) adjusts prose style throughout.
- For data-heavy reports, supply the raw table as a CSV paste in `--data` for best results.
