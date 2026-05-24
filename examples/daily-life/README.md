# Daily Life Examples — Hermes Agent Guide

Five Python scripts covering 20 daily-life use cases, all powered by the
Hermes-3-Llama-3.1-8B model running locally via Ollama.

---

## Prerequisites

### 1. Install Ollama
```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows: download the installer from https://ollama.com
```

### 2. Pull the Hermes model
```bash
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

### 3. Start Ollama
```bash
ollama serve
```
Ollama must be running at `http://localhost:11434` before running any script.

### 4. Install Python dependencies
```bash
pip install -r requirements.txt
```

---

## Scripts & Commands

### `food_and_nutrition.py`
Covers: recipe generation, meal planning, grocery list optimization, nutrition tracking.

```bash
# Generate a recipe from whatever you have on hand
python food_and_nutrition.py recipe "chicken, rice, tomatoes, garlic, olive oil"

# With dietary constraint
python food_and_nutrition.py recipe "eggs, spinach, feta, tomatoes" --diet vegetarian

# 7-day vegetarian meal plan
python food_and_nutrition.py meal-plan --days 7 --diet vegetarian

# Keto meal plan targeting 1800 calories
python food_and_nutrition.py meal-plan --days 5 --diet keto --calories 1800

# Build a grocery list from planned meals
python food_and_nutrition.py grocery --meals "pasta bolognese, caesar salad, vegetable soup"

# Scale to 4 servings per meal
python food_and_nutrition.py grocery --meals "tacos,stir fry,omelette" --servings 4

# Analyze a meal's nutritional content
python food_and_nutrition.py nutrition "200g chicken breast, 100g brown rice, 1 cup broccoli"

# With a specific goal
python food_and_nutrition.py nutrition "2 eggs, 2 slices toast, 1 cup OJ" --goal weight-loss
```

---

### `health_and_fitness.py`
Covers: workout planning, sleep schedule optimization, morning routine design.

```bash
# 4-day fat loss workout plan
python health_and_fitness.py workout --goal "lose weight" --days 4

# Muscle-building plan with equipment
python health_and_fitness.py workout --goal "build muscle" --days 5 \
    --equipment "barbell,dumbbells,pull-up bar" --level intermediate

# Beginner plan avoiding lower back
python health_and_fitness.py workout --goal "general fitness" --days 3 \
    --level beginner --avoid "lower back exercises"

# Optimize sleep for a 7 AM wake time
python health_and_fitness.py sleep --wake "7am" --bedtime-goal "8h"

# With known sleep issues
python health_and_fitness.py sleep --wake "6:30am" --bedtime-goal "7.5h" \
    --issues "trouble falling asleep, phone use in bed"

# 60-minute morning routine
python health_and_fitness.py morning-routine --duration 60

# 90-minute routine with specific goals
python health_and_fitness.py morning-routine --duration 90 \
    --goals "exercise,meditation,healthy breakfast"

# With kids
python health_and_fitness.py morning-routine --duration 75 --kids
```

---

### `home_and_lifestyle.py`
Covers: cleaning schedules, home repair, plant care, pet care, outfit suggestions.

```bash
# Weekly cleaning schedule for a 4-room apartment
python home_and_lifestyle.py cleaning-schedule --rooms 4 --frequency weekly

# With pets, 4 people
python home_and_lifestyle.py cleaning-schedule --rooms 6 --people 4 --pets

# Troubleshoot a home repair issue
python home_and_lifestyle.py repair "leaking faucet"
python home_and_lifestyle.py repair "toilet keeps running after flushing" --skill beginner
python home_and_lifestyle.py repair "circuit breaker keeps tripping" --skill intermediate

# Get plant care advice
python home_and_lifestyle.py plant "monstera"
python home_and_lifestyle.py plant "fiddle leaf fig" --environment "low light, dry apartment"
python home_and_lifestyle.py plant "tomatoes" --zone 7

# Diagnose a sick plant
python home_and_lifestyle.py plant "pothos" --symptoms "yellow leaves, drooping"

# Pet care guide
python home_and_lifestyle.py pet "golden retriever 3 years"
python home_and_lifestyle.py pet "persian cat 10 years" --issue "not eating well"
python home_and_lifestyle.py pet "beagle puppy 4 months"

# Outfit recommendation
python home_and_lifestyle.py outfit --occasion "job interview" --weather "cold"
python home_and_lifestyle.py outfit --occasion "beach wedding" --weather "hot and sunny"

# With your actual wardrobe
python home_and_lifestyle.py outfit \
    --occasion "first date dinner" \
    --weather "mild" \
    --wardrobe "navy chinos, white Oxford shirt, grey sweater, brown loafers, black jeans"
```

