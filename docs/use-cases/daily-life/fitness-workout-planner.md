# Fitness Workout Planner

## Description
Create a personalized weekly workout schedule based on fitness goal, available days, equipment, and current fitness level. Each session includes exercises, sets, reps, rest intervals, and warm-up/cool-down guidance.

## Why Hermes for This
Hermes understands exercise science principles — progressive overload, muscle group splits, recovery windows — and can compose safe, goal-aligned programs without needing a specialized fitness API.

## Quickstart
```bash
cd examples/daily-life
python health_and_fitness.py workout --goal "lose weight" --days 4
python health_and_fitness.py workout --goal "build muscle" --days 5 --equipment "barbell,dumbbells,pull-up bar"
```

## Sample Prompt / Input
```
Create a 4-day per week workout plan for fat loss.
I'm an intermediate lifter with access to dumbbells and a pull-up bar.
Each session should be 45-60 minutes including warm-up.
```

## Expected Output Format
```
**4-Day Fat Loss Program (Intermediate)**
Equipment: Dumbbells, Pull-up bar | Session length: 45-60 min

---
**Day 1 — Upper Body Push + Core**
Warm-up (5 min): Arm circles, band pull-aparts, light shoulder press

| Exercise              | Sets | Reps    | Rest   |
|-----------------------|------|---------|--------|
| Dumbbell bench press  | 4    | 10-12   | 60 s   |
| Overhead press        | 3    | 10-12   | 60 s   |
| Push-ups              | 3    | AMRAP   | 45 s   |
| Plank                 | 3    | 45 s    | 30 s   |

Cool-down: Chest stretch, tricep stretch (3 min)

...

**Progressive Overload Note:** Increase dumbbell weight by 2 kg when you can complete all sets at the top of the rep range.
```

## Tips
- Mention injuries or limitations (e.g., `--avoid "lower back exercises"`) for safe programming.
- Use `--level beginner` to reduce volume and include more form cues.
- Add `--cardio hiit` to blend cardio intervals into resistance sessions.
- Re-run after 6 weeks to generate a new mesocycle with increased intensity.
