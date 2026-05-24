# Pet Care Advisor

## Description
Receive comprehensive, breed- and age-specific care advice for your pet, covering nutrition, exercise, grooming, health screening schedules, and behavioral tips. Guidance adapts to the pet's life stage (puppy/kitten, adult, senior).

## Why Hermes for This
Hermes combines breed-specific knowledge with life-stage reasoning to produce advice that is both specific and empathetic. It clearly flags when veterinary consultation is required rather than offering medical diagnoses.

## Quickstart
```bash
cd examples/daily-life
python home_and_lifestyle.py pet "golden retriever 3 years"
python home_and_lifestyle.py pet "persian cat 10 years" --issue "not eating well"
python home_and_lifestyle.py pet "beagle puppy 4 months"
```

## Sample Prompt / Input
```
I have a 3-year-old male Golden Retriever named Max. He's healthy and neutered.
Give me a comprehensive care overview covering diet, exercise, grooming, and vet visits.
```

## Expected Output Format
```
**Golden Retriever Care Guide — Adult (3 years)**
Name: Max | Sex: Neutered male | Life stage: Prime adult

---
**Diet**
- Recommended: High-quality large-breed adult dry kibble, 3-4 cups/day split into 2 meals
- Look for: Protein as first ingredient; no excessive fillers; AAFCO "complete and balanced" label
- Avoid: Free-feeding (Goldens are prone to obesity); grapes, raisins, xylitol, onions
- Supplements: Omega-3 fish oil (1000 mg/day) supports coat and joint health

**Exercise**
Goldens need 1-2 hours of physical activity daily.
- Morning: 30-min brisk walk or fetch session
- Evening: 30-min walk + mental enrichment (puzzle feeder, training session)
- Weekly: Off-leash run, swimming (a Golden favorite), or hiking

**Grooming**
| Task             | Frequency          | Notes                            |
|------------------|--------------------|----------------------------------|
| Brushing         | 3-4× per week      | Daily during spring/fall shedding |
| Bathing          | Every 6-8 weeks    | Use dog-specific shampoo         |
| Nail trimming    | Every 3-4 weeks    | Clip when you hear clicking on hard floors |
| Ear cleaning     | Weekly             | Goldens are prone to ear infections |
| Teeth brushing   | Daily (ideally)    | Dental chews as minimum backup   |

**Vet Schedule**
- Annual wellness exam + vaccines (rabies, DHPP, bordetella)
- Heartworm test + year-round prevention medication
- Flea/tick prevention (monthly topical or chewable)
- Dental cleaning: every 1-2 years professionally

**Health Watch (Golden-specific)**
- Hip and elbow dysplasia: maintain healthy weight; watch for limping
- Cancer screening: Goldens have elevated cancer risk; discuss with vet at age 6+
- Hypothyroidism: watch for unexplained weight gain, lethargy

> Always consult your veterinarian before changing diet, medications, or if you notice sudden behavioral or physical changes.
```

## Tips
- Include the pet's current health issues or medications for targeted advice.
- Ask for a vaccination schedule by life stage if you're a new owner.
- Use the `--issue` flag to focus on a specific concern like anxiety, shedding, or dental health.
- The model will clearly state "consult your vet" for anything requiring diagnosis.
