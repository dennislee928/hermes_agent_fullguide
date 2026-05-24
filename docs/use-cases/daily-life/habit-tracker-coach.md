# Habit Tracker Coach

## Description
Design a personalized habit-building plan for up to 5 habits simultaneously, using proven behavioral science principles. Includes implementation intentions, habit stacking strategies, obstacle anticipation, and a progress tracking structure.

## Why Hermes for This
Hermes understands habit formation psychology (cue-routine-reward loops, identity-based habits, minimum viable habits) and can apply these principles conversationally to your specific life context and obstacles.

## Quickstart
```bash
cd examples/daily-life
python habits_and_budget.py habits --habits "daily exercise, reading 20 min, no phone before bed" --duration 30
python habits_and_budget.py habits --habit "meditate 10 min daily" --obstacle "forget and feel too tired"
```

## Sample Prompt / Input
```
I want to build these 3 habits over the next 30 days:
1. Exercise 30 minutes daily
2. Read for 20 minutes before bed
3. No phone for the first 30 minutes after waking up

I've tried and failed at all three before. Main obstacles: busy evenings, always reaching for my phone automatically.
```

## Expected Output Format
```
**30-Day Habit Plan — 3 Habits**
Philosophy: Start smaller than you think you need to; build identity before intensity.

---
**Habit 1: Daily Exercise (30 min)**

*Why you've failed before:* "Busy evenings" = decision fatigue + energy depletion.

*New approach:*
- **Minimum viable habit:** 10 minutes of movement (not 30). On busy days, 10 is enough.
  When you have energy, do more — but never skip the 10.
- **Implementation intention:** "When I wake up and finish my no-phone 30 minutes, I will put on workout clothes."
- **Habit stack:** Morning no-phone → workout clothes → 10-30 min movement
- **Cue:** Workout clothes laid out the night before (visible trigger)

*Week 1 target:* 10-min walk or home workout daily
*Week 2-3:* Build to 20 min
*Week 4:* Full 30-min sessions

---
**Habit 2: Read 20 Minutes Before Bed**

*Why you've failed before:* Phone is right there and provides instant dopamine.

*New approach:*
- Phone goes on charger in another room at 9:30 PM (removes the competition)
- Book lives on your nightstand or pillow (visible, zero friction)
- **Minimum viable habit:** Read one page. Truly — one page.
- **Implementation intention:** "After I brush my teeth, I will pick up my book and read."

---
**Habit 3: No Phone for First 30 Minutes**

*Why you've failed before:* Automatic behavior — you're checking before you're conscious of it.

*New approach:*
- Charge phone in the kitchen or bathroom — NOT the bedroom
- Replace the morning phone grab with a tactile substitute: glass of water on nightstand
- **Implementation intention:** "When my alarm goes off, I will drink my water and not touch my phone until I've done X."
- First replacement activity: 2-minute journaling OR reading one page from last night's book

---
**30-Day Tracking Structure**

| Week | Exercise Target | Reading Target | No-Phone Streak Goal |
|------|-----------------|----------------|----------------------|
| 1    | 7/7 × 10 min    | 7/7 × 5 min    | 5/7 days             |
| 2    | 7/7 × 15 min    | 7/7 × 10 min   | 6/7 days             |
| 3    | 7/7 × 20 min    | 7/7 × 15 min   | 7/7 days             |
| 4    | 7/7 × 30 min    | 7/7 × 20 min   | 7/7 days             |

**Never miss twice:** Missing one day is an accident. Missing two is the start of a new habit (the wrong one). If you miss, the next day is non-negotiable.

**Identity shift:** Instead of "I'm trying to exercise," say "I'm someone who moves every day." Behavior follows identity.
```

## Tips
- Start with 1-2 habits if you're new to habit tracking — 3+ simultaneously is ambitious.
- Describe past failure modes specifically so the model can address the root cause.
- Ask for a weekly check-in prompt template to assess progress at the end of each week.
- Use `--duration 21` for a shorter sprint or `--duration 90` for deep habit formation.
