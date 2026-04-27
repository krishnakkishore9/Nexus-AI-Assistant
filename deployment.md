# 🚀 Deployment Guide — Nexus AI Assistant

Two separate Vercel projects from the same GitHub repo:
- **Project 1** → deploys the `backend/` folder as a Python serverless API
- **Project 2** → deploys the `frontend/` folder as a static site

---

## 📋 Prerequisites

- [ ] [GitHub](https://github.com) account
- [ ] [Vercel](https://vercel.com) account (free tier is fine)
- [ ] API keys:
  - [Groq](https://console.groq.com) — primary LLM (free tier)
  - [OpenWeatherMap](https://openweathermap.org/api) — weather tool (free tier)
  - [NewsAPI](https://newsapi.org) — news tool (free tier)
  - *(Optional)* [OpenAI](https://platform.openai.com) — LLM fallback
  - *(Optional)* [Anthropic](https://console.anthropic.com) — LLM fallback

---

## Step 1 — Push the Project to GitHub

1. Go to [github.com/new](https://github.com/new) and create a repository:
   - Name: `Nexus-AI-Assistant`
   - Visibility: **Private** (protects your API keys)
   - Do **not** initialize with a README

2. Push from your project root:

   ```bash
   git init
   git add .
   git commit -m "Initial commit — Nexus AI Assistant"
   git branch -M main
   git remote add origin https://github.com/krishnakkishore9/Nexus-AI-Assistant.git
   git push -u origin main
   ```

3. Confirm `.env` is **not** visible on GitHub — it is excluded by `.gitignore`.

---

## Step 2 — Deploy the Backend

### 2.1 — Import the repo

1. Go to [vercel.com/new](https://vercel.com/new) and click **"Import Git Repository"**.
2. Select your `nexus-ai-assistant` repo.

### 2.2 — Set the Root Directory to `backend`

> [!IMPORTANT]
> This is the critical step. Vercel will only see and deploy the `backend/` folder.

On the configuration screen:

| Setting | Value |
|---|---|
| **Root Directory** | `backend` |
| **Framework Preset** | Other |
| **Build Command** | *(leave blank)* |
| **Output Directory** | *(leave blank)* |
| **Install Command** | `pip install -r requirements.txt` |

### 2.3 — Add environment variables

| Variable | Value |
|---|---|
| `OPENWEATHER_API_KEY` | your OpenWeatherMap key |
| `NEWS_API_KEY` | your NewsAPI key |
| `OPENAI_API_KEY` | your **Groq** key (primary LLM) |
| `FALLBACK_API_KEY` | your OpenAI key *(optional)* |
| `ANTHROPIC_API_KEY` | your Anthropic key *(optional)* |

### 2.4 — Deploy

Click **"Deploy"**. Wait ~1–2 minutes. You'll get a backend URL like:
```
https://nexus-backend-xxx.vercel.app
```
**Copy this URL — you need it for Step 3.**

### 2.5 — Verify the backend

| Check | URL | Expected |
|---|---|---|
| ✅ Health | `https://nexus-backend-xxx.vercel.app/health` | `{"status": "ok"}` |
| ✅ API docs | `https://nexus-backend-xxx.vercel.app/docs` | FastAPI Swagger UI |

---

## Step 3 — Connect the Frontend to the Backend

Before deploying the frontend, update it to point at your live backend URL.

1. Open `frontend/index.html` and find this line:
   ```html
   <script>window.BACKEND_URL = "https://your-backend.vercel.app";</script>
   ```
2. Replace `https://your-backend.vercel.app` with your actual backend URL from Step 2.4.
3. Commit and push:
   ```bash
   git add frontend/index.html
   git commit -m "Point frontend to deployed backend URL"
   git push origin main
   ```

---

## Step 4 — Deploy the Frontend

### 4.1 — Import the repo again (new project)

1. Go to [vercel.com/new](https://vercel.com/new) and **import the same repo** again.
2. Vercel will create a **second separate project** from the same repository.

### 4.2 — Set the Root Directory to `frontend`

| Setting | Value |
|---|---|
| **Root Directory** | `frontend` |
| **Framework Preset** | Other |
| **Build Command** | *(leave blank)* |
| **Output Directory** | *(leave blank)* |
| **Install Command** | *(leave blank)* |

> No environment variables needed for the frontend — it's pure HTML/CSS/JS.

### 4.3 — Deploy

Click **"Deploy"**. You'll get a frontend URL like:
```
https://nexus-frontend-xxx.vercel.app
```

---

## Step 5 — Verify the Full Stack

Open the frontend URL and test:

| Check | How | Expected |
|---|---|---|
| ✅ UI loads | Visit `https://nexus-frontend-xxx.vercel.app` | Nexus chat interface |
| ✅ Query works | Type a question and submit | AI response with tool data |
| ✅ Weather | Ask "Weather in London" | Real-time weather data |
| ✅ News | Ask "latest tech news" | News headlines |

---

## Step 6 — Custom Domains *(optional)*

Repeat for each Vercel project under **Settings → Domains**:
- Backend: e.g. `api.nexus.yourdomain.com`
- Frontend: e.g. `nexus.yourdomain.com`

If you use a custom domain for the backend, update `window.BACKEND_URL` in `frontend/index.html` to match.

---

## 🔁 Redeployments

Both Vercel projects watch the same GitHub repo. Any push to `main` triggers automatic redeployment of **both** projects:

```bash
git add .
git commit -m "Your change"
git push origin main
```

---

## 🛠️ Running Locally

```bash
# Terminal 1 — Backend (from the backend/ directory)
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload

# Terminal 2 — Frontend
cd frontend
python -m http.server 3000
```

| Service | Local URL |
|---|---|
| Frontend | `http://localhost:3000` |
| Backend API | `http://localhost:8001` |
| Swagger Docs | `http://localhost:8001/docs` |

> [!NOTE]
> For local dev, `frontend/js/api.js` falls back to `http://localhost:8001` automatically when `window.BACKEND_URL` is set to `your-backend.vercel.app`. To test locally, temporarily change `index.html` to set `window.BACKEND_URL = "http://localhost:8001"`, or just leave it — the fallback handles it if the production URL is unreachable locally.

---

## 🐛 Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| Backend 500 error | Missing env var | Vercel → Backend Project → Settings → Env Vars |
| Frontend queries fail (CORS) | Backend URL wrong | Check `window.BACKEND_URL` in `index.html` matches deployed backend |
| `ModuleNotFoundError: app` | Root Directory not set to `backend` | Vercel → Backend Project → Settings → Root Directory = `backend` |
| Cold start timeout | Vercel free plan | Upgrade or reduce import weight in `main.py` |
| LLM no response | Wrong Groq key | `OPENAI_API_KEY` should contain your Groq key |
