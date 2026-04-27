# 06 - API Reference & Security Guidelines

## 🔌 1. API Endpoints

### 🔑 Authentication
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/auth/signup` | Registers a new user. | No |
| `POST` | `/api/auth/login` | Authenticates user & returns JWT. | No |
| `GET` | `/api/auth/me` | Returns current user profile. | Yes (JWT) |

### 🧠 Agent Orchestration
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/query` | Submits natural language query to agent. | Yes (JWT) |
| `GET` | `/api/history` | Retrieves user's query history. | Yes (JWT) |

### 🏥 System
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/health` | Returns server status. | No |

## 🛡️ 2. Security Best Practices

### A. Environment Variables
*   Store all API keys (OpenWeather, NewsAPI, LLM Provider) in a root `.env` file.
*   The `.env` file MUST be added to `.gitignore`.

### B. Header Security
Use `FastAPI's` middleware to set secure headers:
*   **CORS**: Only allow the application's domain.
*   **HSTS**: Enforce HTTPS.

### C. Rate Limiting
*   Limit `/api/query` to 5 requests per minute per user to prevent API abuse and cost spikes.

### D. Data Sanitization
*   Escape all user inputs before they are logged or used in database queries.
*   Strip any potential HTML tags from user inputs to prevent XSS.

---
## ✅ 3. Success Verification
- [ ] Users can successfully log in and out.
- [ ] The agent correctly handles queries like "What's the weather in Seattle and current AI news?".
- [ ] The cache successfully returns data on repeat queries within the TTL.
- [ ] The UI renders beautifully on both mobile and desktop.

---
> [!CAUTION]
> Failure to implement rate limiting on the `/api/query` endpoint can lead to significant financial costs if the application is hit by a bot.
