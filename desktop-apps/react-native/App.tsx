/**
 * Hermes Chat — React Native app (iOS + Android)
 * Connects to an Ollama server on your local network.
 *
 * Setup:
 *   npm install
 *   npx expo start
 *
 * Set OLLAMA_HOST to your machine's local IP (e.g. 192.168.1.100)
 */

import React, { useState, useRef } from "react";
import {
  View, Text, TextInput, TouchableOpacity, FlatList,
  StyleSheet, KeyboardAvoidingView, Platform, ActivityIndicator,
} from "react-native";

const OLLAMA_HOST = process.env.EXPO_PUBLIC_OLLAMA_HOST ?? "192.168.1.100";
const OLLAMA_URL = `http://${OLLAMA_HOST}:11434/api/chat`;
const MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF";
const SYSTEM = "You are Hermes, a helpful AI assistant.";

type Message = { id: string; role: "user" | "assistant"; content: string };

export default function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const listRef = useRef<FlatList>(null);
  const history = useRef([{ role: "system", content: SYSTEM }]);

  async function send() {
    const text = input.trim();
    if (!text || loading) return;

    setInput("");
    const userMsg: Message = { id: Date.now().toString(), role: "user", content: text };
    setMessages((prev) => [...prev, userMsg]);
    history.current.push({ role: "user", content: text });
    setLoading(true);

    try {
      const res = await fetch(OLLAMA_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ model: MODEL, messages: history.current, stream: false }),
      });
      const data = await res.json();
      const reply = data.message?.content ?? "No response";
      history.current.push({ role: "assistant", content: reply });
      setMessages((prev) => [
        ...prev,
        { id: (Date.now() + 1).toString(), role: "assistant", content: reply },
      ]);
    } catch (e: any) {
      setMessages((prev) => [
        ...prev,
        { id: (Date.now() + 1).toString(), role: "assistant", content: `Error: ${e.message}` },
      ]);
    } finally {
      setLoading(false);
      setTimeout(() => listRef.current?.scrollToEnd({ animated: true }), 100);
    }
  }

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === "ios" ? "padding" : undefined}
    >
      <View style={styles.header}>
        <Text style={styles.headerText}>Hermes</Text>
        <Text style={styles.subText}>{OLLAMA_HOST}</Text>
      </View>

      <FlatList
        ref={listRef}
        data={messages}
        keyExtractor={(m) => m.id}
        contentContainerStyle={styles.messageList}
        renderItem={({ item }) => (
          <View style={[styles.bubble, item.role === "user" ? styles.userBubble : styles.aiBubble]}>
            <Text style={styles.bubbleText}>{item.content}</Text>
          </View>
        )}
      />

      {loading && <ActivityIndicator style={{ margin: 8 }} color="#2563eb" />}

      <View style={styles.footer}>
        <TextInput
          style={styles.input}
          value={input}
          onChangeText={setInput}
          placeholder="Message Hermes..."
          placeholderTextColor="#666"
          multiline
          onSubmitEditing={send}
          returnKeyType="send"
        />
        <TouchableOpacity style={styles.sendBtn} onPress={send} disabled={loading}>
          <Text style={styles.sendText}>↑</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#1a1a1a" },
  header: { paddingTop: 60, paddingHorizontal: 20, paddingBottom: 12, backgroundColor: "#111",
            borderBottomWidth: 1, borderBottomColor: "#333" },
  headerText: { fontSize: 20, fontWeight: "700", color: "#fff" },
  subText: { fontSize: 12, color: "#666", marginTop: 2 },
  messageList: { padding: 16, gap: 12 },
  bubble: { maxWidth: "80%", padding: 12, borderRadius: 14 },
  userBubble: { backgroundColor: "#2563eb", alignSelf: "flex-end", borderBottomRightRadius: 4 },
  aiBubble: { backgroundColor: "#2a2a2a", alignSelf: "flex-start", borderBottomLeftRadius: 4 },
  bubbleText: { color: "#fff", fontSize: 15, lineHeight: 22 },
  footer: { flexDirection: "row", padding: 12, gap: 8, backgroundColor: "#111",
            borderTopWidth: 1, borderTopColor: "#333" },
  input: { flex: 1, backgroundColor: "#2a2a2a", color: "#fff", borderRadius: 20,
           paddingHorizontal: 16, paddingVertical: 10, fontSize: 15, maxHeight: 120 },
  sendBtn: { width: 44, height: 44, backgroundColor: "#2563eb", borderRadius: 22,
             alignItems: "center", justifyContent: "center" },
  sendText: { color: "#fff", fontSize: 20, fontWeight: "700" },
});
