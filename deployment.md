# 🚀 Deployment Guide — Nexus AI Assistant

Two separate Vercel projects from the same GitHub repo:
- **Project 1** → deploys the `backend/` folder as a Python serverless API
- **Project 2** → deploys the `frontend/` folder as a static site

---

## 🏗️ System Architecture Flow

Here is how data flows securely through the technologies used in this system:

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

### 2.1 — Import the repo into Vercel

1. Log into your Vercel account.
2. From the Vercel dashboard horizon, click the **"Add New..."** button in the top right corner and select **"Project"**.
3. In the "Import Git Repository" section, find `Nexus-AI-Assistant` in the list (you may need to connect your GitHub account if you haven't).
4. Click the **"Import"** button next to the repository.

### 2.2 — Set the Root Directory to `backend`

> [!IMPORTANT]
> This is the critical step. Vercel will only see and deploy the `backend/` folder. If you skip this, Vercel won't know how to run Python.

On the "Configure Project" screen, follow exactly these steps:

1. **Project Name**: You can name it `nexus-backend`.
2. **Framework Preset**: Click this dropdown and select **Other** (it may auto-detect this).
3. **Root Directory**: Click the **"Edit"** button. A file browser will pop up. Click the radio button next to the `backend` folder, then click **"Continue"**. 
4. Open the **"Build and Output Settings"** toggle.
5. In the **Install Command** field, toggle "Override" and type exactly: `pip install -r requirements.txt`

### 2.3 — Add environment variables

Still on the "Configure Project" screen (before clicking Deploy), look for the **"Environment Variables"** dropdown area below the Build and Output settings. 

1. Click the toggle to expand **Environment Variables**.
2. For each key below, paste the variable name into "Key" and your exact key into "Value".
3. Click the **"Add"** button for each one until all keys are added to the list below it.

| Key | Value |
|---|---|
| `OPENWEATHER_API_KEY` | your OpenWeatherMap key |
| `NEWS_API_KEY` | your NewsAPI key |
| `OPENAI_API_KEY` | your **Groq** key (primary LLM) |
| `FALLBACK_API_KEY` | your OpenAI key *(optional)* |
| `ANTHROPIC_API_KEY` | your Anthropic key *(optional)* |

### 2.4 — Click Deploy

1. After adding all your keys, scroll down to the very bottom of the "Configure Project" panel.
2. Click the large blue **"Deploy"** button.
3. Wait ~1–2 minutes while Vercel builds the Python endpoints. Once it succeeds, Vercel will direct you to a success page.
4. Click "Continue to Dashboard".
5. In your Vercel project dashboard, look at the top for the "Domains" section to find your live backend URL (it will look like `https://nexus-backend-xxx.vercel.app`).

**Copy this URL — you absolutely need it for Step 3.**

### 2.5 — Verify the backend

| Check | URL | Expected |
|---|---|---|
| ✅ Health | `https://nexus-backend-xxx.vercel.app/health` | `{"status": "ok"}` |
| ✅ API docs | `https://nexus-backend-xxx.vercel.app/docs` | FastAPI Swagger UI |

---

## Step 3 — Connect the Frontend to the Backend

Before deploying the frontend, you must update the static HTML files to point at your live, cloud-hosted backend.

1. Open the file `frontend/index.html` locally in your code editor (e.g., VS Code).
2. Scroll to the very beginning of the script tag (around line 10), and find this exact code:
   ```html
    <script>
        // Automatically switch between localhost and the deployed backend.
        if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") {
            window.BACKEND_URL = "http://localhost:8001";
        } else {
            // ✏️ Replace this with your actual live backend URL from step 2.4 (No trailing slash)
            window.BACKEND_URL = "https://your-backend.vercel.app";
        }
    </script>
   ```
3. Inside the `else` block, replace `https://your-backend.vercel.app` with your actual live backend URL from step 2.4. *Make sure you do NOT include `/api` or a trailing slash at the end of the URL!*
   **Correct Example:** `window.BACKEND_URL = "https://nexus-backend-xyz.vercel.app";`
4. Save the file.
5. Commit and push the updated file to GitHub so Vercel can see the change:
   ```bash
   git add frontend/index.html
   git commit -m "Point frontend to live backend URL"
   git push origin main
   ```

---

## Step 4 — Deploy the Frontend

### 4.1 — Import the repo again (new project)

1. Go back to your main Vercel dashboard.
2. Click **"Add New..."** -> **"Project"**.
3. **Import the exact same `Nexus-AI-Assistant` repository** again from your GitHub list.
4. Vercel will allow you to create a **second separate project** out of the same repository.

### 4.2 — Set the Root Directory to `frontend`

Follow exactly these steps on the Configure screen:

1. **Project Name**: Name it `nexus-frontend`.
2. **Root Directory**: Click the **"Edit"** button. Select the `frontend` folder from the popup list and click **"Continue"**.
3. **Framework Preset**: Leave it as **Other**.
4. **Build and Output Settings**: Leave these completely blank. No build command is needed.

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
