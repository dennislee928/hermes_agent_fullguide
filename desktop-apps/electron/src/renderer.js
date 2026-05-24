const messagesEl = document.getElementById("messages");
const inputEl = document.getElementById("input");
const sendBtn = document.getElementById("send");
const modelSelect = document.getElementById("model-select");

const SYSTEM = "You are Hermes, a helpful AI assistant. Think step by step.";
let history = [{ role: "system", content: SYSTEM }];

window.hermes.listModels().then((models) => {
  modelSelect.innerHTML = models.length
    ? models.map((m) => `<option value="${m}">${m}</option>`).join("")
    : "<option>No models found — is Ollama running?</option>";
});

function addMessage(role, text) {
  const div = document.createElement("div");
  div.className = `message ${role}`;
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
  addMessage("user", text);
  history.push({ role: "user", content: text });

  const thinkingEl = addMessage("assistant", "…");

  try {
    const reply = await window.hermes.chat(modelSelect.value, history);
    thinkingEl.textContent = reply;
    history.push({ role: "assistant", content: reply });
  } catch (e) {
    thinkingEl.textContent = `Error: ${e.message}. Is Ollama running?`;
  } finally {
    sendBtn.disabled = false;
    inputEl.focus();
  }
}

sendBtn.addEventListener("click", send);
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
});
