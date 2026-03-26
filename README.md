# 💰 RAG-finanance-agent (RAG + Observability)
An end-to-end AI backend system that analyzes personal financial data using Retrieval-Augmented Generation (RAG) and provides actionable insights — with full cost, latency, and usage observability.


---

## 🚀 Features (Planned)

📥 CSV ingestion and preprocessing pipeline
🔍 Semantic search using vector embeddings
🧠 RAG-based financial insights using LLMs
💰 Token-level cost tracking
⏱ Latency instrumentation (retrieval + LLM)
🚦 Rate limiting for API safety
📊 Metrics logging and observability

---

## 🏗️ Architecture
g
                ┌──────────────┐
                │   Client     │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │   FastAPI    │
                └──────┬───────┘
                       ↓
               ┌────────────────┐
               │  Orchestrator  │
               └──────┬─────────┘
                      ↓
        ┌─────────────┴─────────────┐
        ↓                           ↓
 ┌──────────────┐           ┌──────────────┐
 │  Retrieval   │           │    Tools     │
 └──────┬───────┘           └──────────────┘
        ↓
 ┌──────────────┐
 │ Vector Store │ (FAISS)
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │     LLM      │
 └──────┬───────┘
        ↓
    Response

---

## 🧠 System Design Highlights
Modular architecture with ingestion, embedding, retrieval, and LLM layers
Dependency injection for testability and flexibility
Separation of indexing vs query pipelines
Observability built-in for cost and performance monitoring

---

## 🛠 Tech Stack

* FastAPI
* Python
* FAISS (vector search)
* OpenAI APIs

---

## ▶️ How to Run
1. Clone repo
git clone https://github.com/<your-username>/ai-finance-copilot.git
cd ai-finance-copilot
2. Install dependencies
pip install -r requirements.txt
3. Set API key
export OPENAI_API_KEY="your-api-key"
4. Run server
uvicorn app.main:app --reload
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
