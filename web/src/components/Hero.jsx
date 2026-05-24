import { useEffect, useState } from "react";

const GITHUB = "https://github.com/Dennislee/hermes_agent_fullguide";

const TYPING_LINES = [
  "ollama run hermes3",
  "python examples/basic-chat/python/chat.py",
  "python examples/agent-loop/agent.py \"Research quantum computing\"",
  "docker compose up -d",
];

export default function Hero() {
  const [lineIdx, setLineIdx] = useState(0);
  const [displayed, setDisplayed] = useState("");
  const [typing, setTyping] = useState(true);

  useEffect(() => {
    const line = TYPING_LINES[lineIdx];
    if (typing) {
      if (displayed.length < line.length) {
        const t = setTimeout(() => setDisplayed(line.slice(0, displayed.length + 1)), 55);
        return () => clearTimeout(t);
      } else {
        const t = setTimeout(() => setTyping(false), 1800);
        return () => clearTimeout(t);
      }
    } else {
      if (displayed.length > 0) {
        const t = setTimeout(() => setDisplayed(displayed.slice(0, -1)), 22);
        return () => clearTimeout(t);
      } else {
        setLineIdx((i) => (i + 1) % TYPING_LINES.length);
        setTyping(true);
      }
    }
  }, [displayed, typing, lineIdx]);

  return (
    <section style={{ paddingTop: 160, paddingBottom: 100, position: "relative", overflow: "hidden" }}>
      {/* Background glow */}
      <div style={{
        position: "absolute", top: -200, left: "50%", transform: "translateX(-50%)",
        width: 800, height: 600, borderRadius: "50%",
        background: "radial-gradient(ellipse, rgba(79,110,247,0.12) 0%, transparent 70%)",
        pointerEvents: "none",
      }} />

      <div className="container" style={{ textAlign: "center", position: "relative" }}>
        <div className="badge" style={{ marginBottom: 28 }}>
          <span style={{ width: 6, height: 6, borderRadius: "50%", background: "var(--green)", display: "inline-block" }} />
          NousResearch Hermes LLM · Open Source · 100% Local
        </div>

        <h1 style={{
          fontSize: "clamp(40px, 6vw, 72px)", fontWeight: 800, lineHeight: 1.1,
          letterSpacing: "-0.02em", marginBottom: 24,
        }}>
          Run Hermes AI<br />
          <span style={{
            background: "linear-gradient(135deg, #4f6ef7 0%, #a78bfa 100%)",
            WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent",
          }}>on any platform</span>
        </h1>

        <p style={{ fontSize: 20, color: "var(--text2)", maxWidth: 580, margin: "0 auto 40px", lineHeight: 1.7 }}>
          A complete guide to deploying NousResearch Hermes LLMs locally — with real-world use cases,
          runnable code, and one-click desktop apps for Windows, macOS, Linux, iOS, and Android.
        </p>

        <div style={{ display: "flex", gap: 12, justifyContent: "center", flexWrap: "wrap", marginBottom: 64 }}>
          <a href="#setup" className="btn btn-primary" style={{ padding: "14px 28px", fontSize: 16 }}>
            Get Started →
          </a>
          <a href="#demo" className="btn btn-secondary" style={{ padding: "14px 28px", fontSize: 16 }}>
            Try Live Demo
          </a>
          <a href={GITHUB} target="_blank" rel="noopener" className="btn btn-ghost" style={{ padding: "14px 28px", fontSize: 16 }}>
            View on GitHub
          </a>
        </div>

        {/* Terminal */}
        <div style={{
          maxWidth: 640, margin: "0 auto",
          background: "#080810", border: "1px solid var(--border)",
          borderRadius: 14, overflow: "hidden",
          boxShadow: "0 32px 80px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.04)",
        }}>
          <div style={{ padding: "10px 16px", background: "#0d0d18", borderBottom: "1px solid var(--border)", display: "flex", gap: 6, alignItems: "center" }}>
            {["#f87171","#fbbf24","#34d399"].map(c => (
              <div key={c} style={{ width: 10, height: 10, borderRadius: "50%", background: c }} />
            ))}
            <span style={{ fontSize: 12, color: "var(--text3)", marginLeft: 8 }}>Terminal</span>
          </div>
          <div style={{ padding: "20px 24px", fontFamily: "JetBrains Mono, monospace", fontSize: 14, textAlign: "left", minHeight: 60 }}>
            <span style={{ color: "var(--green)" }}>$ </span>
            <span style={{ color: "var(--text)" }}>{displayed}</span>
            <span style={{ animation: "blink 1s step-end infinite", color: "var(--blue)" }}>▋</span>
          </div>
        </div>

        {/* Stats */}
        <div style={{ display: "flex", gap: 48, justifyContent: "center", marginTop: 56, flexWrap: "wrap" }}>
          {[
            { n: "5", label: "Platforms" },
            { n: "4", label: "Use Cases" },
            { n: "3", label: "Desktop Frameworks" },
            { n: "100%", label: "Local & Private" },
          ].map(s => (
            <div key={s.label} style={{ textAlign: "center" }}>
              <div style={{ fontSize: 32, fontWeight: 800, color: "var(--text)", letterSpacing: "-0.02em" }}>{s.n}</div>
              <div style={{ fontSize: 13, color: "var(--text3)", marginTop: 2 }}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>

      <style>{`@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }`}</style>
    </section>
  );
}
