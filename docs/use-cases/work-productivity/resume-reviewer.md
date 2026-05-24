# Resume Reviewer

## Description
Resume Reviewer analyzes a resume for clarity, impact, keyword gaps, and formatting issues, then delivers specific, actionable feedback line by line. It helps candidates present their experience compellingly before submitting to an ATS or recruiter.

## Why Hermes
Hermes provides structured, non-generic critique rather than vague encouragement. It accurately identifies weak action verbs, missing quantification, ATS keyword gaps relative to a target role, and formatting inconsistencies — the specific issues that cause resumes to be overlooked.

## Quickstart
```bash
python examples/work-productivity/career_tools.py review-resume \
  --resume resume.txt \
  --role "Data Scientist" \
  --level mid
```

## Sample Input
```
Resume section (Experience):
  Software Engineer at TechCo (2021-2024)
  - Worked on backend services
  - Helped with database improvements
  - Part of team that launched new product
  - Did code reviews

Target role: Senior Backend Engineer
```

## Expected Output Format
```
Resume Review — Senior Backend Engineer Target

Overall Score: 5/10

Critical Issues:
1. Weak action verbs: "Worked on", "Helped with", "Did" give no sense of ownership or impact.
   Fix: Use "Engineered", "Optimized", "Led", "Delivered".

2. No quantification: None of these bullets has a metric.
   Fix: Add scale (users, requests/sec, latency improvement, team size).

3. Missing keywords for ATS: No mention of specific technologies (languages, frameworks, databases).
   Fix: "Improved database performance" becomes "Optimized PostgreSQL query performance, reducing p95 latency by 40ms"

Rewritten Bullets (Suggested):
- Engineered and maintained 6 backend microservices handling 2M+ daily requests in Go.
- Reduced database query latency by 35% through index optimization and query refactoring.
- Led delivery of [Product Name], coordinating with 3 cross-functional teams over 4 months.
- Conducted weekly code reviews for a team of 5 engineers, improving merge cycle time.

Formatting Notes:
- Use consistent date format throughout: "Jan 2021 – Mar 2024"
```

## Tips
- Provide the target job description with `--jd` for ATS keyword gap analysis.
- Use `--level senior` or `--level entry` so Hermes calibrates expectations appropriately.
- Paste individual sections one at a time for line-by-line granularity.
- Combine with Cover Letter Writer to ensure resume and letter tell the same story.
