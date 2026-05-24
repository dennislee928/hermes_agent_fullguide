# Contract Summarizer

## Description
Contract Summarizer reads dense legal or commercial contract text and produces a plain-language summary of key terms, obligations, risks, and red flags. It helps non-lawyers quickly understand what they are agreeing to before involving legal counsel.

## Why Hermes
Hermes handles long, clause-heavy documents and accurately extracts critical terms — payment schedules, termination clauses, IP ownership, liability caps — without missing important details or misrepresenting legal language. It clearly flags ambiguous or potentially unfavorable terms.

## Quickstart
```bash
python examples/work-productivity/business_tools.py summarize-contract \
  --file contract.txt \
  --focus "payment terms, termination, IP ownership"
```

## Sample Input
```
[Excerpt from SaaS vendor agreement]
"...Notwithstanding any other provision herein, either party may terminate this
Agreement upon thirty (30) days written notice. Vendor retains the right to
suspend service immediately upon non-payment. All data processed through the
platform becomes the non-exclusive property of Vendor for the purpose of
service improvement and model training..."
```

## Expected Output Format
```
Contract Summary — SaaS Vendor Agreement

QUICK OVERVIEW
Type: SaaS Subscription Agreement
Pages reviewed: 24
Risk level: MEDIUM — 3 flagged clauses

KEY TERMS
| Term              | Detail                                              |
|-------------------|-----------------------------------------------------|
| Contract length   | 12 months, auto-renews unless cancelled 60 days prior|
| Payment           | Monthly, Net 30                                     |
| Termination       | Either party, 30 days written notice                |
| Governing law     | State of Delaware                                   |

RED FLAGS
1. DATA RIGHTS (Section 8.2) — Vendor claims non-exclusive rights to your data
   for "model training." This means your data may train their AI products.
   Recommendation: Negotiate removal or limit to anonymized aggregate data only.

2. IMMEDIATE SUSPENSION (Section 5.4) — Vendor can suspend without notice on
   non-payment, with no cure period.
   Recommendation: Request a 5-business-day cure period before suspension.

3. LIABILITY CAP (Section 12.1) — Vendor liability capped at 1 month of fees paid.
   This is very low for enterprise use.
   Recommendation: Negotiate cap to 12 months of fees or a fixed floor.

NOTE: This is a summary for initial review only. Have legal counsel review
before signing.
```

## Tips
- This tool is for initial comprehension, not legal advice — always involve counsel for important contracts.
- Use `--focus` to prioritize specific clauses: `"IP, liability, data"`.
- For very long contracts, split into sections and summarize each independently.
- Add `--compare other_contract.txt` to diff two versions of an agreement (future feature).
