import { useState, useRef, useEffect } from "react";

const OLLAMA = "/ollama"; // proxied through Vite dev server
const DEFAULT_MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF";
const SYSTEM = "You are Hermes, a helpful AI assistant created by NousResearch. Be concise and helpful.";

// --- Demo modes ---
const MODES = [
  { id: "chat", label: "💬 Chat", desc: "Talk to Hermes" },
  { id: "tools", label: "🔧 Function Calling", desc: "Hermes calls tools" },
  { id: "agent", label: "🤖 Agent Loop", desc: "Multi-step reasoning" },
];

// Simulated tool results for demo
const TOOL_STUBS = {
  get_weather: (args) => `{"city":"${args.city || 'Tokyo'}","temperature":22,"unit":"celsius","condition":"Partly cloudy","humidity":68}`,
  calculate: (args) => {
    try { return String(eval(args.expression.replace(/[^0-9+\-*/().% ]/g, ""))); }
    catch { return "Error evaluating expression"; }
  },
  web_search: (args) => `Top results for "${args.query}": 1. Wikipedia article, 2. Recent news coverage, 3. Official documentation. [Simulated results — connect real search API for live data]`,
};

function parseToolCall(text) {
  const m = text.match(/<tool_call>\s*(\{[\s\S]*?\})\s*<\/tool_call>/);
  if (m) { try { return JSON.parse(m[1]); } catch {} }
  return null;
}

// --- Status indicator ---
function OllamaStatus({ status }) {
  const colors = { checking: "var(--yellow)", online: "var(--green)", offline: "var(--red)" };
  const labels = { checking: "Checking Ollama...", online: "Ollama connected", offline: "Ollama offline — start it to use live demo" };
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, fontSize: 13, color: "var(--text2)" }}>
      <span style={{ width: 8, height: 8, borderRadius: "50%", background: colors[status], display: "inline-block",
        boxShadow: status === "online" ? "0 0 6px var(--green)" : "none" }} />
      {labels[status]}
    </div>
  );
}

// --- Message bubble ---
function Bubble({ msg }) {
  const isUser = msg.role === "user";
  return (
    <div style={{ display: "flex", gap: 10, alignItems: "flex-start", flexDirection: isUser ? "row-reverse" : "row" }}>
      {!isUser && (
        <div style={{ width: 28, height: 28, borderRadius: "50%", background: "var(--blue-glow)",
          border: "1px solid var(--blue)", display: "flex", alignItems: "center", justifyContent: "center",
          fontSize: 13, flexShrink: 0 }}>⚡</div>
      )}
      <div style={{
        maxWidth: "78%", padding: "10px 14px", borderRadius: 12,
        background: isUser ? "var(--blue)" : "var(--bg3)",
        border: isUser ? "none" : "1px solid var(--border)",
        fontSize: 14, lineHeight: 1.6,
        borderBottomRightRadius: isUser ? 4 : 12,
        borderBottomLeftRadius: isUser ? 12 : 4,
        whiteSpace: "pre-wrap", wordBreak: "break-word",
      }}>
        {msg.content}
        {msg.streaming && <span style={{ animation: "blink 1s step-end infinite", color: "var(--blue)" }}>▋</span>}
      </div>
    </div>
  );
}

function ToolCallBubble({ call, result }) {
  return (
    <div style={{ padding: "10px 14px", borderRadius: 10, background: "rgba(167,139,250,0.06)",
      border: "1px solid rgba(167,139,250,0.2)", fontSize: 13, fontFamily: "monospace" }}>
      <div style={{ color: "var(--purple)", fontWeight: 700, marginBottom: 6 }}>⚙ Tool call: {call.name}</div>
      <div style={{ color: "var(--text2)" }}>Args: {JSON.stringify(call.arguments)}</div>
      {result && <div style={{ color: "var(--green)", marginTop: 6 }}>→ {result.slice(0, 120)}{result.length > 120 ? "…" : ""}</div>}
    </div>
  );
}

