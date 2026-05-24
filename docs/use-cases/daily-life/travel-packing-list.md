# Travel Packing List

## Description
Generate a comprehensive, trip-specific packing list based on destination, duration, activities planned, and weather. Items are organized by category (clothing, toiletries, documents, electronics) and marked as essential vs. optional.

## Why Hermes for This
Hermes can reason about trip-specific needs — beach vs. hiking vs. business travel — and tailor packing lists accordingly rather than producing a generic template. It also catches commonly forgotten items.

## Quickstart
```bash
cd examples/daily-life
python travel_and_social.py packing --destination "Tokyo" --days 10 --activities "sightseeing,hiking,business dinner"
python travel_and_social.py packing --destination "beach resort" --days 5 --weather "hot and humid"
```

## Sample Prompt / Input
```
I'm traveling to Tokyo for 10 days in October.
Activities: sightseeing, one business dinner, day hike on Mount Takao, lots of walking.
Weather: 15-22°C (59-72°F), some rain expected.
I carry-on only. Create a complete packing list.
```

## Expected Output Format
```
**Packing List — Tokyo, 10 Days (Carry-on Only)**
Season: October | Activities: Sightseeing, Business dinner, Hiking, Walking

---
**Clothing (carry-on capsule)**
Essential:
- [ ] 4 × T-shirts or light tops (mix casual/smart)
- [ ] 2 × long-sleeve shirts (layering for cool evenings)
- [ ] 1 × smart shirt/blouse (business dinner)
- [ ] 2 × trousers/pants (1 casual, 1 smart-casual)
- [ ] 1 × shorts or light skirt
- [ ] 1 × light rain jacket / packable windbreaker ★ (rain expected)
- [ ] 5 × underwear + 5 × socks
- [ ] 1 × comfortable walking shoes (broken in)
- [ ] 1 × smart shoes (business dinner)
- [ ] 1 × packable day bag / daypack (for hiking and sightseeing)

**Toiletries** (TSA-compliant sizes if flying)
- [ ] Toothbrush, toothpaste, floss
- [ ] Shampoo, conditioner (or plan to buy at a 100-yen shop in Tokyo)
- [ ] Deodorant, skincare basics
- [ ] Sunscreen SPF 30+
- [ ] Small umbrella or packable rain poncho

**Documents & Money**
- [ ] Passport (valid 6+ months beyond travel dates)
- [ ] Travel insurance details (printed + digital)
- [ ] IC card / Suica card (load at airport for trains)
- [ ] Some cash yen — many smaller venues are cash-only
- [ ] Hotel confirmation printouts

**Electronics**
- [ ] Phone + charger
- [ ] Universal power adapter (Japan uses Type A; same as US — only needed for EU/UK travelers)
- [ ] Portable battery pack
- [ ] Earphones / earbuds

**Japan-Specific Tips:**
- Bring a small towel — many public restrooms don't have hand dryers or paper towels.
- Pack light: lockers at attractions have size limits.
- Laundromats are cheap and easy — pack for 6 days and wash mid-trip.
```

## Tips
- Specify "carry-on only" to receive a capsule wardrobe approach with re-wear planning.
- Add `--activities hiking` to ensure gear like moisture-wicking socks and trekking poles are included.
- Mention any medications you take — the model will remind you of prescription quantities and documentation.
- Ask for a "day before departure" checklist to catch last-minute items.
