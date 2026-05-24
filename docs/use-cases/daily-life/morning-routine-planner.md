# Morning Routine Planner

## Description
Build a time-blocked morning routine that fits within a specified duration and aligns with your personal goals — whether productivity, wellness, or a calm start to the day. Each block is timed and ordered for maximum effectiveness.

## Why Hermes for This
Hermes is adept at time-boxing tasks and reasoning about sequencing logic (e.g., shower before getting dressed, coffee while breakfast cooks). It produces routines that feel human and realistic rather than robotically optimized.

## Quickstart
```bash
cd examples/daily-life
python health_and_fitness.py morning-routine --duration 60
python health_and_fitness.py morning-routine --duration 90 --goals "exercise,meditation,healthy breakfast"
```

## Sample Prompt / Input
```
Create a 60-minute morning routine for a productive workday.
I want to include: a short workout, journaling, and a healthy breakfast.
I wake up at 6:30 AM.
```

## Expected Output Format
```
**60-Minute Morning Routine**
Wake time: 6:30 AM | Ready by: 7:30 AM

| Time      | Activity                        | Duration |
|-----------|---------------------------------|----------|
| 6:30 AM   | Wake up — no snooze, drink water| 2 min    |
| 6:32 AM   | Quick stretch / mobility        | 8 min    |
| 6:40 AM   | High-intensity workout          | 20 min   |
| 7:00 AM   | Shower + get dressed            | 15 min   |
| 7:15 AM   | Prepare & eat healthy breakfast | 10 min   |
| 7:25 AM   | Journaling (3 prompts)          | 5 min    |
| 7:30 AM   | Out the door / start work       | —        |

**Journal Prompts:**
1. What is the single most important thing I will accomplish today?
2. What am I grateful for this morning?
3. What would make today a great day?

**Tips for Success:**
- Lay out workout clothes the night before to remove friction.
- Prep breakfast ingredients (overnight oats, smoothie bag) the evening before.
- Place your journal on your pillow so you don't forget.
```

## Tips
- Use `--no-workout` to replace the exercise block with reading or meditation.
- Add `--commute 30` to account for travel time and shift the end target.
- Specify `--kids` to include child-related tasks (school prep, packed lunches) in the schedule.
- Run this alongside the sleep schedule optimizer to ensure your wake time is realistic.
