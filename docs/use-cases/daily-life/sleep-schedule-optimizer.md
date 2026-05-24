# Sleep Schedule Optimizer

## Description
Design an optimal sleep and wind-down schedule based on your required wake time, sleep duration goal, and current habits. The output includes bedtime, wind-down routine, and tips for improving sleep quality.

## Why Hermes for This
Hermes synthesizes sleep hygiene research into actionable, personalized plans. It can reason about circadian rhythm principles, screen time recommendations, and caffeine cutoff windows without needing specialized medical APIs.

## Quickstart
```bash
cd examples/daily-life
python health_and_fitness.py sleep --wake "7am" --bedtime-goal "8h"
python health_and_fitness.py sleep --wake "6:30am" --bedtime-goal "7.5h" --issues "trouble falling asleep"
```

## Sample Prompt / Input
```
I need to wake up at 7:00 AM and want 8 hours of quality sleep.
I currently struggle with falling asleep and often use my phone in bed.
Create an optimized sleep schedule and wind-down routine.
```

## Expected Output Format
```
**Optimized Sleep Schedule**

Target wake time:   7:00 AM
Target sleep time:  10:45 PM  (allows ~15 min to fall asleep)
Wind-down start:    9:30 PM

---
**Wind-Down Routine (90 minutes before bed)**

9:30 PM — Dim lights to 30% brightness; switch devices to night mode
9:45 PM — Last caffeine cutoff was 1:00 PM (8h prior — verify you met this)
10:00 PM — Phone goes on charger OUTSIDE the bedroom
10:10 PM — Light stretching or reading (paper book preferred)
10:30 PM — Bedroom temperature set to 65-68°F (18-20°C)
10:45 PM — Lights out

**Sleep Hygiene Tips:**
1. Keep wake time consistent even on weekends to anchor your circadian rhythm.
2. Avoid alcohol within 3 hours of bedtime — it fragments sleep architecture.
3. Use white noise or earplugs if your environment has intermittent sounds.
4. If not asleep in 20 minutes, get up and do a quiet activity until drowsy.
```

## Tips
- Add `--issues "waking at 3am"` to get targeted middle-of-night advice.
- Specify `--chronotype night-owl` for a realistic gradual shift plan.
- Ask for a weekday vs. weekend schedule if your routine differs.
- Track your actual sleep times for a week before running this to give the model real baseline data.
