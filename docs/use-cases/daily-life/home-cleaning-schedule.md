# Home Cleaning Schedule

## Description
Generate a realistic, sustainable cleaning schedule for your home based on the number of rooms, household size, and preferred cleaning frequency. Tasks are divided into daily, weekly, and monthly categories to prevent overwhelm.

## Why Hermes for This
Hermes understands how to break large recurring tasks into manageable chunks and can reason about room-specific cleaning priorities. It produces human-friendly schedules rather than generic checklists.

## Quickstart
```bash
cd examples/daily-life
python home_and_lifestyle.py cleaning-schedule --rooms 4 --frequency weekly
python home_and_lifestyle.py cleaning-schedule --rooms 6 --people 4 --pets --frequency biweekly
```

## Sample Prompt / Input
```
Create a home cleaning schedule for a 4-room apartment (living room, kitchen, bathroom, bedroom).
2 adults, no pets. I prefer to do a big clean on Saturdays and light maintenance during the week.
```

## Expected Output Format
```
**Home Cleaning Schedule — 4-Room Apartment**
Household: 2 adults | Big clean: Saturday | Light maintenance: Daily

---
**Daily (5-10 min)**
- [ ] Wipe kitchen counters and stovetop after cooking
- [ ] Wash dishes / load dishwasher
- [ ] Quick bathroom sink wipe
- [ ] Pick up clutter before bed

**Weekly — Saturday Deep Clean (2-3 hours)**

*Kitchen (45 min)*
- [ ] Clean inside microwave and oven exterior
- [ ] Scrub sink and faucet
- [ ] Mop floor
- [ ] Wipe cabinet fronts

*Bathroom (30 min)*
- [ ] Scrub toilet, tub/shower, and sink
- [ ] Replace towels; wash used ones
- [ ] Mop floor

*Living Room (30 min)*
- [ ] Vacuum sofa and rugs
- [ ] Dust surfaces and electronics
- [ ] Clean glass surfaces

*Bedroom (20 min)*
- [ ] Change bed sheets
- [ ] Vacuum floor
- [ ] Dust nightstands and surfaces

**Monthly (1 hour)**
- [ ] Clean inside refrigerator
- [ ] Wipe baseboards
- [ ] Clean windows (interior)
- [ ] Descale kettle and coffee maker
```

## Tips
- Add `--pets` to include pet-specific tasks like vacuuming hair off furniture daily.
- Use `--people 4` for busier households — the model will increase daily task frequency.
- Ask for a rotating schedule if some tasks feel overwhelming all on one day.
- Request a printable checklist format with `--format checklist`.
