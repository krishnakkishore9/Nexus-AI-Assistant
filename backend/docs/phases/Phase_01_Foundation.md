# Phase 1: Environment Setup & Foundation

## 🎯 Goal
Establish the project structure, initialize the backend server, and configure the development environment.

## 🛠️ Tasks

### 1. Project Initialization
- Create the root project directory.
- Initialize a virtual environment: `python -m venv venv`.
- Create a `.gitignore` file (exclude `venv/`, `.env`, `__pycache__`).

### 2. Dependency Management
- Create `requirements.txt` with core packages:
  - `fastapi`
  - `uvicorn`
  - `python-dotenv`
  - `pydantic`
  - `pydantic-settings`
  - `langchain`
  - `langchain-openai` (or relevant provider)

### 3. Basic Directory Structure
```plaintext
/backend
  /app
    main.py
    /core
      config.py
    /api
      router.py
/frontend
  index.html
  style.css
  script.js
.env
```

### 4. Configuration & Health Check
- Create `backend/app/core/config.py` to load environment variables.
- Implement a basic `GET /health` endpoint in `main.py`.
- Run the server: `uvicorn backend.app.main:app --reload`.

## ✅ Success Criteria
- [ ] Backend server runs without errors.
- [ ] Accessing `http://localhost:8000/health` returns `{"status": "ok"}`.
- [ ] `.env` variables are correctly loaded into the application.
