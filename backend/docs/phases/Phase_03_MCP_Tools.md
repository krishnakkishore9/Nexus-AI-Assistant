# Phase 3: MCP Layer - Core Tools Implementation

## 🎯 Goal
Develop the standalone tools that the AI agent will use to fetch external data.

## 🛠️ Tasks

### 1. Weather Tool (`get_weather`)
- Integrate with **OpenWeatherMap API**.
- Function should take a `city_name` (string).
- Return a structured dictionary: `{temp, humidity, conditions}`.

### 2. News Tool (`get_news`)
- Integrate with **NewsAPI.org**.
- Function should accept a `query` or `category`.
- Return a list of top 3 relevant articles: `[{title, url, description, image_url}]`.

### 3. Search Tool (`web_search`)
- Integrate with **DuckDuckGo** (using `langchain_community.tools.ddg_search`).
- Function should accept a broad search `query`.
- Return snippets and links from the web.

### 4. Unit Testing
- Create a test script to call these tools independently (without the LLM) to verify API connectivity and response parsing.

## ✅ Success Criteria
- [ ] `get_weather('London')` returns valid JSON data.
- [ ] `get_news('Technology')` returns a list of news articles.
- [ ] `web_search('LangChain tutorial')` returns search snippets.
