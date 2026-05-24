const features = [
  {
    icon: "🔒",
    title: "100% Private",
    desc: "Runs entirely on your machine. No API keys, no data sent to the cloud, no usage limits.",
    tag: "Privacy",
    tagClass: "tag-green",
  },
  {
    icon: "⚡",
    title: "GPU Accelerated",
    desc: "Metal on Apple Silicon, CUDA on NVIDIA, ROCm on AMD. Automatic detection on every platform.",
    tag: "Performance",
    tagClass: "tag-blue",
  },
  {
    icon: "🧠",
    title: "Function Calling",
    desc: "Hermes-2-Pro is fine-tuned for tool use. Build agents that call real APIs and execute code.",
    tag: "Agentic",
    tagClass: "tag-purple",
  },
  {
    icon: "📚",
    title: "RAG Pipeline",
    desc: "Index your own documents with local embeddings (nomic-embed-text) and query them with Hermes.",
    tag: "Use Case",
    tagClass: "tag-yellow",
  },
  {
    icon: "🖥️",
    title: "Desktop Apps",
    desc: "Production-ready Electron, Tauri, React Native, and SwiftUI app skeletons with CI/CD pipelines.",
    tag: "Apps",
    tagClass: "tag-blue",
  },
  {
    icon: "🤖",
    title: "Autonomous Agents",
    desc: "ReAct loop with web search, file I/O, and code execution. Hermes reasons and acts over multiple steps.",
    tag: "Agents",
    tagClass: "tag-purple",
  },
];

export default function Features() {
  return (
    <section className="section-sm" style={{ borderTop: "1px solid var(--border)" }}>
      <div className="container">
        <div style={{ textAlign: "center", marginBottom: 56 }}>
          <div className="section-label">What's included</div>
          <h2 className="section-title">Everything you need to ship</h2>
          <p className="section-sub" style={{ margin: "0 auto" }}>
            From first install to production app — every layer covered with working code.
          </p>
        </div>

        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
          gap: 20,
        }}>
          {features.map(f => (
            <div key={f.title} className="card" style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between" }}>
                <span style={{ fontSize: 28 }}>{f.icon}</span>
                <span className={`tag ${f.tagClass}`}>{f.tag}</span>
              </div>
              <h3 style={{ fontSize: 17, fontWeight: 700 }}>{f.title}</h3>
              <p style={{ fontSize: 14, color: "var(--text2)", lineHeight: 1.65 }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
