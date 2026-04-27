# Phase 7: Frontend - Feature Integration

## 🎯 Goal
Connect the UI to the backend and handle data rendering.

## 🛠️ Tasks

### 1. API Client
- Create a `api.js` utility using `fetch` or `axios`.
- Handle JWT token management (Save to `localStorage` on login, attach to `Authorization` header).

### 2. Search Integration
- Capture user input from the search field.
- Send a POST request to `/api/query`.
- Handle "Loading" states (show a spinner or skeleton loader).

### 3. Dynamic Rendering
- Create functions to render various card types:
  - `renderWeather(data)`
  - `renderNews(articles)`
  - `renderSearchResults(results)`
- Inject these into the Results Grid div.

### 4. Error Notifications
- Implement a "Toast" or alert system to show backend errors (e.g., "Invalid Token", "API Down").

## ✅ Success Criteria
- [ ] User can log in and remain authenticated across refreshes.
- [ ] Submitting a query displays real data from the backend.
- [ ] Weather icons and news thumbnails render correctly.
