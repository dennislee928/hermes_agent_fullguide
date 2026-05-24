/**
 * Tauri frontend — communicates with Ollama via the Tauri HTTP plugin.
 * In tauri.conf.json, allow: ["http://localhost:11434/*"]
 */

const OLLAMA = "http://localhost:11434";
const SYSTEM = "You are Hermes, a helpful AI assistant.";
let history = [{ role: "system", content: SYSTEM }];

const messagesEl = document.getElementById("messages");
const inputEl = document.getElementById("input");
const sendBtn = document.getElementById("send");
const modelSelect = document.getElementById("model");
const composerEl = document.getElementById("composer");

async function loadModels() {
  const res = await fetch(`${OLLAMA}/api/tags`);
  const data = await res.json();
  const models = data.models ?? [];
  modelSelect.innerHTML = models.length
    ? models.map((m) => `<option>${m.name}</option>`).join("")
    : "<option>No models — start Ollama</option>";
}

function addMsg(role, text) {
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  div.textContent = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return div;
}

async function send() {
  const text = inputEl.value.trim();
  if (!text) return;
  inputEl.value = "";
  sendBtn.disabled = true;
  addMsg("user", text);
  history.push({ role: "user", content: text });
  const el = addMsg("assistant", "…");

  try {
    const res = await fetch(`${OLLAMA}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model: modelSelect.value, messages: history, stream: false }),
    });
    const data = await res.json();
    const reply = data.message?.content ?? "No response";
    el.textContent = reply;
    history.push({ role: "assistant", content: reply });
  } catch (e) {
    el.textContent = `Error: ${e.message}`;
  } finally {
    sendBtn.disabled = false;
  }
}

composerEl.addEventListener("submit", (e) => {
  e.preventDefault();
  send();
});
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
});

loadModels();
