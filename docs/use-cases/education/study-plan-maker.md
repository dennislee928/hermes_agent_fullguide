# Study Plan Maker

## Description
Create a personalized, day-by-day study schedule based on the subject, exam date, and available study hours. The plan breaks large topics into manageable daily goals, incorporates review sessions, and accounts for spaced repetition principles.

## Why Hermes
Generating a coherent multi-week schedule requires holding many constraints simultaneously — available days, topic dependencies, review cycles. Hermes-3's strong reasoning ability produces plans that are logically sequenced rather than simply listing topics in random order.

## Quickstart
```bash
python examples/education/study_tools.py study-plan --subject "Calculus" --exam-date "2024-03-15" --hours-per-day 2
```

## Sample Input
```
Subject: AP Biology
Exam date: 2024-05-07
Hours per day: 1.5
Topics: Cell Biology, Genetics, Evolution, Ecology, Physiology
```

## Output Format
```
STUDY PLAN: AP Biology
Total days available: 42  |  Total study hours: 63
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK 1: Cell Biology Foundations
  Day 1 (Feb 24) — Cell structure & organelles (1.5 hrs)
  Day 2 (Feb 25) — Cell membrane & transport (1.5 hrs)
  Day 3 (Feb 26) — Review Day 1-2 + practice questions (1.5 hrs)
  ...

WEEK 2: Genetics
  ...

FINAL WEEK: Full Review & Exam Strategy
  Day 40 — Full practice exam under timed conditions
  Day 41 — Review weak areas identified in practice exam
  Day 42 — Light review only; rest and prepare
```

## Tips
- Specify `--topics` as a comma-separated list to give Hermes explicit subject matter to schedule.
- Add `--include-breaks` to have rest days and buffer days built into the plan.
- Re-run with a closer exam date as the exam approaches to generate a condensed crunch plan.
- Combine with the flashcard generator to create materials for each day's topic.
