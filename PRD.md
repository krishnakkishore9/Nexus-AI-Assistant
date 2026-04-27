Here’s your **clean, updated Project Requirement Document (PRD)** in Markdown with the requested sections removed.

---

# 📄 Full-Stack MCP Tool Calling App

### (Weather + News + Search with Advanced Features)

---

## 🧩 1. Project Overview

Build a **full-stack AI-powered web application** that integrates multiple external tools (Weather, News, Search APIs) via an advanced **MCP (Model Context Protocol)** layer.

The system will:

* Accept natural language queries
* Dynamically decide which tools to call
* Aggregate results
* Present structured outputs in a modern UI

---

## 🎯 2. Objectives

* Integrate at least **3 external APIs**
* Implement **advanced MCP orchestration**
* Provide **secure authentication**
* Deliver **fast, responsive UI**
* Ensure **fault tolerance and reliability**

---

## 🏗️ 3. System Architecture

```plaintext
Frontend (HTML + Tailwind + JS)
        ↓
FastAPI Backend
        ↓
Advanced MCP Layer (Agent + Tools + Memory)
        ↓
-----------------------------------------
| Weather API | News API | Search API   |
-----------------------------------------
        ↓
Cache Layer (Redis / In-Memory)
```

---

## ⚙️ 4. Tech Stack

### 🔹 Frontend

* HTML5
* Tailwind CSS
* Vanilla JavaScript

### 🔹 Backend

* FastAPI (Python)
* Uvicorn (ASGI server)

### 🔹 MCP / AI Layer

* LangChain (Agent + Tool Calling)
* Optional LLM (OpenRouter / Groq)

### 🔹 APIs

* Weather API (OpenWeatherMap)
* News API (NewsAPI.org)
* Search API (DuckDuckGo / SerpAPI)

### 🔹 Caching

* Redis (preferred) OR in-memory cache

### 🔹 Authentication

* JWT-based authentication

---

## 🔐 5. Authentication Requirements

### Features

* User Signup / Login
* JWT Token-based authentication
* Protected API routes

### Flow

```plaintext
User Login → Backend verifies → JWT issued → Stored in frontend
→ Sent in headers for every request
```

### Backend Example

```python
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    return {"message": "Authorized"}
```

---

## 🧠 6. Advanced MCP Design

### Components

#### 1. Tool Definitions

* Weather Tool
* News Tool
* Search Tool

#### 2. Agent Capabilities

* Multi-step reasoning
* Intelligent tool selection
* Tool chaining
* Response aggregation

#### 3. Memory (Optional but Recommended)

* Maintain conversation history
* Context-aware responses

### Example Flow

```plaintext
User Query:
"Weather in Delhi and AI news"

Agent:
→ Detects multiple intents  
→ Calls Weather Tool  
→ Calls News Tool  
→ Combines structured results  
```

---

## 📦 7. Structured Output Design

### Backend Response Format

```json
{
  "status": "success",
  "data": {
    "weather": {
      "city": "Delhi",
      "temperature": "32°C",
      "condition": "Sunny"
    },
    "news": [
      {
        "title": "AI breakthrough",
        "url": "..."
      }
    ],
    "search": []
  },
  "error": null
}
```

### Benefits

* Easy frontend rendering
* Clear data separation
* Scalable response structure

---

## ⚡ 8. Caching Layer

### Purpose

* Reduce redundant API calls
* Improve response time

### Strategy

* Weather → Cache for 10 minutes
* News → Cache for 5 minutes
* Search → Cache for 15 minutes

### Example (In-Memory)

```python
cache = {}

def get_cached(key):
    return cache.get(key)

def set_cache(key, value):
    cache[key] = value
```

---

## ❗ 9. Error Handling

### Error Types

* External API failures
* Invalid user input
* Timeout issues
* Authentication failures

### Response Format

```json
{
  "status": "error",
  "data": null,
  "error": {
    "message": "API unavailable",
    "code": 503
  }
}
```

### Best Practices

* Wrap all API/tool calls in try/except
* Return meaningful error messages
* Log errors for debugging
* Use fallback responses where possible

---

## 🎨 10. Frontend UI Requirements

### Layout Components

* Header (Application title)
* Input field (user query)
* Submit button
* Results section with:

  * Weather card
  * News list
  * Search results

---

## 💅 11. Tailwind CSS UI Design

### Example Layout

```html
<div class="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center">
  <h1 class="text-3xl font-bold mb-6">Smart Assistant</h1>

  <input id="query"
    class="p-3 w-96 rounded-lg text-black"
    placeholder="Ask something..." />

  <button onclick="sendQuery()"
    class="mt-4 px-6 py-2 bg-blue-500 rounded-lg hover:bg-blue-600">
    Search
  </button>

  <div id="loader" class="hidden mt-4">Loading...</div>

  <div id="results" class="mt-6 w-full max-w-2xl"></div>
</div>
```

---

## 🔄 12. Loading & Animations

### Features

* Display loader during API calls
* Smooth UI transitions
* Fade-in result rendering

### Example

```javascript
function showLoader() {
  document.getElementById("loader").classList.remove("hidden");
}

function hideLoader() {
  document.getElementById("loader").classList.add("hidden");
}
```

---

## 🔌 13. API Endpoints

### POST `/login`

* Authenticate user
* Returns JWT token

### POST `/query`

* Accepts user query
* Returns structured response

### GET `/health`

* Health check endpoint

---

## 🔒 14. Security Considerations

* Store API keys in environment variables
* Use HTTPS for communication
* Validate and sanitize inputs
* Implement rate limiting (optional)

---

## ✅ 15. Success Criteria

* All three APIs integrated successfully
* MCP agent correctly routes queries
* Authentication is functional
* UI is responsive and modern
* Error handling is robust
* Caching improves performance

---

## 🧠 Final Note

This system forms the foundation of a **scalable AI-powered assistant platform**, capable of intelligent tool orchestration and structured data delivery.

---

If you want next, I can:
✅ Convert this into a **downloadable .md file**
✅ Generate **complete working code (FastAPI + UI)**
✅ Or design a **high-end dashboard UI version**
