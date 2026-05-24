import { useState } from "react";

export default function CodeBlock({ code, language = "bash" }) {
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    await navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 1800);
  };

  return (
    <div className="code-block mono" style={{ position: "relative" }}>
      <pre style={{ whiteSpace: "pre-wrap", wordBreak: "break-all" }}>{code}</pre>
      <button className={`copy-btn ${copied ? "copied" : ""}`} onClick={copy}>
        {copied ? "Copied!" : "Copy"}
      </button>
    </div>
  );
}