// --- Preset prompts per mode ---
const PRESETS = {
  chat: [
    "Explain the difference between RAG and fine-tuning in 3 sentences",
    "Write a Python function to parse JSON safely",
    "What are the pros and cons of Hermes vs GPT-4?",
  ],
  tools: [
    "What's the weather like in Tokyo right now?",
    "Calculate 2 to the power of 32, then add 1024",
    "Search for recent news about local AI models",
  ],
  agent: [
    "Research quantum computing and give me a 3-point summary",
    "What is 15% of 847, and is that more or less than 100?",
    "Find information about Hermes LLM and summarize its key features",
  ],
};

const TOOL_SYSTEM = `You are a helpful assistant with access to tools. When you need a tool, respond with:
<tool_call>
{"name": "tool_name", "arguments": {"param": "value"}}
</tool_call>

Available tools:
- get_weather: Get weather for a city. Args: {city: string}
- calculate: Evaluate math. Args: {expression: string}
- web_search: Search the web. Args: {query: string}

After receiving tool results, give a natural answer. Only call tools when needed.`;

const AGENT_SYSTEM = `You are an autonomous reasoning agent. Solve tasks step by step:

Thought: your reasoning
Action: tool_name
Action Input: the input

After Observation, continue or give:
Final Answer: your answer

Tools: web_search(query), calculate(expression)

Always start with "Thought:"`;

