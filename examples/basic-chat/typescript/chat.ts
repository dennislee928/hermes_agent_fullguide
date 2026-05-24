/**
 * Streaming terminal chatbot using Hermes via Ollama.
 * Run: npx ts-node chat.ts
 * Or:  bun run chat.ts
 */

import * as readline from "readline";

const OLLAMA_URL = "http://localhost:11434/api/chat";
const MODEL = process.env.HERMES_MODEL ?? "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF";
const SYSTEM = "You are Hermes, a helpful AI assistant. Think step by step.";

type Message = { role: "system" | "user" | "assistant"; content: string };

async function streamChat(messages: Message[]): Promise<string> {
  const res = await fetch(OLLAMA_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ model: MODEL, messages, stream: true }),
  });

  if (!res.ok || !res.body) throw new Error(`HTTP ${res.status}`);

  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let fullReply = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const lines = decoder.decode(value).split("\n").filter(Boolean);
    for (const line of lines) {
      const chunk = JSON.parse(line);
      const token: string = chunk?.message?.content ?? "";
      process.stdout.write(token);
      fullReply += token;
    }
  }

  process.stdout.write("\n");
  return fullReply;
}

async function main() {
  const messages: Message[] = [{ role: "system", content: SYSTEM }];
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

  console.log(`Hermes Chat (${MODEL})\nType 'quit' to exit.\n`);

  const ask = () => {
    rl.question("You: ", async (input) => {
      input = input.trim();
      if (!input || input === "quit") { rl.close(); return; }

      messages.push({ role: "user", content: input });
      process.stdout.write("Hermes: ");

      const reply = await streamChat(messages);
      messages.push({ role: "assistant", content: reply });

      ask();
    });
  };

  ask();
}

main().catch(console.error);
