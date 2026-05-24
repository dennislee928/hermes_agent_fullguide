# Meeting Agenda Generator

## Description
Meeting Agenda Generator transforms a meeting title, attendee list, and bullet-point topics into a structured, time-boxed agenda document ready to share. It ensures every meeting has a clear purpose, owner for each item, and defined time allocation.

## Why Hermes
Hermes reliably maps unstructured topic lists to formatted agenda tables with accurate time distribution, because its instruction-following capability keeps the output schema consistent across runs. It also infers logical sequencing (e.g., placing housekeeping last and blockers first) without being explicitly told.

## Quickstart
```bash
python examples/work-productivity/meetings_and_docs.py agenda \
  --title "Q3 Sprint Kickoff" \
  --duration 60 \
  --attendees "PM, Engineering Lead, Designer, QA" \
  --topics "sprint goals, backlog grooming, design review, blockers, action items"
```

## Sample Input
```
Meeting: Weekly Engineering Sync
Duration: 45 minutes
Attendees: Alice (EM), Bob (Backend), Carol (Frontend), Dave (DevOps)
Topics:
  - Deployment status from last week
  - Review open PRs blocking release
  - Discuss database migration plan
  - Any blockers / help needed
  - Next steps and owners
```

## Expected Output Format
```
# Weekly Engineering Sync — Agenda
Date: [DATE] | Duration: 45 min | Facilitator: Alice

| # | Topic                          | Owner  | Time  |
|---|-------------------------------|--------|-------|
| 1 | Deployment status update       | Dave   | 5 min |
| 2 | Open PRs blocking release      | Bob    | 10 min|
| 3 | Database migration plan        | Bob    | 15 min|
| 4 | Blockers & help needed         | All    | 10 min|
| 5 | Next steps & action item owners| Alice  | 5 min |

Pre-read: [link to relevant docs if any]
Goal: Align on release readiness and unblock migration work.
```

## Tips
- Provide attendee roles, not just names, so Hermes can assign agenda item owners intelligently.
- For recurring meetings, add `--recurring weekly` so the output notes the cadence.
- Use `--goal "one sentence"` to anchor the agenda to a specific outcome.
- Time allocations are estimates; ask Hermes to "redistribute time so decision items get more" if needed.
