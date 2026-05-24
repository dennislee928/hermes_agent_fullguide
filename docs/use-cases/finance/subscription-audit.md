# Subscription Audit

## Description
List your active subscriptions and receive a structured audit: usage-value assessment, identification of redundant services, a priority ranking for cancellation, negotiation tips, and an estimated annual savings if recommended cancellations are made.

## Why Hermes
Subscription audits require applying value-for-money reasoning to services with different utility levels, identifying overlaps, and ranking by cancellation impact. Hermes provides direct, opinionated recommendations rather than just listing the subscriptions back.

## Quickstart
```bash
python examples/finance/budget_tools.py subscriptions --list "Netflix:15,Spotify:10,Gym:40,iCloud:3"
```

## Sample Input
```
Netflix: $15.49/month
Disney+: $13.99/month
Hulu: $17.99/month
HBO Max: $15.99/month
Amazon Prime: $14.99/month
Spotify: $10.99/month
YouTube Premium: $13.99/month
iCloud 200GB: $2.99/month
Google One 100GB: $1.99/month
Gym membership: $45/month
Unused fitness app: $9.99/month
Adobe Creative Cloud: $54.99/month
Grammarly Premium: $30/month
LinkedIn Premium: $39.99/month
```

## Output Format
```
SUBSCRIPTION AUDIT
Total monthly spend: $288.37 | Annual: $3,460.44
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IMMEDIATE CANCELLATIONS (Clear redundancies)

1. Google One 100GB ($1.99/mo) — You have iCloud. Using two cloud storage subscriptions suggests only one is actually needed. Cancel unless actively using both. Annual savings: $23.88.

2. Unused Fitness App ($9.99/mo) — Self-described as unused. Cancel immediately. Annual savings: $119.88.

STREAMING CONSOLIDATION (You have 5 streaming services)

Monthly cost: $78.45 for streaming alone = $941.40/year
Assessment: Unless you actively use all 5, this is substantial. A household typically exhausts 2-3 services.

Recommended: Keep 2-3, rotate the others every 6-12 months (binge the content you want, then cancel and switch).

Priority to keep:
1. Amazon Prime ($14.99) — dual value: shipping + video; hard to replace
2. Netflix ($15.49) — largest original content library
3. One of: Disney+, Hulu, or HBO Max based on your actual viewing

Priority to cancel first:
- Hulu ($17.99) — most expensive of the three
- Consider: Disney+ and HBO Max rotate every 6 months

Potential streaming savings: $29-$48/month ($348-$576/year)

EVALUATE CAREFULLY

LinkedIn Premium ($39.99/mo, $479.88/year): High cost, high variability in value. Valuable if actively job searching or in sales; poor value otherwise. Evaluate honestly — if not actively using InMail or viewing profile viewers, cancel.

YouTube Premium ($13.99/mo): If you watch YouTube daily, the ad-free experience may be worth it. If Spotify already covers your music needs, evaluate whether you use YouTube Music.

RETAIN AS-IS
- Spotify ($10.99) — Reasonable for daily music use
- iCloud 200GB ($2.99) — Low cost, high utility
- Adobe Creative Cloud ($54.99) — Professional tool; cancel only if not regularly using
- Gym membership ($45) — Retain if used; cancel if <2x/week (cost per visit >$5.62)
- Grammarly Premium ($30) — Evaluate against free tier; significant cost for a writing tool

SUMMARY
Definite savings (cancel unused + duplicate): $143.76/year
Potential streaming consolidation: $348-$576/year
Total potential savings: $491-$720/year

ACTION PLAN
Week 1: Cancel Google One + unused fitness app (5 minutes)
Week 2: Decide on LinkedIn Premium
Week 3: Pick 2-3 streaming services to keep; cancel the rest
```

## Tips
- Include the monthly cost for each subscription — the annual totals are often shocking.
- Check your credit card statements for subscriptions you've forgotten about.
- For streaming: use a service for 1-2 months, watch everything you want, then rotate to the next.
- Many services offer cancellation retention offers — always click "continue cancellation" to see if a discount is offered.
