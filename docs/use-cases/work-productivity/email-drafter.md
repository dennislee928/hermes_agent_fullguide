# Email Drafter

## Description
Email Drafter uses Hermes to compose professional, context-aware emails from a brief summary of your intent. It handles tone calibration, subject line generation, and appropriate sign-offs so you can send polished emails in seconds rather than minutes.

## Why Hermes
Hermes excels at following nuanced instruction sets and adapting register and vocabulary to a specified tone — making it reliable for producing emails that sound like you, not like a template. Its instruction-following fidelity means it respects constraints like word limits, recipient context, and formality level without drift.

## Quickstart
```bash
python examples/work-productivity/email_and_comms.py draft \
  --to "client" \
  --subject "project update" \
  --tone professional \
  --context "The project is on track, milestones met, next phase starts Monday."
```

## Sample Input
```
Recipient: Sarah (direct manager)
Subject: Requesting Friday afternoon off
Tone: friendly but professional
Context: I have a medical appointment that can only be scheduled at 2pm Friday.
         My current sprint tasks will be completed by Thursday EOD.
```

## Expected Output Format
```
Subject: Requesting Friday Afternoon Off — [Your Name]

Hi Sarah,

I hope your week is going well. I wanted to reach out to let you know I have a
medical appointment scheduled for 2:00 PM this Friday that I was unable to
reschedule. I plan to have all of my current sprint tasks wrapped up by
Thursday end of day, so there should be no impact to the team.

Would it be alright if I took Friday afternoon off? Happy to discuss if needed.

Thanks so much,
[Your Name]
```

## Tips
- Always include `--context` with key facts; the more specific you are, the less generic the output.
- Use `--tone` values like `formal`, `friendly`, `assertive`, `empathetic`, or `concise`.
- For reply chains, paste the original email into `--context` so Hermes can reference it naturally.
- Add `--length short` to request a 3-sentence version when appropriate.
