# 🚀 Nexus AI Assistant — Full-Stack MCP Tool Calling App

**Nexus AI Assistant** is a full-stack AI chat app where you ask questions in plain English and get smart, tool-powered answers.

Ask about the weather, latest news, or anything on the web — the backend agent picks the right tools, fetches live data, and hands it to an LLM to craft a clear response. Built with FastAPI on the backend and a clean glassmorphic UI on the frontend.

---

## 📖 Overview

The application allows users to ask natural language questions through a clean, modern chat interface. Behind the scenes, an intelligent **MCP Agent** parses the query, selects the appropriate tools (weather API, news API, or DuckDuckGo web search), executes them in parallel if needed, and synthesizes a coherent response using a multi-provider LLM chain.

### 🏗️ System Architecture Flow

```text
1️⃣ User Input  ──▶ 2️⃣ Frontend (Vercel Edge Network)
[Browser]          [HTML5 / TailwindCSS / Vanilla JS]
                       │
                       ▼ 
                 3️⃣ Backend API (Vercel Serverless Functions)
                   [Python / FastAPI / Pydantic]
                       │
       ┌───────────────┴───────────────┐
       ▼                               ▼
4️⃣ Brain/Orchestrator          5️⃣ External Tools 
[Groq Llama 70b / OpenAI]       [OpenWeatherMap / NewsAPI / DuckDuckGo]
```

**Key Highlights:**

| Feature | Description |
|---|---|
| 🧠 Agentic Architecture | Custom tool-calling agent with iterative reasoning loops |
| ⚡ LLM Failover | Primary (Groq) → Fallback 1 (OpenAI) → Fallback 2 (Anthropic) |
| 🌤️ Live Weather | Real-time weather data via OpenWeatherMap API |
| 📰 News Retrieval | Global news headlines via NewsAPI + DuckDuckGo fallback |
| 🔍 Web Search | General web search via DuckDuckGo |
| 🔒 Rate Limiting | Request throttling via `slowapi` for abuse prevention |
| 🎨 Premium UI | Glassmorphic dark-mode frontend with TailwindCSS + custom CSS |
| ☁️ Vercel Ready | Frontend on CDN + backend as a Python serverless function |

---

## 📁 Project Structure

```
FStackToolCallingApp/
├── backend/                          ← Deployed as Vercel Project 1
│   ├── api/
│   │   └── index.py              # Vercel Python serverless entry point
│   ├── app/
│   │   ├── api/
│   │   │   └── query.py          # /api/query — main agent endpoint
│   │   ├── core/
│   │   │   ├── cache.py          # In-memory response cache
│   │   │   ├── config.py         # Pydantic settings (loads .env)
│   │   │   └── limiter.py        # slowapi rate limiter setup
│   │   ├── mcp/
│   │   │   ├── agent.py          # Custom Groq agent with iterative tool-calling
│   │   │   └── tools.py          # Tool definitions (weather, news, web search)
│   │   └── main.py               # FastAPI app, middleware, router registration
│   ├── docs/
│   │   ├── phases/               # Step-by-step build prompts (Phase 1–9)
│   │   └── prd/                  # Product Requirement Document sections
│   ├── tests/                    # Backend test suite
│   ├── vercel.json               # Backend Vercel config (routes all → serverless fn)
│   └── requirements.txt          # Python dependencies
├── frontend/                         ← Deployed as Vercel Project 2
│   ├── index.html                # Main UI — set BACKEND_URL here before deploying
│   ├── style.css                 # Custom CSS design tokens and animations
│   ├── script.js                 # Core UI logic (query handling, rendering)
│   └── js/
│       └── api.js                # API client — reads BACKEND_URL from index.html
├── .env                              # Local env vars — never commit
├── .gitignore
├── Dockerfile                        # For Docker/container deployments
├── deployment.md                     # Step-by-step Vercel deployment guide
├── PRD.md                            # Product Requirement Document (summary)
├── design.md                         # UI/UX design specification
└── README.md
```

---

## 🛠️ Tech Stack

### Backend