export default function LiveDemo() {
  const [mode, setMode] = useState("chat");
  const [messages, setMessages] = useState([]);
  const [toolEvents, setToolEvents] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [ollamaStatus, setOllamaStatus] = useState("checking");
  const [models, setModels] = useState([DEFAULT_MODEL]);
  const [selectedModel, setSelectedModel] = useState(DEFAULT_MODEL);
  const bottomRef = useRef(null);
  const history = useRef([]);

  useEffect(() => {
    checkOllama();
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, toolEvents]);

  useEffect(() => {
    setMessages([]);
    setToolEvents([]);
    history.current = [];
  }, [mode]);

  async function checkOllama() {
    try {
      const res = await fetch(`${OLLAMA}/api/tags`, { signal: AbortSignal.timeout(3000) });
      if (res.ok) {
        const data = await res.json();
        const names = (data.models ?? []).map(m => m.name);
        if (names.length) setModels(names);
        setOllamaStatus("online");
      } else {
        setOllamaStatus("offline");
      }
    } catch {
      setOllamaStatus("offline");
    }
  }

  function getSystemPrompt() {
    if (mode === "tools") return TOOL_SYSTEM;
    if (mode === "agent") return AGENT_SYSTEM;
    return SYSTEM;
  }

  async function streamReply(msgs) {
    const res = await fetch(`${OLLAMA}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model: selectedModel, messages: msgs, stream: true }),
    });
    if (!res.ok) throw new Error(`Ollama error ${res.status}`);

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let full = "";

    const id = Date.now();
    setMessages(prev => [...prev, { id, role: "assistant", content: "", streaming: true }]);

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      const lines = decoder.decode(value).split("\n").filter(Boolean);
      for (const line of lines) {
        try {
          const chunk = JSON.parse(line);
          const token = chunk?.message?.content ?? "";
          full += token;
          setMessages(prev => prev.map(m => m.id === id ? { ...m, content: full } : m));
        } catch {}
      }
    }

    setMessages(prev => prev.map(m => m.id === id ? { ...m, streaming: false } : m));
    return full;
  }

  async function sendChat(text) {
    history.current.push({ role: "user", content: text });
    const msgs = [{ role: "system", content: getSystemPrompt() }, ...history.current];
    const reply = await streamReply(msgs);
    history.current.push({ role: "assistant", content: reply });
  }

  async function sendWithTools(text) {
    history.current.push({ role: "user", content: text });
    const events = [];
    let safetyCount = 0;

    while (safetyCount++ < 4) {
      const msgs = [{ role: "system", content: getSystemPrompt() }, ...history.current];
      const reply = await streamReply(msgs);
      history.current.push({ role: "assistant", content: reply });

      const toolCall = parseToolCall(reply);
      if (!toolCall) break;

      const stubFn = TOOL_STUBS[toolCall.name];
      const result = stubFn ? stubFn(toolCall.arguments ?? {}) : "Tool not found";
      const event = { call: toolCall, result };
      events.push(event);
      setToolEvents(prev => [...prev, event]);

      history.current.push({ role: "user", content: `<tool_response>\n${result}\n</tool_response>` });
    }
  }

  async function sendAgentLoop(text) {
    history.current.push({ role: "user", content: text });
    let safetyCount = 0;

    while (safetyCount++ < 5) {
      const msgs = [{ role: "system", content: getSystemPrompt() }, ...history.current];
      const reply = await streamReply(msgs);
      history.current.push({ role: "assistant", content: reply });

      if (reply.includes("Final Answer:")) break;

      const actionMatch = reply.match(/Action:\s*(\w+)\nAction Input:\s*(.+)/);
      if (actionMatch) {
        const [, toolName, toolInput] = actionMatch;
        const stubFn = TOOL_STUBS[toolName];
        const result = stubFn ? stubFn({ query: toolInput, expression: toolInput }) : "No result";
        const obs = `Observation: ${result}`;
        const event = { call: { name: toolName, arguments: { input: toolInput } }, result };
        setToolEvents(prev => [...prev, event]);
        history.current.push({ role: "user", content: obs });
      } else {
        break;
      }
    }
  }

  async function send(text) {
    const t = (text ?? input).trim();
    if (!t || loading) return;
    setInput("");
    setLoading(true);
    setMessages(prev => [...prev, { id: Date.now() - 1, role: "user", content: t }]);

    try {
      if (mode === "chat") await sendChat(t);
      else if (mode === "tools") await sendWithTools(t);
      else await sendAgentLoop(t);
    } catch (e) {
      setMessages(prev => [...prev, { id: Date.now(), role: "assistant", content: `⚠ ${e.message}. Is Ollama running?` }]);
    } finally {
      setLoading(false);
    }
  }

  const allEvents = [...toolEvents];

  return (
    <section id="demo" className="section" style={{ borderTop: "1px solid var(--border)" }}>
      <div className="container">
        <div style={{ marginBottom: 40 }}>
          <div className="section-label">Interactive Demo</div>
          <h2 className="section-title">Try Hermes live</h2>
          <p className="section-sub">
            Connects directly to your local Ollama instance. No data leaves your machine.
          </p>
        </div>

        <div className="card" style={{ padding: 0, overflow: "hidden", maxWidth: 820 }}>
          {/* Demo toolbar */}
          <div style={{ padding: "14px 20px", background: "var(--bg3)", borderBottom: "1px solid var(--border)",
            display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
            <div style={{ display: "flex", gap: 4, flex: 1 }}>
              {MODES.map(m => (
                <button key={m.id} onClick={() => setMode(m.id)} style={{
                  padding: "6px 14px", borderRadius: "var(--radius-sm)", border: "1px solid",
                  borderColor: mode === m.id ? "var(--blue)" : "var(--border)",
                  background: mode === m.id ? "var(--blue-glow)" : "transparent",
                  color: mode === m.id ? "var(--blue)" : "var(--text2)",
                  fontSize: 13, fontWeight: 600, cursor: "pointer", transition: "all 0.15s",
                }}>{m.label}</button>
              ))}
            </div>
            <OllamaStatus status={ollamaStatus} />
          </div>

          {/* Model selector */}
          <div style={{ padding: "10px 20px", background: "var(--bg2)", borderBottom: "1px solid var(--border)",
            display: "flex", alignItems: "center", gap: 10 }}>
            <span style={{ fontSize: 12, color: "var(--text3)", fontWeight: 600 }}>MODEL</span>
            <select value={selectedModel} onChange={e => setSelectedModel(e.target.value)} style={{
              background: "var(--bg3)", color: "var(--text2)", border: "1px solid var(--border)",
              borderRadius: 6, padding: "3px 8px", fontSize: 12, fontFamily: "JetBrains Mono, monospace",
              cursor: "pointer",
            }}>
              {models.map(m => <option key={m} value={m}>{m}</option>)}
            </select>
            {ollamaStatus === "offline" && (
              <button onClick={checkOllama} style={{
                fontSize: 11, padding: "3px 10px", borderRadius: 6,
                background: "transparent", border: "1px solid var(--border2)",
                color: "var(--text3)", cursor: "pointer",
              }}>Retry</button>
            )}
          </div>

          {/* Messages */}
          <div style={{ height: 380, overflowY: "auto", padding: "20px", display: "flex", flexDirection: "column", gap: 12 }}>
            {messages.length === 0 && (
              <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", gap: 16 }}>
                <div style={{ fontSize: 40 }}>⚡</div>
                <div style={{ fontSize: 14, color: "var(--text3)", textAlign: "center" }}>
                  {MODES.find(m => m.id === mode)?.desc} — try a preset below
                </div>
                <div style={{ display: "flex", gap: 8, flexWrap: "wrap", justifyContent: "center" }}>
                  {PRESETS[mode].map(p => (
                    <button key={p} onClick={() => send(p)} style={{
                      padding: "6px 14px", borderRadius: "var(--radius-sm)",
                      background: "var(--bg3)", border: "1px solid var(--border2)",
                      color: "var(--text2)", fontSize: 13, cursor: "pointer", transition: "all 0.15s",
                    }}
                    onMouseEnter={e => e.currentTarget.style.borderColor = "var(--blue)"}
                    onMouseLeave={e => e.currentTarget.style.borderColor = "var(--border2)"}
                    >{p}</button>
                  ))}
                </div>
              </div>
            )}

            {messages.map(msg => (
              <div key={msg.id}>
                <Bubble msg={msg} />
                {/* Show tool events after assistant messages */}
                {msg.role === "assistant" && allEvents
                  .filter(e => msg.content.includes(e.call.name))
                  .slice(0, 1)
                  .map((e, i) => <div key={i} style={{ marginTop: 8, marginLeft: 38 }}><ToolCallBubble call={e.call} result={e.result} /></div>)
                }
              </div>
            ))}

            {loading && messages.length > 0 && messages[messages.length - 1].role === "user" && (
              <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
                <div style={{ width: 28, height: 28, borderRadius: "50%", background: "var(--blue-glow)",
                  border: "1px solid var(--blue)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 13 }}>⚡</div>
                <div style={{ display: "flex", gap: 4 }}>
                  {[0,1,2].map(i => (
                    <div key={i} style={{ width: 6, height: 6, borderRadius: "50%", background: "var(--blue)",
                      animation: `pulse 1.2s ease-in-out ${i * 0.2}s infinite` }} />
                  ))}
                </div>
              </div>
            )}
            <div ref={bottomRef} />
          </div>

          {/* Input */}
          <div style={{ padding: "14px 20px", borderTop: "1px solid var(--border)", display: "flex", gap: 10 }}>
            <input
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={e => e.key === "Enter" && !e.shiftKey && send()}
              placeholder={ollamaStatus === "offline" ? "Start Ollama to enable live chat..." : "Message Hermes..."}
              disabled={loading || ollamaStatus === "offline"}
              style={{
                flex: 1, background: "var(--bg3)", color: "var(--text)",
                border: "1px solid var(--border)", borderRadius: "var(--radius-sm)",
                padding: "10px 14px", fontSize: 14, outline: "none",
                opacity: ollamaStatus === "offline" ? 0.5 : 1,
              }}
            />
            <button
              onClick={() => send()}
              disabled={loading || !input.trim() || ollamaStatus === "offline"}
              className="btn btn-primary"
              style={{ padding: "10px 20px" }}
            >
              {loading ? "…" : "Send"}
            </button>
          </div>
        </div>

        {/* Quick presets below */}
        {messages.length > 0 && (
          <div style={{ marginTop: 16, display: "flex", gap: 8, flexWrap: "wrap" }}>
            {PRESETS[mode].map(p => (
              <button key={p} onClick={() => send(p)} disabled={loading} style={{
                padding: "5px 12px", borderRadius: "var(--radius-sm)",
                background: "transparent", border: "1px solid var(--border)",
                color: "var(--text3)", fontSize: 12, cursor: "pointer",
              }}>{p}</button>
            ))}
            <button onClick={() => { setMessages([]); setToolEvents([]); history.current = []; }} style={{
              padding: "5px 12px", borderRadius: "var(--radius-sm)",
              background: "transparent", border: "1px solid var(--border)",
              color: "var(--text3)", fontSize: 12, cursor: "pointer",
            }}>Clear</button>
          </div>
        )}
      </div>
      <style>{`
        @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
        @keyframes pulse { 0%,100%{opacity:0.3;transform:scale(0.8)} 50%{opacity:1;transform:scale(1)} }
      `}</style>
    </section>
  );
}
