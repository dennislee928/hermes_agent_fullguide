# Retrospective Facilitator

## Description
Retrospective Facilitator helps engineering and product teams structure sprint or project retrospectives by generating discussion prompts, synthesizing team input, and producing a clear action item list with owners. It moves retros from venting sessions to productive improvement cycles.

## Why Hermes
Hermes identifies patterns in team feedback, groups related themes, and generates constructive framing — turning raw team input like "deploys keep breaking" into actionable discussion points and improvement hypotheses rather than complaint lists.

## Quickstart
```bash
python examples/work-productivity/project_management.py retro \
  --sprint "Sprint 24" \
  --went-well "shipped feature on time, good code reviews" \
  --improve "deploy failed twice, standups run long" \
  --format action-plan
```

## Sample Input
```
Sprint: Q3 Sprint 3
Team: 5 engineers, 1 PM, 1 designer
Went well:
  - Feature shipped on time
  - New pairing sessions were valuable
  - PR reviews faster than usual
Needs improvement:
  - Two production incidents from undiscovered edge cases
  - Sprint planning took 3 hours (should be 90 min)
  - Designer was blocked for 2 days waiting on API spec
Actions from last retro: Added integration tests (partially done)
```

## Expected Output Format
```
Sprint Retrospective — Q3 Sprint 3

WENT WELL (Keep Doing)
+ On-time delivery: reinforce estimation and scope discipline.
+ Pairing sessions: schedule recurring slots, don't leave to chance.
+ Faster PR reviews: identify what changed and codify it.

NEEDS IMPROVEMENT (Discussion Prompts)
Issue 1: Production incidents from edge cases
  Root cause hypothesis: Test coverage gap on boundary conditions.
  Discussion: What pre-ship checklist would catch these? Who owns it?

Issue 2: Sprint planning taking 3 hours
  Root cause hypothesis: Stories not pre-refined before planning.
  Discussion: Should we move refinement to mid-sprint? What does "ready" mean for us?

Issue 3: Designer blocked 2 days on API spec
  Root cause hypothesis: API spec not defined as a prerequisite in workflow.
  Discussion: Can we add "API spec complete" as a Definition of Ready gate?

ACTION ITEMS
| # | Action                                  | Owner     | Due        |
|---|-----------------------------------------|-----------|------------|
| 1 | Create edge-case test checklist         | Bob       | Next sprint|
| 2 | Establish Definition of Ready with PM   | Alice + PM | This week  |
| 3 | Add API spec to sprint planning gate    | PM        | Next sprint|
| 4 | Finish remaining integration tests      | Carol     | EOW        |
```

## Tips
- Provide `--actions-last-retro` so Hermes checks follow-through before setting new ones.
- Use `--format discussion-only` to generate prompts without pre-summarizing if the team wants open conversation first.
- Add `--team-size` to calibrate the number of action items (small teams can handle fewer).
- Run immediately after the retro to turn live notes into a formatted doc for Confluence or Notion.
