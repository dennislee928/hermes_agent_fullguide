# Presentation Outline

## Description
Presentation Outline generates a slide-by-slide outline for any talk or pitch, including suggested talking points and visual prompts for each slide. It structures your message logically from hook to call-to-action so you can build slides without staring at a blank deck.

## Why Hermes
Hermes understands narrative arc and persuasive structure, making it effective at organizing ideas into a story rather than a flat list of facts. It reliably follows constraints like slide count and audience type to produce outlines that need minimal restructuring.

## Quickstart
```bash
python examples/work-productivity/project_management.py outline \
  --topic "Launching a company wellness program" \
  --audience "C-suite" \
  --slides 10 \
  --goal "Get budget approval"
```

## Sample Input
```
Topic: Migrating our infrastructure to Kubernetes
Audience: Engineering team (mixed experience levels)
Number of slides: 12
Goal: Align team on migration plan and timeline
Key points: current pain points, K8s benefits, migration phases, risks, timeline
```

## Expected Output Format
```
Presentation Outline: Kubernetes Migration Plan

Slide 1 — Title
  "From VMs to Kubernetes: Our Path Forward"
  Visual: Architecture diagram split view

Slide 2 — The Problem (Hook)
  Talking points: Deployment time, scaling bottlenecks, ops overhead
  Visual: Graph of deployment frequency vs. time

Slide 3 — What Is Kubernetes?
  Talking points: Brief intro for mixed audience, key concepts only
  Visual: Simple K8s node/pod diagram

Slide 4-11 — [Body slides covering benefits, phases, risks, timeline]

Slide 12 — Call to Action
  Talking points: What we need from the team this week
  Visual: Timeline with owner names
```

## Tips
- Include your `--goal` explicitly; it anchors the narrative arc (inform vs. persuade vs. train).
- Add `--format pitch` for investor-style decks or `--format workshop` for interactive sessions.
- Use `--key-points` to list must-cover topics; Hermes will fit them into logical slide order.
- After generating the outline, run it through the Tone Checker for audience alignment.
