"""
ReAct-style autonomous agent using Hermes.
Run: python agent.py "Research the pros and cons of Rust vs Go"
"""

import re
import sys
import json
import math
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"
MAX_STEPS = 10

SYSTEM_PROMPT = """You are an autonomous reasoning agent. Solve tasks step by step using this format:

Thought: your reasoning about what to do next
Action: tool_name
Action Input: the input to the tool

After receiving an Observation, continue with the next Thought/Action or give your final answer:

Thought: I now have enough information
Final Answer: your complete answer

Available tools:
- web_search: Search the web. Input: a search query string
- calculate: Evaluate math. Input: a math expression
- write_file: Write text to a file. Input: JSON {"path": "file.txt", "content": "text"}
- read_file: Read a file. Input: file path string

Start every response with "Thought:"."""


def web_search(query: str) -> str:
    try:
        res = requests.get(
            "https://api.duckduckgo.com/",
            params={"q": query, "format": "json", "no_html": 1, "skip_disambig": 1},
            timeout=10,
        )
        data = res.json()
        abstract = data.get("AbstractText", "")
        related = [r["Text"] for r in data.get("RelatedTopics", [])[:3] if "Text" in r]
        parts = [abstract] + related
        result = " | ".join(p for p in parts if p)
        return result or f"No results found for: {query}"
    except Exception as e:
        return f"Search error: {e}"


def calculate(expression: str) -> str:
    try:
        safe = re.sub(r"[^0-9+\-*/().% ]", "", expression)
        result = eval(safe, {"__builtins__": {}}, {"sqrt": math.sqrt, "pi": math.pi, "abs": abs})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def write_file(input_str: str) -> str:
    try:
        data = json.loads(input_str)
        with open(data["path"], "w", encoding="utf-8") as f:
            f.write(data["content"])
        return f"Written to {data['path']}"
    except Exception as e:
        return f"Error: {e}"


def read_file(path: str) -> str:
    try:
        with open(path.strip(), encoding="utf-8") as f:
            return f.read()[:3000]
    except FileNotFoundError:
        return f"File not found: {path}"


TOOL_MAP = {
    "web_search": web_search,
    "calculate": calculate,
    "write_file": write_file,
    "read_file": read_file,
}


def parse_action(text: str) -> tuple[str, str] | None:
    action_match = re.search(r"Action:\s*(\w+)", text)
    input_match = re.search(r"Action Input:\s*(.+?)(?=\nThought:|\nAction:|\Z)", text, re.DOTALL)
    if action_match and input_match:
        return action_match.group(1).strip(), input_match.group(1).strip()
    return None


def parse_final_answer(text: str) -> str | None:
    match = re.search(r"Final Answer:\s*(.+)", text, re.DOTALL)
    return match.group(1).strip() if match else None


def chat(messages: list[dict]) -> str:
    res = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=180,
    )
    res.raise_for_status()
    return res.json()["message"]["content"]


def run_agent(goal: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": goal},
    ]

    for step in range(MAX_STEPS):
        print(f"\n--- Step {step + 1} ---")
        reply = chat(messages)
        print(reply)
        messages.append({"role": "assistant", "content": reply})

        final = parse_final_answer(reply)
        if final:
            return final

        action_info = parse_action(reply)
        if not action_info:
            return reply

        tool_name, tool_input = action_info
        tool_fn = TOOL_MAP.get(tool_name)
        if not tool_fn:
            observation = f"Unknown tool: {tool_name}"
        else:
            observation = tool_fn(tool_input)

        obs_msg = f"Observation: {observation}"
        print(obs_msg)
        messages.append({"role": "user", "content": obs_msg})

    return "Agent reached max steps without a final answer."


if __name__ == "__main__":
    goal = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Goal: ").strip()
    print(f"\nGoal: {goal}\n")
    result = run_agent(goal)
    print(f"\n=== Final Answer ===\n{result}")
