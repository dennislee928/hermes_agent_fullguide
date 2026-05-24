# Ergonomics Advisor

## Description
Receive a personalized ergonomics assessment and setup guide for your workstation, including monitor placement, chair adjustments, keyboard/mouse positioning, lighting, and break schedules. Also provides targeted stretches and micro-exercises for common pain areas caused by prolonged sitting.

## Why Hermes
Ergonomics guidance requires integrating multiple variables (height, equipment type, pain locations, work duration) into a coherent setup recommendation. Hermes produces actionable, specific guidance rather than generic "sit up straight" advice, and can address the interplay between equipment setup and musculoskeletal discomfort.

## Quickstart
```bash
python examples/health-wellness/mindfulness_tools.py ergonomics --height "5ft 9in" --pain "lower back, neck" --setup "laptop, external monitor, office chair"
```

## Sample Input
```
Height: 5'9" (175 cm)
Equipment: Laptop on desk, no external monitor, built-in keyboard, wireless mouse
Work duration: 8+ hours/day
Pain areas: Neck (right side), upper back, wrist (right)
Chair: Adjustable office chair with armrests
```

## Output Format
```
ERGONOMICS ASSESSMENT & SETUP GUIDE
Profile: 5'9" | Laptop-primary | 8+ hrs/day
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRIORITY ISSUES IDENTIFIED
Your setup suggests classic laptop-only posture: screen too low → forward head → neck strain. Combined with extended mouse use, this explains both your neck (right) and wrist pain.

IMMEDIATE FIXES (High Impact)
1. LAPTOP ELEVATION (Most Important)
   Raise your laptop screen so the top of the screen is at or slightly below eye level.
   Use: A laptop stand, monitor riser, or even a stack of books — height should be approximately 25-30cm (10-12") above desk.
   Why: This eliminates the 30-45° downward head tilt that compresses your cervical spine.

2. EXTERNAL KEYBOARD & MOUSE
   With your screen elevated, you'll need a separate keyboard and mouse.
   Keyboard placement: Elbows at ~90-110°, wrists neutral (not bent up or down)
   Mouse: Keep it close — reaching forward strains your right shoulder and wrist.

3. CHAIR HEIGHT
   Set chair so your feet are flat on the floor and thighs are parallel to the ground.
   Your chair height: approximately 43-46 cm (17-18") seat height for your height.
   Lumbar support: Position the lumbar pad to support the inward curve of your lower back.

4. MONITOR DISTANCE
   Screen should be approximately 50-70 cm (20-27") from your eyes — roughly arm's length.

TARGETED STRETCHES FOR YOUR PAIN AREAS

Neck (Right Side) — Do every 60-90 minutes:
• Lateral neck stretch: Tilt left ear to left shoulder, hold 20-30 seconds. Gentle right-hand weight adds depth.
• Chin tucks: Gently pull chin straight back (creating a "double chin"), hold 5 seconds, repeat 10 times.

Wrist (Right) — Do every hour:
• Prayer stretch: Palms together, press down gently until wrist stretch felt, hold 20 seconds.
• Wrist circles: 10 slow circles each direction.

BREAK SCHEDULE
Every 30 minutes: 20-20-20 rule — look 20 feet away for 20 seconds.
Every 60 minutes: Stand, walk for 2 minutes, perform neck and wrist stretches.
Every 2 hours: 5-minute movement break away from the desk.
```

## Tips
- Use `--setup` to specify your exact equipment for the most targeted advice.
- Invest in a laptop stand + external keyboard/mouse as the highest-ROI ergonomic purchase.
- If pain is acute or persistent, see a physiotherapist — ergonomics prevents but doesn't treat existing injuries.
- Re-evaluate setup when you change chairs, desks, or screen sizes.
