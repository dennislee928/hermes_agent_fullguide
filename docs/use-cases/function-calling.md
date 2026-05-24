# Use Case: Function Calling / Tool Use

Hermes-2-Pro and Hermes-3 are fine-tuned for function calling using a structured XML/JSON format. Use this to give the model access to real tools: web search, calculators, APIs, file systems.

## How Hermes does function calling

Hermes uses a `<tool_call>` XML format in its output:

```
<tool_call>
{"name": "get_weather", "arguments": {"city": "Tokyo", "unit": "celsius"}}
</tool_call>
```

Your code detects this, runs the function, and feeds the result back as a `<tool_response>`.

## Quickstart

```bash
cd examples/function-calling
pip install -r requirements.txt
python agent.py
```

## Recommended model

```bash
ollama pull hf.co/NousResearch/Hermes-2-Pro-Mistral-7B-GGUF
```

Hermes-2-Pro has the strongest function-calling accuracy of the Hermes family.

## Tool definition format

```python
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["city"]
        }
    }
]
```

Tools are injected into the system prompt by the example code.

## Loop pattern

```
1. Send user message + tool definitions to Hermes
2. Parse response for <tool_call> blocks
3. Execute the requested function
4. Append tool result to conversation as <tool_response>
5. Send back to Hermes for final answer
6. Repeat until no more tool calls
```

## See the code

[examples/function-calling/agent.py](../../examples/function-calling/agent.py)

Includes: weather tool, calculator, web search stub, file reader.
