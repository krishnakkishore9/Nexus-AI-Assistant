# 04 - Caching & Data Persistence

## ⚡ 1. Caching Strategy
To minimize latency and API costs, a caching layer is implemented between the Backend and External APIs.

### A. Cache Layers
*   **Primary**: **Redis** (Highly Recommended for production).
*   **Fallback**: In-memory dictionary (Python `dict` with TTL logic).

### B. TTL (Time To Live) Configuration
| Data Type | Cache Duration | Reason |
| :--- | :--- | :--- |
| **Weather** | 10 Minutes | Forecasts change slowly but need updates. |
| **News** | 5 Minutes | News cycles are rapid. |
| **Search** | 1 Hour | General web results are relatively stable. |

## 📊 2. Data Models (Pydantic)

### User Model
```python
class User(BaseModel):
    id: str
    username: str
    email: str
    is_active: bool
```

### Unified Response Model
All `/api/query` responses must follow this structure for the frontend:
```json
{
  "status": "success",
  "query": "What's the weather in Tokyo?",
  "data": {
    "weather": { ... },
    "news": [ ... ],
    "web_results": [ ... ]
  },
  "metadata": {
    "tokens_used": 150,
    "source": "cache | live",
    "execution_time_ms": 450
  }
}
```

## ❗ 3. Error Handling
The backend must return consistent error objects:
```json
{
  "status": "error",
  "error": {
    "code": "API_TIMEOUT",
    "message": "The weather service is currently unavailable.",
    "details": "..."
  }
}
```

---
> [!IMPORTANT]
> Always implement a "Stale-While-Revalidate" approach for caching to ensure the user gets a fast response even if data is slightly old.
