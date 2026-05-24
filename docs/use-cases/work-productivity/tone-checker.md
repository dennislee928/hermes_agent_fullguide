# Tone Checker

## Description
Tone Checker analyzes written text and reports on its tone profile, flagging phrases that may read as passive-aggressive, too casual, overly formal, or unintentionally cold. It suggests specific rewrites to align the text with the intended register.

## Why Hermes
Hermes is sensitive to subtle register and connotation differences — distinguishing "as per my last email" (passive-aggressive) from "as I mentioned" (neutral) — and produces specific, phrase-level rewrites rather than vague style advice.

## Quickstart
```bash
python examples/work-productivity/email_and_comms.py tone-check \
  --file email.txt \
  --intended-tone professional-friendly
```

## Sample Input
```
Text to check:
"Per my previous message, the deadline was clearly stated as Friday.
I'm not sure why this wasn't completed. Please advise on when
we can expect delivery. Going forward, let's make sure
communications are timely."

Intended tone: Firm but collaborative
```

## Expected Output Format
```
Tone Analysis

Detected Tone: Passive-aggressive / Critical
Intended Tone: Firm but collaborative
Match: POOR

Flagged Phrases:
1. "Per my previous message" — reads as pointed and accusatory.
   Rewrite: "As we discussed last week" or "Following up on Friday's message"

2. "clearly stated" — implies the recipient was careless or inattentive.
   Rewrite: Remove "clearly" — "the deadline was Friday"

3. "I'm not sure why this wasn't completed" — rhetorical, not a genuine question.
   Rewrite: "Could you share what got in the way? I want to help unblock this."

4. "Please advise" — corporate filler that reads as cold or sarcastic in context.
   Rewrite: "What's the updated timeline on your end?"

5. "Going forward, let's make sure..." — sounds like a reprimand.
   Rewrite: "To keep things on track, would a shared deadline tracker help?"

Revised Version:
Following up on Friday's message — the delivery was due that day and we haven't
received it yet. Could you share what caused the delay? Happy to help unblock
anything. What timeline works for you now?
```

## Tips
- Use `--intended-tone` values like `warm`, `authoritative`, `empathetic`, `neutral`, `concise`.
- Works well on Slack messages, emails, and performance review text.
- Combine with Email Drafter: draft first, tone-check second.
- Use `--audience executive` to flag phrases that may be too casual for senior stakeholders.
