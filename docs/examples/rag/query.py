"""
Query the ChromaDB vector store and answer with Hermes.
Run: python query.py "What does the document say about X?"
"""

import sys
import json
import requests
import chromadb

OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"
CHROMA_PATH = "./chroma_db"
COLLECTION = "hermes_rag"
TOP_K = 5

SYSTEM_PROMPT = (
    "You are a document QA assistant. Answer ONLY from the provided context. "
    "If the answer is not in the context, say so. Cite source filenames when possible."
)


def embed(text: str) -> list[float]:
    res = requests.post(OLLAMA_EMBED_URL, json={"model": EMBED_MODEL, "prompt": text}, timeout=30)
    res.raise_for_status()
    return res.json()["embedding"]


def retrieve(question: str, collection: chromadb.Collection) -> list[dict]:
    q_embed = embed(question)
    results = collection.query(query_embeddings=[q_embed], n_results=TOP_K)
    docs = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        docs.append({"text": doc, "source": meta.get("source", "unknown")})
    return docs


def build_context(docs: list[dict]) -> str:
    parts = []
    for d in docs:
        parts.append(f"[{d['source']}]\n{d['text']}")
    return "\n\n---\n\n".join(parts)


def ask_hermes(question: str, context: str) -> None:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
    ]
    res = requests.post(
        OLLAMA_CHAT_URL,
        json={"model": CHAT_MODEL, "messages": messages, "stream": True},
        stream=True,
        timeout=120,
    )
    res.raise_for_status()
    for line in res.iter_lines():
        if not line:
            continue
        chunk = json.loads(line)
        print(chunk.get("message", {}).get("content", ""), end="", flush=True)
        if chunk.get("done"):
            break
    print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python query.py \"your question here\"")
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(COLLECTION)

    print(f"Question: {question}\n")
    docs = retrieve(question, collection)
    if not docs:
        print("No documents indexed. Run ingest.py first.")
        sys.exit(1)

    context = build_context(docs)
    print("Answer: ", end="", flush=True)
    ask_hermes(question, context)


if __name__ == "__main__":
    main()
