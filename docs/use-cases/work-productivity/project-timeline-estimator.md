# Project Timeline Estimator

## Description
Project Timeline Estimator converts a project description and list of deliverables into a phased timeline with milestones, dependencies, and realistic duration estimates. It gives teams a starting-point plan without requiring a dedicated project manager.

## Why Hermes
Hermes can reason about sequential and parallel work streams, identify implicit dependencies, and apply common project patterns (discovery before development, testing before launch) to produce sensible timelines from minimal input.

## Quickstart
```bash
python examples/work-productivity/project_management.py timeline \
  --project "Build a customer feedback portal" \
  --team "2 engineers, 1 designer, 1 PM" \
  --deadline "3 months"
```

## Sample Input
```
Project: Redesign company website
Team: 1 designer, 2 frontend devs, 1 content writer, 1 PM
Deliverables: new branding, 8 redesigned pages, CMS integration, SEO audit
Deadline: 10 weeks from now
Constraints: designer is part-time (20hrs/week), must keep current site live until launch
```

## Expected Output Format
```
Project Timeline: Website Redesign (10 Weeks)

Phase 1 — Discovery & Strategy (Weeks 1-2)
  - Kickoff meeting and stakeholder alignment
  - Content audit and sitemap finalization
  - Brand direction moodboard review
  Milestone: Approved sitemap and brand direction

Phase 2 — Design (Weeks 2-5)
  - Homepage and key landing page wireframes
  - Full visual design (8 pages)
  - Design review cycles (2 rounds)
  Milestone: Approved designs handed to dev

Phase 3 — Development (Weeks 4-8)
  [Overlaps with design for pages approved early]
  - CMS setup and template build
  - Page-by-page implementation
  Milestone: Staging site complete

Phase 4 — QA, SEO & Launch (Weeks 8-10)
  - SEO audit and on-page optimization
  - Cross-browser / device testing
  - Go-live and monitoring
  Milestone: Site live

Risk Flags:
- Part-time designer is the critical path; delays in design delay development.
- CMS integration complexity is unknown; add 3-day buffer in Phase 3.
```

## Tips
- Mention team capacity constraints (part-time, vacation) for more realistic estimates.
- Add `--buffer 20` to have Hermes automatically pad estimates by 20%.
- Use `--output gantt` to get a text-based Gantt chart representation.
- Feed output into the OKR Goal Setter to tie milestones to quarterly goals.
