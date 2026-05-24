# Book & Movie Recommender

## Description
Receive personalized book or movie recommendations based on titles you've enjoyed, preferred genres, mood, and available time. Each recommendation includes a brief pitch explaining why it matches your taste.

## Why Hermes for This
Hermes can reason about thematic, stylistic, and emotional similarities between works — going beyond genre matching to understand why you loved a specific book or film and finding others with the same essence.

## Quickstart
```bash
cd examples/daily-life
python habits_and_budget.py recommend books --liked "The Martian, Project Hail Mary" --mood "uplifting"
python habits_and_budget.py recommend movies --liked "Inception, Interstellar" --time 2h
python habits_and_budget.py recommend books --genre "historical fiction" --count 5
```

## Sample Prompt / Input
```
I loved "The Martian" and "Project Hail Mary" by Andy Weir.
I enjoy: hard science fiction, competent protagonists solving problems, optimistic tone, humor.
Recommend 5 books I'll probably love. Include a brief pitch for each.
```

## Expected Output Format
```
**Book Recommendations — Hard Sci-Fi, Problem-Solving, Optimistic**
Based on: The Martian, Project Hail Mary

---
1. **"The Long Way to a Small, Angry Planet" — Becky Chambers**
   *Why you'll love it:* Found-family crew solving problems together on a long space voyage.
   Warm, optimistic tone — the closest thing to "cozy sci-fi." Less hard-science than Weir
   but deeply human and uplifting.

2. **"Children of Time" — Adrian Tchaikovsky**
   *Why you'll love it:* Evolutionary biology + first contact + competent characters under
   extreme pressure. Scientifically rigorous and endlessly inventive — hard sci-fi readers
   consistently rank it among the best of the decade.

3. **"Seveneves" — Neal Stephenson**
   *Why you'll love it:* An engineer's dream — pages of real orbital mechanics and survival
   problem-solving. Slower paced than Weir but rewards patience with jaw-dropping scope.

4. **"A Fire Upon the Deep" — Vernor Vinge**
   *Why you'll love it:* Big ideas: zones of thought where intelligence itself is limited.
   Alien civilizations feel genuinely alien. Classic hard SF.

5. **"The Dispatcher" — John Scalzi**
   *Why you'll love it:* Short, punchy, and clever — a perfect palate cleanser between
   longer books. Scalzi has Weir's wit with a noir detective twist.
```

## Tips
- Give 2-3 specific titles you've loved for the most accurate recommendations.
- Specify mood ("I want something light" vs. "I want something that challenges me") to tune the tone.
- Add `--avoid "slow pacing, sad endings"` to filter out works with deal-breaker traits.
- Ask for a mix of well-known and obscure titles for variety.
