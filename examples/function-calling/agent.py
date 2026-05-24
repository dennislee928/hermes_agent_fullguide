"""
Hermes function-calling agent.
Run: python agent.py
"""

import json
import math
import re
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-2-Pro-Mistral-7B-GGUF"

TOOLS = [
    {
        "name": "calculate",
        "description": "Evaluate a mathematical expression",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "Math expression, e.g. '2 ** 10'"}
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_weather",
        "description": "Get current weather for a city (stub — returns fake data)",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "default": "celsius"},
            },
            "required": ["city"],
        },
    },
    {
        "name": "read_file",
        "description": "Read the contents of a local text file",
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "Relative file path"}},
            "required": ["path"],
        },
    },
]


def build_system_prompt(tools: list[dict]) -> str:
    tool_json = json.dumps(tools, indent=2)
    return f"""You are a helpful assistant with access to tools.

Available tools:
{tool_json}

When you need to use a tool, respond with:
<tool_call>
{{"name": "tool_name", "arguments": {{"param": "value"}}}}
</tool_call>

After receiving <tool_response>, continue reasoning and provide a final answer.
Only call tools when necessary."""


def execute_tool(name: str, arguments: dict) -> str:
    if name == "calculate":
        try:
            safe_expr = re.sub(r"[^0-9+\-*/().% ]", "", arguments["expression"])
            result = eval(safe_expr, {"__builtins__": {}}, {"sqrt": math.sqrt, "pi": math.pi})
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    if name == "get_weather":
        city = arguments["city"]
        unit = arguments.get("unit", "celsius")
        temp = 22 if unit == "celsius" else 72
        return json.dumps({"city": city, "temperature": temp, "unit": unit, "condition": "Partly cloudy"})

    if name == "read_file":
        try:
            with open(arguments["path"], encoding="utf-8") as f:
                return f.read()[:2000]
        except FileNotFoundError:
            return f"File not found: {arguments['path']}"

    return f"Unknown tool: {name}"


def parse_tool_call(text: str) -> dict | None:
    match = re.search(r"<tool_call>\s*(\{.*?\})\s*</tool_call>", text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    return None


def chat(messages: list[dict]) -> str:
    res = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    res.raise_for_status()
    return res.json()["message"]["content"]


def run(user_input: str, max_steps: int = 5) -> str:
    messages = [
        {"role": "system", "content": build_system_prompt(TOOLS)},
        {"role": "user", "content": user_input},
    ]

    for _ in range(max_steps):
        reply = chat(messages)
        messages.append({"role": "assistant", "content": reply})

        tool_call = parse_tool_call(reply)
        if not tool_call:
            return reply

        tool_result = execute_tool(tool_call["name"], tool_call.get("arguments", {}))
        print(f"  [tool] {tool_call['name']}({tool_call.get('arguments', {})}) → {tool_result[:100]}")

        messages.append({
            "role": "user",
            "content": f"<tool_response>\n{tool_result}\n</tool_response>",
        })

    return "Max steps reached."


if __name__ == "__main__":
    print("Hermes Function-Calling Agent")
    print("Try: 'What is sqrt(144) + 55?' or 'What's the weather in Tokyo?'\n")
    while True:
        try:
            q = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not q or q in ("quit", "exit"):
            break
        answer = run(q)
        print(f"Hermes: {answer}\n")
