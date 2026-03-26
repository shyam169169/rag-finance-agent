# 💰 AI Financial Copilot (RAG + Observability)

An end-to-end AI backend system that analyzes personal financial data using **Retrieval-Augmented Generation (RAG)** and provides actionable insights — with full **cost, latency, and usage observability**.

---

## 🚀 Key Features

* 📥 CSV ingestion and preprocessing pipeline
* 🔍 Semantic search using vector embeddings
* 🧠 RAG-based financial insights using LLMs
* 💰 Token-level cost tracking
* ⏱ Latency instrumentation (retrieval + LLM)
* 🚦 Rate limiting for API safety
* 📊 Metrics logging and observability

---

## 🏗️ Architecture

```text
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
```

---

## 🧠 System Design Highlights

* Modular architecture with **ingestion, embedding, retrieval, and LLM layers**
* Dependency injection for **testability and flexibility**
* Separation of **indexing vs query pipelines**
* Observability built-in for **cost and performance monitoring**

---

## 🛠 Tech Stack

* FastAPI (backend framework)
* Python
* FAISS (vector similarity search)
* OpenAI APIs (LLM + embeddings)

---

## ▶️ How to Run

### 1. Clone repo

```bash
git clone https://github.com/<your-username>/ai-finance-copilot.git
cd ai-finance-copilot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API key

```bash
export OPENAI_API_KEY="your-api-key"
```

### 4. Run server

```bash
uvicorn app.main:app --reload
```

---

## 🧪 API Endpoints

| Endpoint             | Description                            |
| -------------------- | -------------------------------------- |
| `POST /upload`       | Upload CSV and build vector index      |
| `POST /query`        | RAG-based response with cost + latency |
| `POST /query-stream` | Streaming response                     |
| `GET /metrics`       | View token + latency logs              |

---

## 📊 Example Response

```json
{
  "answer": "You are spending heavily on shopping...",
  "usage": {
    "total_tokens": 1050,
    "cost": 0.00023
  },
  "latency": {
    "retrieval_time": 0.01,
    "llm_time": 1.2,
    "total_time": 1.21
  }
}
```

---

## 📌 Roadmap

* [x] RAG pipeline (ingestion → retrieval → generation)
* [x] Token + cost tracking
* [x] Latency instrumentation
* [x] Rate limiting
* [ ] Observability dashboard
* [ ] Multi-user support
* [ ] Caching layer

---

## 📬 Contact

Feel free to connect or reach out for discussion on AI backend systems.
