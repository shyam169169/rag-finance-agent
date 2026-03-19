# 💰 RAG-finanance-agent (RAG + Agent System)

An AI-powered backend system that analyzes personal financial data using **Retrieval-Augmented Generation (RAG)** and provides actionable insights.

---

## 🚀 Features (Planned)

* 📥 CSV ingestion and processing
* 🔍 Semantic search using embeddings
* 🧠 RAG-based financial insights
* ⚡ Streaming responses
* 💰 Token cost tracking
* 🚦 Rate limiting
* 📊 Observability dashboard

---

## 🏗️ Architecture

```text
CSV → Chunking → Embeddings → Vector DB
                               ↓
User Query → Retrieval → LLM → Response
```

---

## 🧪 Current Status

✅ Ingestion pipeline (CSV → chunks)
✅ Unit tests for ingestion
🚧 Embedding module (in progress)

---

## 🛠 Tech Stack

* FastAPI
* Python
* FAISS (vector search)
* OpenAI APIs

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 📌 Roadmap

* [x] Ingestion module
* [ ] Embedding + vector store
* [ ] Retrieval pipeline
* [ ] Streaming responses
* [ ] Cost tracking
* [ ] Rate limiting
* [ ] Observability dashboard

---

## 💡 Why this project?

This project is designed to demonstrate:

* AI backend engineering
* RAG system design
* Production-ready architecture
