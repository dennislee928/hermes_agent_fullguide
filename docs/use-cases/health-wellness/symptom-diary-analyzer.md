# Symptom Diary Analyzer

## Description
Analyze a collection of symptom entries to identify patterns, potential triggers, symptom clusters, and trends over time. Output is a structured report suitable for sharing with a healthcare provider, helping patients communicate their experience more effectively.

## Why Hermes
Pattern recognition in symptom data requires holding multiple data points across time and identifying correlations — a task that benefits from Hermes's reasoning ability. It presents findings neutrally and always recommends professional medical consultation, respecting appropriate AI boundaries in healthcare contexts.

## Quickstart
```bash
python examples/health-wellness/wellness_tools.py symptoms "headache for 3 days, mild fever, fatigue"
```

## Sample Input
```
Day 1: Headache (moderate, 4/10), started after lunch, resolved by evening
Day 2: Headache returned in morning (5/10), fatigue, slight nausea
Day 3: Headache severe (7/10), fever 38.1°C, neck stiffness
Day 4: All symptoms resolved
Sleep: 6 hours each night
Diet: Skipped breakfast days 1-2
Stress: High work deadline days 1-2
```

## Output Format
```
SYMPTOM ANALYSIS REPORT
Period: 4 days | Generated: [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SYMPTOM OVERVIEW
Primary: Headache (progressive, 4/10 → 7/10 over 3 days)
Secondary: Fatigue, nausea, fever (38.1°C), neck stiffness

PATTERN OBSERVATIONS
1. Symptom Progression: Headache worsened consistently over 3 days before resolving — this progressive pattern differs from typical tension headaches that remain stable.
2. Accompanying Fever + Neck Stiffness: The combination of headache, fever, and neck stiffness on Day 3 is a combination that warrants prompt medical evaluation.
3. Potential Triggers Noted: Sleep deprivation (6 hrs/night) and skipped breakfast coincided with symptom onset — these are known headache triggers worth tracking.

WHAT TO TELL YOUR DOCTOR
- Headache progressive over 3 days, reaching 7/10 severity
- Accompanied by fever (38.1°C) and neck stiffness on Day 3
- Associated with fatigue and nausea
- Resolved completely on Day 4
- Possible contributing factors: sleep restriction, meal skipping, high stress

IMPORTANT NOTICE
This analysis is for informational purposes only and is NOT medical advice. The combination of severe headache, fever, and neck stiffness you described should be evaluated by a healthcare provider. If these symptoms recur, seek medical attention promptly.

TRACKING RECOMMENDATION
Continue logging: time of day, severity (1-10), duration, food/sleep, stress level, and any new accompanying symptoms.
```

## Tips
- Log symptoms daily for at least 2 weeks before analyzing for pattern accuracy.
- Include sleep hours, meals, exercise, and stress levels as these often correlate with symptoms.
- Always share the output report with a qualified healthcare provider.
- Use for chronic condition tracking: migraines, IBS, chronic fatigue, arthritis flares.
