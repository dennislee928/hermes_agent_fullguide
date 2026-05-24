# Salary Negotiation Coach

## Description
Prepare for salary negotiations with a customized strategy covering your market value research framework, specific counter-offer language, objection handling scripts, and timing guidance. Hermes role-plays the negotiation to help you practice.

## Why Hermes
Salary negotiation is a high-stakes conversation where specific language and sequencing significantly affect outcomes. Hermes generates realistic dialogue, identifies common negotiator tactics, and provides confident, professional counter-scripts rather than vague advice to "know your worth."

## Quickstart
```bash
python examples/finance/financial_advisor.py negotiate --role "Software Engineer" --offer 95000 --target 110000 --location "San Francisco"
```

## Sample Input
```
Role: Marketing Manager
Current offer: $78,000
Target: $88,000
Experience: 7 years
Location: Chicago
Competing offer: None
```

## Output Format
```
SALARY NEGOTIATION STRATEGY
Role: Marketing Manager | Offer: $78,000 | Target: $88,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MARKET CONTEXT
Marketing Manager median in Chicago (2024): $82,000-$95,000 (Glassdoor/BLS data ranges).
Your target of $88,000 is within the market range and reasonable to request with 7 years experience.

NEGOTIATION STRATEGY
Gap to close: $10,000 (12.8% increase) — negotiable but will require a confident, well-framed ask.
Recommended ask: Counter at $91,000-$93,000 to leave room to meet in the middle at ~$88,000.

STEP-BY-STEP SCRIPT

STEP 1 — Express enthusiasm (don't lead with money)
"Thank you so much for the offer. I'm genuinely excited about this role and the team — the [specific thing about the role] really resonates with what I want to work on. I do want to discuss the compensation."

STEP 2 — Make the counter confidently, with a number, not a range
"Based on my 7 years in marketing, my track record of [specific achievement — e.g., 'growing organic traffic 150% in my last role'], and the Chicago market rate for this level, I was hoping we could get to $92,000."

Why a specific number: Ranges signal uncertainty. A specific number anchors the conversation higher.

STEP 3 — Then be quiet
After stating your number, stop talking. Silence is pressure on the employer, not you. Let them respond.

HANDLING COMMON OBJECTIONS

If they say: "That's at the top of our budget range."
You say: "I understand budget constraints are real. Is there flexibility on other components — signing bonus, additional PTO, or an earlier performance review at 6 months rather than 12?"

If they say: "We feel the offer is competitive for the role."
You say: "I appreciate that, and I've done my research on Chicago market rates for this level. My experience with [specific skills] typically commands $88,000-$93,000. Can we find a path to $90,000?"

If they say: "We need a decision by Friday."
You say: "I want to make this work — can we resolve the compensation question today so I can commit enthusiastically?"

TOTAL COMPENSATION TO EVALUATE
If base salary is immovable, ask about:
- Signing bonus: "Could a $5,000 signing bonus bridge the gap?"
- Additional PTO: 2-3 extra days has real monetary value
- Remote work flexibility: reduces commute cost
- Earlier review cycle: get to your target through a faster raise

MINDSET NOTE
Negotiating does NOT put offers at risk if done professionally. Research shows 85%+ of employers expect negotiation. A professional, evidence-based counter actually signals the confidence employers want in a manager.
```

## Tips
- Always negotiate — research consistently shows most employers expect it and offers are rarely rescinded.
- Practice the opening line out loud before the call — confidence in delivery matters.
- Use `--role-play` to have Hermes simulate the hiring manager's responses and practice your replies.
- If you have a competing offer, mention it — it shifts the entire negotiation dynamic.
