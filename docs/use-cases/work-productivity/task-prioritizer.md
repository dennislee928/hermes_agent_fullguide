# Task Prioritizer

## Description
Task Prioritizer evaluates a list of tasks against urgency and importance criteria to produce a ranked, actionable priority matrix. It gives you a clear picture of what to do now, what to schedule, what to delegate, and what to drop.

## Why Hermes
Hermes accurately applies decision frameworks like the Eisenhower Matrix and MoSCoW method based on concise task descriptions, without needing explicit urgency scores. Its structured output is table-formatted and consistent, making it easy to copy into a project tracker.

## Quickstart
```bash
python examples/work-productivity/project_management.py prioritize \
  --tasks "Fix login bug, Write Q3 report, Schedule team 1-on-1s, Update readme, Respond to client email, Review PRs"
```

## Sample Input
```
Tasks:
- Fix critical authentication bug (customers affected)
- Prepare board presentation for next Friday
- Reply to vendor contract email (non-urgent)
- Refactor payment module (tech debt)
- Set up new hire laptop
- Review and merge 4 open PRs
- Update internal wiki
- Call back recruiter
```

## Expected Output Format
```
Task Priority Matrix (Eisenhower)

DO FIRST — Urgent + Important
| Task                          | Reason                              |
|-------------------------------|-------------------------------------|
| Fix critical auth bug         | Customer-facing, blocking users now |
| Board presentation prep       | Hard deadline, high stakes          |

SCHEDULE — Important, Not Urgent
| Task                          | Suggested Timing                    |
|-------------------------------|-------------------------------------|
| Refactor payment module       | Next sprint                         |
| Review & merge PRs            | Today, end of day                   |

DELEGATE — Urgent, Not Important
| Task                          | Suggested Owner                     |
|-------------------------------|-------------------------------------|
| Set up new hire laptop        | IT / Ops                            |

DROP or DEFER — Not Urgent, Not Important
| Task                          | Reason                              |
|-------------------------------|-------------------------------------|
| Update internal wiki          | No deadline, low impact             |
| Call back recruiter           | Defer to next week                  |
```

## Tips
- Include brief context per task (e.g., "deadline: Friday", "customer-facing") for more accurate categorization.
- Combine with the OKR Goal Setter to align priorities against quarterly objectives.
- Re-run Monday mornings with the week's task list for a consistent planning ritual.
- Use `--framework moscow` for product backlog prioritization instead.
