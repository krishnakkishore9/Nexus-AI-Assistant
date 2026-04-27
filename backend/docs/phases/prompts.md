# 🤖 Implementation Prompts for AI Development Agent

Use these prompts sequentially to guide your development agent through the build process. Each prompt is designed to be self-contained but relies on the progress of previous phases.

---

## 🏁 Phase 1: Environment Setup & Foundation
**Prompt:**
> "Initialize a new FastAPI project for a Full-Stack MCP Tool Calling App. 
> 1. Set up a virtual environment and a `.gitignore` file.
> 2. Create a `requirements.txt` with `fastapi`, `uvicorn`, `python-dotenv`, and `pydantic`.
> 3. Create a basic directory structure: `/backend/app/main.py`, `/backend/app/core/config.py`, and a `/frontend` placeholder.
> 4. Implement a root `GET /health` endpoint that returns `{"status": "ok"}`.
> 5. Ensure `.env` loading is functional in `config.py`.
>
> **CRITICAL**: Once complete and verified, ask me: 'Phase 1 is complete. Ready to proceed to Phase 2: Authentication?'"

---

## 🔐 Phase 2: Authentication & User Management
**Link to Previous**: Builds on the FastAPI structure and `config.py` from Phase 1.
**Prompt:**
> "Implement an Authentication system in the existing FastAPI backend.
> 1. Set up a SQLite database and a SQLAlchemy `User` model (`id`, `username`, `email`, `hashed_password`).
> 2. Use `passlib[bcrypt]` for password hashing and `python-jose` for JWT generation.
> 3. Create endpoints: `POST /api/auth/signup`, `POST /api/auth/login` (returns JWT), and `GET /api/auth/me` (protected).
> 4. Add the `get_current_user` dependency to secure routes.
>
> **CRITICAL**: Once code is written and endpoints are tested, ask me: 'Phase 2 is complete. Ready to proceed to Phase 3: MCP Tool Implementation?'"

---

## ⚙️ Phase 3: MCP Layer - Core Tools
**Link to Previous**: These tools will be imported into the backend routes established in Phase 1/2.
**Prompt:**
> "Develop three standalone tool functions for the backend:
> 1. `get_weather(city_name)`: Connect to OpenWeatherMap API and return structured weather data.
> 2. `get_news(topic)`: Connect to NewsAPI.org and return a list of top 3 articles.
> 3. `web_search(query)`: Implement a DuckDuckGo search using LangChain's community tools.
> Ensure all API keys are fetched from environment variables.
>
> **CRITICAL**: Once the tools are verified with a test script, ask me: 'Phase 3 is complete. Ready to proceed to Phase 4: Agent Orchestration?'"

---

## 🧠 Phase 4: MCP Layer - Agent Orchestration
**Link to Previous**: Uses the tool functions from Phase 3 and the logic patterns from Phase 1.
**Prompt:**
> "Integrate the tools from Phase 3 into a LangChain Agent.
> 1. Use an LLM (GPT-4o/Groq) and define the tools using `StructuredTool`.
> 2. Set up a `SystemPrompt` that instructs the agent on multi-tool reasoning and structured JSON output.
> 3. Implement `ConversationBufferMemory` to maintain context.
> 4. Create an `AgentExecutor` to handle the reasoning loop.
>
> **CRITICAL**: Once the agent is capable of handling combined queries like 'Weather in NYC and tech news', ask me: 'Phase 4 is complete. Ready to proceed to Phase 5: API Integration & Caching?'"

---

## ⚡ Phase 5: Backend API Integration & Caching
**Link to Previous**: Connects the Agent (Phase 4) to the REST API (Phase 1) and protects it with Auth (Phase 2).
**Prompt:**
> "Finalize the backend by creating the query endpoint.
> 1. Implement `POST /api/query` which accepts a user prompt and returns the Agent's structured output.
> 2. Wrap this route in the `get_current_user` JWT dependency.
> 3. Implement a Redis or In-memory caching layer with TTL (10m for weather, 5m for news).
> 4. Ensure the response format matches the `Unified Response Model` from the PRD.
>
> **CRITICAL**: Once the endpoint is functional and cached responses are verified, ask me: 'Phase 5 is complete. Ready to proceed to Phase 6: Frontend Layout?'"

---

## 🎨 Phase 6: Frontend - Layout & Design System
**Link to Previous**: This is the client for the API developed in Phases 1-5.
**Prompt:**
> "Start the frontend development in the `/frontend` directory.
> 1. Create `index.html`, `style.css`, and `script.js`.
> 2. Use Tailwind CSS to implement a 'Glassmorphic Dark Mode'.
> 3. Build the layout: A sticky Navbar, a centered Hero Search section, and a Results Grid container.
> 4. Add CSS classes for glass panels and the deep navy background.
>
> **CRITICAL**: Once the visual shell is ready and responsive, ask me: 'Phase 6 is complete. Ready to proceed to Phase 7: Frontend Feature Integration?'"

---

## 🧱 Phase 7: Frontend - Feature Integration
**Link to Previous**: Connects the UI (Phase 6) to the API Endpoints (Phase 2 & 5).
**Prompt:**
> "Implement the logic in `script.js`.
> 1. Handle user authentication (Login/Signup fetch calls and token storage).
> 2. Implement the search query flow: send the prompt to `/api/query` with the Bearer token.
> 3. Create rendering functions to dynamically inject Weather cards, News headlines, and Search results into the grid.
> 4. Handle loading states and show simple error alerts.
>
> **CRITICAL**: Once the app is fully functional and displaying data, ask me: 'Phase 7 is complete. Ready to proceed to Phase 8: Polish & Animations?'"

---

## ✨ Phase 8: Polish & Animations
**Link to Previous**: Adds aesthetic layers to the functional UI from Phase 7.
**Prompt:**
> "Enhance the user experience with animations and motion.
> 1. Add staggered fade-in animations for result cards when they appear.
> 2. Implement Skeleton Loader placeholders to show during API fetches.
> 3. Add hover effects and transition glows for the search input and buttons.
> 4. Fine-tune mobile responsiveness.
>
> **CRITICAL**: Once the animations are smooth and the UI feels premium, ask me: 'Phase 8 is complete. Ready to proceed to the final Phase 9?'"

---

## 🚀 Phase 9: Reliability & Deployment
**Link to Previous**: Hardens the entire codebase produced in Phases 1-8.
**Prompt:**
> "Conduct final security and reliability checks.
> 1. Implement rate limiting on the backend `/api/query` endpoint.
> 2. Add global error boundaries in the frontend.
> 3. Verify cross-browser compatibility and conduct a full E2E test.
> 4. Prepare a `Dockerfile` or `Procfile` for production deployment.
>
> **CRITICAL**: Once the project is production-ready, ask me: 'Phase 9 is complete. The application is ready for deployment. Would you like to review the final documentation?'"
