# Performance Review Writer

## Description
Performance Review Writer helps managers and employees translate rough notes, accomplishments, and observations into polished, fair, and constructive performance review text. It produces calibrated language appropriate for formal HR documentation.

## Why Hermes
Hermes excels at rewriting vague or charged language into professional, growth-oriented framing that HR systems expect. It applies appropriate positive/constructive balance based on the overall rating context and avoids biased phrasing patterns.

## Quickstart
```bash
python examples/work-productivity/career_tools.py perf-review \
  --role "Senior Engineer" \
  --rating "exceeds expectations" \
  --notes "delivered auth rewrite, mentored 2 juniors, missed one deadline due to scope creep"
```

## Sample Input
```
Employee: Mid-level designer
Rating: Meets Expectations
Notes:
  - Delivered all assigned projects on time
  - Good at execution but rarely proposes new ideas
  - Occasionally needs to be reminded of deadlines
  - Team enjoys working with them
  - Could improve cross-functional communication
Tone: constructive and encouraging
```

## Expected Output Format
```
Performance Review — Meets Expectations

Achievements & Strengths:
[Employee] delivered all assigned projects on schedule throughout the review period,
demonstrating consistent reliability and strong execution skills. Their collaborative
approach has been a positive force on team morale, with multiple peers noting their
helpfulness and approachability.

Areas for Growth:
To advance to the next level, [Employee] is encouraged to take a more proactive role
in shaping project direction, not just executing on defined scope. Building the habit
of bringing early ideas and proposals to design reviews will be a key growth lever.
Additionally, refining deadline communication — particularly when workload is high —
will strengthen cross-functional trust.

Goals for Next Period:
1. Propose at least one original design initiative per quarter.
2. Establish a weekly check-in practice with key cross-functional partners.
3. Share a progress update proactively when a deadline is at risk.
```

## Tips
- Use `--rating` to anchor tone: "exceeds" skews positive, "needs improvement" skews constructive.
- Add `--pov employee` to write self-review text instead of manager review.
- For sensitive feedback, use `--soften` to avoid language that could read as punitive.
- Always review output for factual accuracy; Hermes cannot verify claims in notes.
