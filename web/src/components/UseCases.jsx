import { useState } from "react";
import CodeBlock from "./CodeBlock.jsx";

const cases = [
  {
    id: "chatbot",
    icon: "💬",
    title: "Local Chatbot",
    tag: "Basic",
    tagClass: "tag-green",
    desc: "A streaming terminal chatbot with conversation history. No API key, fully private.",
    code: `cd examples/basic-chat/python
pip install -r requirements.txt
python chat.py --model hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`,
    details: [
      "Streaming token output",
      "Full conversation history",
      "Custom system prompt via --system flag",
      "TypeScript version included",
    ],
  },
  {
    id: "rag",
    icon: "📚",
    title: "RAG Pipeline",
    tag: "Advanced",
    tagClass: "tag-blue",
    desc: "Index your own PDFs and text files. Query them with Hermes. Answers grounded in your documents.",
    code: `cd examples/rag
pip install -r requirements.txt

# Index your docs
python ingest.py --docs ./my_docs/

# Ask questions
python query.py "What does the contract say about payment terms?"`,
    details: [
      "Local embeddings with nomic-embed-text (no API)",
      "ChromaDB vector store (file-based, no server)",
      "Chunking with overlap for context continuity",
      "Source citations in answers",
    ],
  },
  {
    id: "tools",
    icon: "🔧",
    title: "Function Calling",
    tag: "Agentic",
    tagClass: "tag-purple",
    desc: "Hermes-2-Pro detects when to call tools and executes a structured tool call loop.",
    code: `cd examples/function-calling
pip install -r requirements.txt
python agent.py

# Try: "What is sqrt(256) + 100?"
# Try: "What's the weather in Paris?"`,
    details: [
      "Calculator, weather, file reader tools included",
      "XML-based tool call parsing (Hermes native format)",
      "Tool result injection and re-prompting",
      "Extend by adding functions to TOOL_MAP",
    ],
  },
  {
    id: "agent",
    icon: "🤖",
    title: "Autonomous Agent",
    tag: "Advanced",
    tagClass: "tag-yellow",
    desc: "ReAct-loop agent that reasons across multiple steps with web search and code execution.",
    code: `cd examples/agent-loop
pip install -r requirements.txt

python agent.py "Research the top 3 Python web frameworks and compare them"
python agent.py "Calculate compound interest on $10,000 at 7% for 10 years"`,
    details: [
      "DuckDuckGo web search (no API key)",
      "Python code execution in sandboxed namespace",
      "File read/write tools",
      "Step limit and loop detection",
    ],
  },
];

export default function UseCases() {
  const [active, setActive] = useState("chatbot");
  const c = cases.find(c => c.id === active);

  return (
    <section id="use-cases" className="section" style={{ borderTop: "1px solid var(--border)" }}>
      <div className="container">
        <div style={{ marginBottom: 48 }}>
          <div className="section-label">Real use cases</div>
          <h2 className="section-title">From chat to autonomous agents</h2>
          <p className="section-sub">Every example is a runnable Python script with zero boilerplate.</p>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "220px 1fr", gap: 24 }}>
          {/* Sidebar */}
          <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
            {cases.map(c => (
              <button key={c.id} onClick={() => setActive(c.id)} style={{
                padding: "12px 16px", borderRadius: "var(--radius-sm)",
                border: "1px solid",
                borderColor: active === c.id ? "var(--blue)" : "var(--border)",
                background: active === c.id ? "var(--blue-glow)" : "transparent",
                color: "var(--text)", textAlign: "left", cursor: "pointer",
                display: "flex", alignItems: "center", gap: 10,
                transition: "all 0.15s",
              }}>
                <span style={{ fontSize: 20 }}>{c.icon}</span>
                <div>
                  <div style={{ fontWeight: 600, fontSize: 14 }}>{c.title}</div>
                  <div style={{ fontSize: 11, color: "var(--text3)", marginTop: 2 }}>{c.tag}</div>
                </div>
              </button>
            ))}
          </div>

          {/* Detail */}
          <div className="card" style={{ display: "flex", flexDirection: "column", gap: 20 }}>
            <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: 12 }}>
              <div>
                <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
                  <span style={{ fontSize: 28 }}>{c.icon}</span>
                  <h3 style={{ fontSize: 20, fontWeight: 700 }}>{c.title}</h3>
                  <span className={`tag ${c.tagClass}`}>{c.tag}</span>
                </div>
                <p style={{ fontSize: 15, color: "var(--text2)", lineHeight: 1.65 }}>{c.desc}</p>
              </div>
            </div>

            <div>
              <div style={{ fontSize: 12, fontWeight: 700, color: "var(--text3)", marginBottom: 8, letterSpacing: "0.06em" }}>QUICKSTART</div>
              <CodeBlock code={c.code} />
            </div>

            <div>
              <div style={{ fontSize: 12, fontWeight: 700, color: "var(--text3)", marginBottom: 12, letterSpacing: "0.06em" }}>FEATURES</div>
              <ul style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                {c.details.map(d => (
                  <li key={d} style={{ display: "flex", gap: 10, alignItems: "flex-start", fontSize: 14, color: "var(--text2)" }}>
                    <span style={{ color: "var(--green)", fontWeight: 700, flexShrink: 0, marginTop: 1 }}>✓</span>
                    {d}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
