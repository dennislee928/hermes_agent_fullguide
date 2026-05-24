# Home Repair Troubleshooter

## Description
Diagnose common household problems and receive step-by-step DIY repair guidance, required tools, estimated time, and a clear signal for when to call a professional instead. Covers plumbing, electrical basics, appliances, and structural issues.

## Why Hermes for This
Hermes can walk through diagnostic decision trees conversationally, asking clarifying questions and narrowing down the likely cause before offering a fix — just like a knowledgeable friend who happens to be handy.

## Quickstart
```bash
cd examples/daily-life
python home_and_lifestyle.py repair "leaking faucet"
python home_and_lifestyle.py repair "toilet keeps running after flushing"
python home_and_lifestyle.py repair "circuit breaker keeps tripping"
```

## Sample Prompt / Input
```
My kitchen faucet has a slow drip from the spout even when fully turned off.
It's a single-handle cartridge faucet (Delta brand). The drip started about a week ago.
What is the likely cause and how do I fix it?
```

## Expected Output Format
```
**Diagnosis: Worn Cartridge or O-Ring**

Single-handle cartridges are the most common cause of a persistent drip in Delta faucets.
The cartridge contains rubber seals that degrade over time, allowing water to pass through.

---
**Tools Needed:**
- Adjustable wrench or basin wrench
- Flathead and Phillips screwdrivers
- Needle-nose pliers
- Replacement Delta cartridge (RP46074 for most single-handle models)
- Plumber's grease

**Estimated Time:** 30-45 minutes

**Steps:**
1. Shut off water supply valves under the sink (turn clockwise).
2. Open the faucet handle to release residual pressure.
3. Remove the decorative cap on the handle, then unscrew the handle screw.
4. Pull off the handle to expose the cartridge.
5. Note the cartridge orientation, then pull it straight out with pliers.
6. Take the old cartridge to a hardware store to match the replacement.
7. Insert the new cartridge in the same orientation; reassemble in reverse order.
8. Turn water back on slowly and test.

**When to Call a Plumber:**
- Water supply valves won't shut off
- You see corrosion or mineral buildup on pipes
- The leak appears to be coming from inside the wall

**Difficulty: Easy | Cost: $10-25 for cartridge**
```

## Tips
- Include the brand and model of the fixture for more precise part recommendations.
- Describe what you already tried to avoid redundant suggestions.
- Ask "is this safe for a beginner?" if you're unsure — the model will advise honestly.
- Always mention if the issue involves the electrical panel; the model will prioritize professional referral for safety.
