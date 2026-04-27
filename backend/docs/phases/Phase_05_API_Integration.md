# Phase 5: API Integration & Caching

## 🎯 Goal
Connect the Agent to the main FastAPI server and implement performance optimizations.

## 🛠️ Tasks

### 1. The `/api/query` Endpoint
- Create the main POST endpoint to accept user queries.
- Secure it with the `get_current_user` dependency from Phase 2.

### 2. Caching Layer
- Implement a caching utility (using **Redis** or an in-memory `Store`).
- Logic: Before calling the agent, check if a similar query exists in the cache.
- TTL (Time-To-Live):
  - Weather: 10 mins
  - News: 5 mins
  - Search: 1 hour

### 3. Response Standardization
- Ensure the backend always returns the `Unified Response Model` defined in the PRD (Status, Query, Data, Metadata).

### 4. Logging & Monitoring
- Log query processing times and token usage into the console/log files.

## ✅ Success Criteria
- [ ] Repeat queries are served from the cache (indicated in metadata).
- [ ] API successfully handles concurrent requests.
- [ ] Token usage is tracked and returned in the response.
