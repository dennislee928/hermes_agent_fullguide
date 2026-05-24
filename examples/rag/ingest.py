"""
Ingest documents into a local ChromaDB vector store using Ollama embeddings.
Run: python ingest.py --docs ./my_docs
"""

import argparse
import os
from pathlib import Path

import chromadb
import requests

OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"
CHROMA_PATH = "./chroma_db"
COLLECTION = "hermes_rag"
CHUNK_SIZE = 512
CHUNK_OVERLAP = 50


def embed(text: str) -> list[float]:
    res = requests.post(OLLAMA_EMBED_URL, json={"model": EMBED_MODEL, "prompt": text}, timeout=30)
    res.raise_for_status()
    return res.json()["embedding"]


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i : i + size])
        chunks.append(chunk)
        i += size - overlap
    return chunks


def ingest_file(path: Path, collection: chromadb.Collection) -> int:
    text = path.read_text(encoding="utf-8", errors="ignore")
    chunks = chunk_text(text)
    count = 0
    for idx, chunk in enumerate(chunks):
        doc_id = f"{path.name}::{idx}"
        embedding = embed(chunk)
        collection.upsert(
            ids=[doc_id],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{"source": path.name, "chunk": idx}],
        )
        count += 1
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs", default="./docs", help="Folder with .txt / .md files")
    args = parser.parse_args()

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(COLLECTION)

    docs_path = Path(args.docs)
    total = 0
    for ext in ("*.txt", "*.md", "*.py", "*.json"):
        for file in docs_path.rglob(ext):
            n = ingest_file(file, collection)
            print(f"  {file.name}: {n} chunks")
            total += n

    print(f"\nIndexed {total} chunks into {CHROMA_PATH}")


if __name__ == "__main__":
    # Pull embed model if not present
    requests.post("http://localhost:11434/api/pull", json={"name": EMBED_MODEL}, timeout=120)
    main()