| Layer | Technology | Purpose |
|---|---|---|
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) | High-performance async Python API framework |
| **ASGI Server** | [Uvicorn](https://www.uvicorn.org/) | Lightning-fast ASGI server |
| **LLM — Primary** | [Groq](https://groq.com/) via `groq` SDK | Ultra-fast inference (Llama 3.1) |
| **LLM — Fallback 1** | [OpenAI](https://openai.com/) via `langchain-openai` | GPT-4o fallback provider |
| **LLM — Fallback 2** | [Anthropic](https://anthropic.com/) | Claude fallback provider |
| **Configuration** | [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Type-safe `.env` loading |
| **Rate Limiting** | [slowapi](https://github.com/laurentS/slowapi) | Per-IP request throttling |
| **HTTP Client** | [httpx](https://www.python-httpx.org/) | Async external API calls |
| **Web Search** | [DDGS](https://github.com/deedy5/duckduckgo_search) | DuckDuckGo search + news fallback |

### Frontend

| Layer | Technology | Purpose |
|---|---|---|
| **Structure** | HTML5 | Semantic page markup |
| **Styling** | [TailwindCSS](https://tailwindcss.com/) (CDN) + Vanilla CSS | Utility classes + custom glassmorphic design tokens |
| **Logic** | Vanilla JavaScript (ES6+) | Query submission, dynamic card rendering, loading states |
| **Typography** | Inter (Google Fonts) | Modern, clean sans-serif typeface |
| **Design Style** | Glassmorphism + Dark Mode | Premium frosted-glass UI aesthetic |

> **Note:** The frontend is a static SPA served by Vercel's CDN in production. For local dev, serve it with `python -m http.server 3000 --directory frontend`. No Node.js build step is required.

---

## ⚙️ Environment Variables

Create a `.env` file in the project root (one already exists for development). Populate it with your own keys before running in production:

```env
# External Tool APIs
OPENWEATHER_API_KEY=your_openweathermap_key   # https://openweathermap.org/api
NEWS_API_KEY=your_newsapi_key                 # https://newsapi.org

# LLM Providers (Failover Chain)
OPENAI_API_KEY=your_groq_key                  # Primary — Groq key goes here
FALLBACK_API_KEY=your_openai_fallback_key     # Fallback 1 — OpenAI sk-... (optional)
ANTHROPIC_API_KEY=your_anthropic_key          # Fallback 2 — Anthropic sk-ant-... (optional)
```

---

## 🏃 How to Run Locally

### Prerequisites

- Python **3.10+**
- `pip` (or `pip3`)
- API keys for at least one LLM provider and the tool APIs

### Step 1 — Clone the repository

```bash
git clone https://github.com/your-username/FStackToolCallingApp.git
cd FStackToolCallingApp
```

### Step 2 — Create and activate a virtual environment

```bash
# Create venv
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (macOS / Linux)
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
# Dependencies live inside backend/
cd backend
pip install -r requirements.txt
```

### Step 4 — Configure environment variables

The `.env` file is at the project root — just update the placeholder values with your real API keys.

### Step 5 — Run the backend

```bash
# Run from the backend/ directory
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

> The `--reload` flag enables hot-reloading during development.

### Step 6 — Serve the frontend (separate terminal)

```bash
# Run from the project root
python -m http.server 3000 --directory frontend
```

> [!NOTE]
> The frontend automatically targets `http://localhost:8001` when running locally. No manual edits to `api.js` needed.

### Step 7 — Access the app

| URL | Description |
|---|---|
| `http://localhost:3000` | Main UI (Nexus Assistant) |
| `http://localhost:8001/docs` | FastAPI Swagger UI (interactive API docs) |
| `http://localhost:8001/redoc` | ReDoc API documentation |
| `http://localhost:8001/health` | Health check endpoint |

---

## 🗺️ Development Phases Roadmap

This project was built using a structured implementation roadmap. All blueprints and prompts are located in the `/Development Phases` folder.

| Phase | Scope |
|---|---|
| Phase 1–2 | Core FastAPI setup and project structure |
| Phase 3–4 | MCP tool definitions (weather, news, search) and custom Groq agent |
| Phase 5 | Agent integration into `/api/query` endpoint with LLM failover |
| Phase 6–8 | Frontend — glassmorphic UI, API client, dynamic result rendering |
| Phase 9 | Finalization, rate limiting, Vercel deployment config |

> [!TIP]
> Full phase prompts and blueprints are in `backend/docs/phases/`.

> [!IMPORTANT]
> **Environment Variables**: Populate `.env` with your `OPENWEATHER_API_KEY`, `NEWS_API_KEY`, and at least one LLM key before running.

> [!NOTE]
> See `deployment.md` for the full step-by-step Vercel deployment guide.