---

### `travel_and_social.py`
Covers: packing lists, vacation itineraries, restaurant guidance, gift ideas, party planning.

```bash
# Packing list for Tokyo
python travel_and_social.py packing --destination "Tokyo" --days 10 \
    --activities "sightseeing,hiking,business dinner"

# Carry-on only beach trip
python travel_and_social.py packing --destination "beach resort Thailand" --days 7 \
    --weather "hot and humid" --carry-on

# 5-day Kyoto cultural itinerary
python travel_and_social.py itinerary --destination "Kyoto, Japan" --days 5 \
    --style "cultural" --budget moderate

# Barcelona food and art tour
python travel_and_social.py itinerary --destination "Barcelona, Spain" --days 7 \
    --style "food and art" --budget moderate

# Restaurant recommendations
python travel_and_social.py restaurant --city "Tokyo" --cuisine "ramen" \
    --occasion "casual lunch"

python travel_and_social.py restaurant --city "New York" --occasion "anniversary dinner" \
    --budget upscale --diet vegetarian

# Gift ideas
python travel_and_social.py gift --for "dad, 58, loves fishing and BBQ" \
    --budget 75 --occasion "Father's Day"

python travel_and_social.py gift --for "best friend, late 20s, into yoga and travel" \
    --budget 50 --occasion "birthday"

# Party planning
python travel_and_social.py party --type "birthday" --guests 20 \
    --budget 300 --theme "90s" --age 30

python travel_and_social.py party --type "dinner party" --guests 8 \
    --budget 150 --diet "includes vegan guests"
```

---

### `habits_and_budget.py`
Covers: personal budget analysis, habit formation coaching, book/movie recommendations.

```bash
# Budget analysis with expense breakdown
python habits_and_budget.py budget --income 4500 \
    --expenses "rent:1400,food:600,transport:200,subscriptions:80,dining:300,misc:400" \
    --goal "save 600/month for house down payment"

# Budget without expense detail (general advice)
python habits_and_budget.py budget --income 3000 --goal "build a 3-month emergency fund"

# Build multiple habits
python habits_and_budget.py habits \
    --habits "daily exercise, reading 20 min, no phone before bed" \
    --duration 30 \
    --obstacle "busy evenings, always reaching for phone automatically"

# Single habit focus
python habits_and_budget.py habits --habit "meditate 10 minutes daily" \
    --obstacle "I forget and feel too tired at night"

# Book recommendations
python habits_and_budget.py recommend books \
    --liked "The Martian, Project Hail Mary" --mood "uplifting"

python habits_and_budget.py recommend books --genre "historical fiction" --count 5

# Movie recommendations
python habits_and_budget.py recommend movies \
    --liked "Inception, Interstellar, The Prestige" --time "2h"

python habits_and_budget.py recommend movies --mood "light and funny" \
    --avoid "sad endings" --count 6
```

---

## Use Cases Covered

| Script | Use Cases |
|--------|-----------|
| `food_and_nutrition.py` | Recipe from ingredients, Weekly meal planner, Grocery list optimizer, Nutrition tracker |
| `health_and_fitness.py` | Fitness workout planner, Sleep schedule optimizer, Morning routine planner |
| `home_and_lifestyle.py` | Home cleaning schedule, Home repair troubleshooter, Plant care assistant, Pet care advisor, Outfit suggester |
| `travel_and_social.py` | Travel packing list, Vacation itinerary planner, Restaurant recommender, Gift idea generator, Party planner |
| `habits_and_budget.py` | Personal budget advisor, Habit tracker coach, Book & movie recommender |

---

## Notes

- All scripts stream output token-by-token for a responsive experience.
- Connection errors are handled gracefully with a clear error message.
- Each script has a `--help` flag: `python food_and_nutrition.py --help`
- Responses are approximate — always verify nutritional data, medical information, and financial advice with qualified professionals.
- Model responses may vary between runs; this is expected behavior.
