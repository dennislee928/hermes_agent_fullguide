# Health & Wellness Examples

Hermes-powered command-line tools for health information, mindfulness, and wellness. All scripts connect to a local Ollama instance running the Hermes-3 model.

**IMPORTANT: All output is for informational and educational purposes only. Nothing in these tools constitutes medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical decisions.**

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) running locally (`ollama serve`)
- The Hermes model pulled: `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`

## Installation

```bash
pip install -r requirements.txt
```

## Scripts

### wellness_tools.py

Symptom diary analyzer, medication interaction checker, nutrition label decoder, and allergy recipe adapter.

```bash
# Analyze symptom patterns
python wellness_tools.py symptoms "headache for 3 days, mild fever, fatigue"
python wellness_tools.py symptoms --file symptom_diary.txt

# Check medication interactions (educational only — consult your pharmacist)
python wellness_tools.py medications "ibuprofen, warfarin"

# Decode a nutrition label
python wellness_tools.py nutrition --label "Calories 250, Fat 12g, Sodium 480mg, Sugar 8g"
python wellness_tools.py nutrition --file nutrition_label.txt --product "Granola Bar"

# Adapt a recipe for allergens
python wellness_tools.py adapt-recipe --file pasta.txt --avoid "gluten, dairy"
python wellness_tools.py adapt-recipe --recipe "Chicken Alfredo" --avoid "dairy" --serious
```

### mindfulness_tools.py

Mental health journaling, guided meditation, hydration planner, ergonomics advisor, first aid guide, and workout form explainer.

```bash
# Guided journaling session
python mindfulness_tools.py journal --mood "anxious about upcoming job interview"

# Generate a meditation script
python mindfulness_tools.py meditate --duration 10 --goal "reduce anxiety" --level beginner
python mindfulness_tools.py meditate --duration 5 --technique "4-7-8 breathing"

# Personalized hydration plan
python mindfulness_tools.py hydration --weight 70 --unit kg --activity moderate --climate hot

# Ergonomics assessment
python mindfulness_tools.py ergonomics --height "5ft 9in" --pain "lower back, neck" --setup "laptop, external monitor, office chair"

# First aid instructions
python mindfulness_tools.py first-aid "deep cut on hand"
python mindfulness_tools.py first-aid "child has a burn"

# Exercise form guide
python mindfulness_tools.py form "barbell squat"
python mindfulness_tools.py form "Romanian Deadlift" --level intermediate
```

## Safety Notes

- The symptom analyzer and medication checker are for **educational awareness only** — always verify with your doctor or pharmacist.
- First aid information should supplement, not replace, formal first aid training.
- In any medical emergency, call your local emergency number (911/999/112) immediately.
