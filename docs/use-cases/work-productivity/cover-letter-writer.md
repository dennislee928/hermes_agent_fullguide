# Cover Letter Writer

## Description
Cover Letter Writer produces a tailored, compelling cover letter for any job application by aligning your experience and skills with the specific role and company. It avoids generic filler and focuses on the concrete value you bring to the position.

## Why Hermes
Hermes follows multi-variable instructions precisely — role requirements, company tone, candidate background, and word limit — to generate cover letters that feel personalized rather than templated. It reliably highlights relevant experience without inventing credentials.

## Quickstart
```bash
python examples/work-productivity/career_tools.py cover-letter \
  --role "Software Engineer" \
  --company "Acme Corp" \
  --resume resume.txt \
  --jd job_description.txt
```

## Sample Input
```
Role: Senior Product Manager
Company: Stripe
Job Description highlights: payments infrastructure, B2B SaaS, data-driven, cross-functional leadership
Resume highlights:
  - 5 years PM at fintech startup
  - Launched 3 payment products used by 500k merchants
  - Led engineering team of 8 through series B
  - Strong SQL and data analysis skills
Tone: confident but not arrogant
```

## Expected Output Format
```
[Your Name]
[Email] | [LinkedIn] | [Location]

Hiring Team, Stripe

I've spent five years building payment products at scale, and Stripe's infrastructure
work sits at the intersection of everything I'm most passionate about: elegant APIs,
merchant trust, and data-informed decisions that move the needle on revenue.

At [Company], I led the end-to-end launch of three payment products now used by over
500,000 merchants. That required deep partnership with engineering, legal, and
compliance — exactly the cross-functional coordination Stripe describes in this role.
I also brought a hands-on data practice to the team; I write SQL daily and built our
product analytics dashboards from scratch.

What draws me to Stripe specifically is your commitment to developer experience as a
product principle, not an afterthought. I'd love to bring that same philosophy to your team.

I'd welcome the chance to talk. Thank you for your consideration.

[Your Name]
```

## Tips
- Provide both `--resume` and `--jd` (job description) files for the most targeted output.
- Use `--tone confident` vs. `--tone humble` to match company culture signals in the JD.
- Add `--word-limit 300` to keep letters concise for companies that prefer brevity.
- Run the output through the Tone Checker to verify it matches the company's communication style.
