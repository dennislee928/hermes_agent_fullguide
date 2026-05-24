# Science Simplifier

## Description
Break down complex scientific concepts, processes, and discoveries into clear explanations calibrated to any audience level — from curious 10-year-olds to interested adults with no scientific background. Uses analogies, everyday examples, and progressive layering of complexity.

## Why Hermes
Effective science communication requires both accurate technical knowledge and the ability to construct apt analogies. Hermes-3 handles this dual demand well, producing explanations that are scientifically accurate without being dumbed down, and appropriately simplified without being misleading.

## Quickstart
```bash
python examples/education/learning_assistant.py science "explain CRISPR gene editing for a 15-year-old"
```

## Sample Input
```
Concept: Quantum entanglement
Audience: Curious adult, no physics background
```

## Output Format
```
QUANTUM ENTANGLEMENT — Explained Simply

THE BIG IDEA
Imagine you have a pair of magic gloves. You put one in a box and ship it to Australia, keeping the other in your pocket. When you open your pocket and see a left-hand glove, you instantly know the one in Australia is a right-hand glove — without looking at it.

Quantum entanglement works somewhat like this, but far stranger: two particles can be "linked" so that measuring one instantly determines properties of the other, no matter how far apart they are.

HOW IT ACTUALLY WORKS
When two particles interact in certain ways, they become entangled — their quantum states become correlated. Before measurement, each particle exists in multiple states at once (superposition). The moment you measure one, its partner's state is simultaneously determined.

WHY IT'S WEIRD
Einstein called it "spooky action at a distance" because it seems to violate the rule that nothing travels faster than light. However, entanglement can't be used to send information faster than light — it's more like a pre-shared correlation than a communication channel.

REAL-WORLD USES
- Quantum cryptography: creating unbreakable encryption keys
- Quantum computing: linking qubits to perform calculations classical computers cannot
- Quantum teleportation: transferring quantum states (not matter) between locations

GOING DEEPER
If you want to understand the mathematics, the key concept is the Bell inequality — an experiment that proved entanglement is real, not just a hidden pre-arrangement.
```

## Tips
- Always specify your audience level for the best-calibrated explanation.
- Use `"explain X using only an analogy"` for a single memorable metaphor.
- Ask for `"common misconceptions about X"` to understand what's often misunderstood.
- Effective for pre-reading before a lecture: `"give me a 3-minute overview of thermodynamics"`.
