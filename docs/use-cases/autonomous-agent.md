# Use Case: Autonomous Agent (ReAct Loop)

Build an agent that can reason and act autonomously over multiple steps — web search, file operations, code execution — using Hermes as the reasoning engine.

## Pattern: ReAct (Reason + Act)

```
Thought: I need to find the current price of Bitcoin
Action: web_search("bitcoin price usd")
Observation: Bitcoin is $67,420 as of 2024-01-15
Thought: I have the answer
Final Answer: Bitcoin is currently $67,420 USD.
```

Hermes generates Thought/Action pairs; your code executes the actions and feeds Observations back.

## Quickstart

```bash
cd examples/agent-loop
pip install -r requirements.txt
python agent.py "Research the top 3 Python web frameworks and summarize their differences"
```

## Architecture

```
User goal
    ↓
[Hermes] Thought + Action
    ↓
[Tool executor] runs action → Observation
    ↓
[Hermes] next Thought + Action (or Final Answer)
    ↓
Loop until "Final Answer" or max_steps reached
```

## Available tools in the example

| Tool | What it does |
|---|---|
| `web_search` | DuckDuckGo search (no API key needed) |
| `read_file` | Read a local file |
| `write_file` | Write/create a local file |
| `run_python` | Execute Python code in a sandbox |
| `calculate` | Evaluate math expressions |

## Safety

The example sandbox limits `run_python` to a restricted namespace — no file system access, no network. Adjust `safe_builtins` in `agent.py` to your needs.

## See the code

[examples/agent-loop/agent.py](../../examples/agent-loop/agent.py)

Key sections:
- `build_system_prompt()` — injects tool definitions into the ReAct prompt
- `parse_action()` — extracts Action/Action Input from Hermes output
- `run_agent()` — the main loop with step limit and loop detection
