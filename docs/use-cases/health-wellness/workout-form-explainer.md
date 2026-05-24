# Workout Form Explainer

## Description
Receive detailed technique instructions for any exercise, including setup, movement cues, common mistakes, muscles worked, modifications for beginners, and progressions for advanced practitioners. Helps prevent injury and maximize the effectiveness of each exercise.

## Why Hermes
Good exercise instruction requires explaining not just what to do but why — which muscles are targeted, why proper alignment protects joints, and how to feel the correct movement. Hermes structures this layered explanation clearly and includes the coaching cues that actually change movement patterns.

## Quickstart
```bash
python examples/health-wellness/mindfulness_tools.py form "barbell squat"
```

## Sample Input
```
Exercise: Romanian Deadlift
Experience level: Intermediate
Equipment: Barbell
Goal: Understand proper technique and common mistakes
```

## Output Format
```
EXERCISE FORM GUIDE: Romanian Deadlift (RDL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRIMARY MUSCLES: Hamstrings, Glutes (gluteus maximus)
SECONDARY MUSCLES: Erector spinae, Adductors, Core (stabilizing)
EQUIPMENT: Barbell (also works with dumbbells)

SETUP
- Stand with feet hip-width apart, toes pointing forward or slightly out
- Hold the barbell with an overhand grip, hands just outside your legs
- Start position: standing tall, barbell at hip level, slight bend in knees

THE MOVEMENT

HINGE PHASE (lowering)
1. Push your hips BACK (not down) — this is a hip hinge, not a squat
2. Maintain a neutral spine — imagine a straight line from tailbone to the back of your skull
3. Lower the bar along your legs (it should graze your shins/quads on the way down)
4. Lower until you feel a strong stretch in the hamstrings — typically bar is at mid-shin level, depending on your flexibility
5. Keep your weight in your heels throughout

RETURN PHASE (rising)
1. Drive your hips FORWARD to return to standing
2. Squeeze glutes at the top
3. Do not hyperextend your lower back at lockout — simply stand tall

KEY COACHING CUES
- "Push the wall behind you with your hips" — best cue for hip hinge
- "Proud chest" — keeps the spine neutral and prevents rounding
- "Bar stays close" — prevents the bar drifting forward, which strains the lower back
- "Feel the hamstrings stretch" — confirms you're hinging rather than squatting

COMMON MISTAKES
1. Rounding the lower back: Usually from excessive range or too much weight. Reduce range until flexibility improves.
2. Bending the knees too much: Turns it into a conventional deadlift. Maintain slight knee bend throughout.
3. Bar drifting forward: Strains lumbar spine. Drag the bar up your legs.
4. Looking up too far: Causes neck compression. Keep neutral neck (eyes tracking the floor 10 feet ahead).

BEGINNER MODIFICATION
Start with dumbbells or a light barbell. Practice the hinge movement without weight first by placing a dowel rod along your spine — it should maintain 3 points of contact (back of head, upper back, tailbone).

PROGRESSION
Once comfortable: Deficit RDL (standing on a plate to increase range of motion), Single-leg RDL (balance and unilateral development).
```

## Tips
- Always describe your current experience level and available equipment for the most relevant guidance.
- For injury history, add `--note "previous lower back injury"` to receive appropriate modifications.
- Video yourself from the side to compare your actual form to the described cues.
- New to a lift? Master the movement pattern with bodyweight before adding load.
