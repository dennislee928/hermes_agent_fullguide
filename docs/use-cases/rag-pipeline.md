# Use Case: RAG Pipeline (Retrieval-Augmented Generation)

Let Hermes answer questions about your own documents — PDFs, text files, codebases — with no hallucination risk from its training data.

## Architecture

```
Documents → chunk → embed (nomic-embed-text) → ChromaDB
                                                    ↓
User question → embed → similarity search → top-k chunks
                                                    ↓
                              Hermes: [system prompt] + [chunks] + [question]
                                                    ↓
                                           Grounded answer
```

## Quickstart

```bash
cd examples/rag
pip install -r requirements.txt

# Index your documents
python ingest.py --docs ./my_docs/

# Query
python query.py "What does the contract say about termination?"
```

## Stack

| Component | Tool | Why |
|---|---|---|
| LLM | Hermes 3 (Ollama) | Local, private |
| Embeddings | `nomic-embed-text` (Ollama) | Also local, no API key |
| Vector store | ChromaDB | Simple, file-based, no server needed |
| Orchestration | LangChain | Handles chunking, retrieval, prompting |

## What the code does

`ingest.py`:
1. Load PDFs/text files from a folder
2. Split into 512-token chunks with 50-token overlap
3. Embed each chunk with `nomic-embed-text`
4. Store in a local ChromaDB collection

`query.py`:
1. Embed the question
2. Find top-5 most similar chunks
3. Build a prompt: `[RAG system prompt] + [chunks] + [question]`
4. Stream Hermes's answer

## See the code

[examples/rag/](../../examples/rag/)

## Scaling up

- For larger doc sets (>10K docs): replace ChromaDB with **Qdrant** or **Weaviate**
- For better chunking: use `RecursiveCharacterTextSplitter` with semantic boundaries
- For re-ranking: add a cross-encoder pass before sending to Hermes
