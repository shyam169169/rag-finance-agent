# 💰 AI Financial Copilot(a.k.a rag finanace agent) (RAG + Observability)

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
Clone this repo
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
| `GET /metrics`       | View token + latency logs              |

---

## 📊 Example Response

```json
{
    "question": "\"How much did I spend on home\"",
    "retrieved_chunks": [
        "[TRANSACTION]\nDate: 02/02/2025\nCategory: beverage\nAmount: 10$\nDescription: ",
        "[TRANSACTION]\nDate: 02/02/2025\nCategory: home\nAmount: 1000$\nDescription: "
    ],
    "answer": "You spent $1000 on home-related expenses on 02/02/2025.\n\nActionable insight: Since the home expense is significantly higher than your beverage expense, it might be helpful to review your home-related purchases to ensure they align with your budget and financial goals. Consider tracking larger expenses like these to better manage your monthly spending.",
    "usage": {
        "input_tokens": 105,
        "output_tokens": 68,
        "total_tokens": 173
    },
    "latency": {
        "retrieval_time": 1.621246337890625e-05,
        "llm_time": 1.909255027770996,
        "total_time": 1.9092731475830078
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
