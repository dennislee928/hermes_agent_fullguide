# Medication Interaction Checker

## Description
Provide a list of medications and receive an overview of known or potential interactions between them, including the nature of the interaction, severity classification, and recommendations for discussing with a pharmacist or physician.

## Why Hermes
Medication interactions involve complex biochemical relationships that Hermes can summarize from its training data. Critically, Hermes is calibrated to present this information as educational context rather than medical advice, consistently directing users to verify with a pharmacist — the appropriate professional for drug interaction counseling.

## Quickstart
```bash
python examples/health-wellness/wellness_tools.py medications "ibuprofen, warfarin"
```

## Sample Input
```
Medications: metformin, lisinopril, aspirin (81mg), omeprazole, vitamin D supplement
```

## Output Format
```
MEDICATION INTERACTION OVERVIEW
Medications reviewed: metformin, lisinopril, aspirin (81mg), omeprazole, vitamin D
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INTERACTION SUMMARY
2 interactions of note identified. No high-severity interactions found in this combination.

INTERACTION 1: Metformin + Omeprazole
Severity: Mild
Mechanism: Omeprazole may slightly increase metformin blood levels by affecting renal transporters (OCT2).
Clinical significance: Generally not clinically significant at typical doses. Some clinicians monitor blood glucose more closely.
Action: Mention this combination to your prescriber. No change is typically required but awareness is warranted.

INTERACTION 2: Lisinopril + Aspirin
Severity: Mild-Moderate
Mechanism: NSAIDs (including aspirin) can reduce the antihypertensive effectiveness of ACE inhibitors like lisinopril by promoting sodium retention and vasoconstriction.
Clinical significance: Low-dose aspirin (81mg) carries lower risk than full-dose NSAIDs. Effect may be minimal at this dose but worth monitoring.
Action: Ensure your cardiologist/prescriber is aware you are taking both. Blood pressure should be monitored.

NO INTERACTIONS NOTED BETWEEN
- Metformin + Lisinopril: No significant interaction
- Metformin + Aspirin: No significant interaction
- Metformin + Vitamin D: No significant interaction
- Lisinopril + Vitamin D: No significant interaction

IMPORTANT DISCLAIMER
This overview is for educational purposes only and is NOT a substitute for professional pharmaceutical review. Your pharmacist has access to your complete medication list and is the best resource for a comprehensive interaction check. Please review this list with your pharmacist at your next visit.
```

## Tips
- Include supplements, vitamins, and over-the-counter medications — these are frequently overlooked sources of interactions.
- Use this as preparation for a pharmacist consultation, not as a replacement for one.
- For newly prescribed medications, always verify interactions with the dispensing pharmacist.
- This tool is most valuable for understanding the nature of interactions your pharmacist has flagged.
