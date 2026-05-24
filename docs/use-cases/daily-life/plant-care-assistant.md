# Plant Care Assistant

## Description
Get tailored care instructions for any houseplant or garden plant, including watering frequency, light requirements, soil preferences, fertilizing schedule, and common problem diagnosis. Advice adapts to your climate and home environment.

## Why Hermes for This
Hermes has extensive knowledge of plant species and can give nuanced, context-aware advice — distinguishing, for example, between care in a dry apartment versus a humid greenhouse — without requiring a specialized botanical database.

## Quickstart
```bash
cd examples/daily-life
python home_and_lifestyle.py plant "monstera"
python home_and_lifestyle.py plant "fiddle leaf fig" --environment "low light apartment, dry climate"
python home_and_lifestyle.py plant "tomatoes" --type outdoor --zone 7
```

## Sample Prompt / Input
```
I have a Monstera deliciosa in a north-facing apartment window in a dry climate (humidity ~30%).
The pot is 10 inches, well-draining soil. Give me a complete care guide.
```

## Expected Output Format
```
**Monstera Deliciosa Care Guide**
Environment: North-facing, low-medium light | Humidity: ~30% (low) | Pot: 10-inch, well-draining

---
**Light**
Monsteras prefer bright indirect light. A north-facing window in most climates provides
medium-low light — your plant will grow slowly but healthily. Consider a grow light 2-4 hours
per day in winter if you notice very slow growth or small new leaves.

**Watering**
- Frequency: Every 10-14 days in winter; every 7-10 days in summer
- Method: Water deeply until it drains from the bottom; empty the saucer after 30 min
- Check: Insert finger 2 inches into soil — water only when the top 2 inches are dry

**Humidity**
At 30% your Monstera will survive but may develop brown leaf edges. Recommended actions:
1. Place a pebble tray with water beneath the pot (do not let roots sit in water)
2. Group plants together to create a microclimate
3. Run a small humidifier nearby (target 50-60%)

**Fertilizing**
- Growing season (March-September): Balanced liquid fertilizer (10-10-10) diluted to half strength, once per month
- Dormant season (October-February): No fertilizing needed

**Common Problems**
| Symptom                  | Likely Cause              | Fix                        |
|--------------------------|---------------------------|----------------------------|
| Yellow leaves            | Overwatering              | Let soil dry out; improve drainage |
| Brown crispy leaf edges  | Low humidity / underwater | Increase humidity; check watering |
| No new leaves (summer)   | Too little light           | Move closer to window or add grow light |
| Leggy / small leaves     | Low light                 | Brighter location          |

**Repotting:** Every 1-2 years in spring, when roots circle the bottom of the pot.
```

## Tips
- Describe any current symptoms (yellowing, drooping, brown spots) for instant diagnosis.
- Mention your local climate zone for outdoor plants to get seasonal timing advice.
- Ask for a propagation guide by appending "and how to propagate" to your query.
- Use the exact Latin name for rare plants to get the most accurate advice.
