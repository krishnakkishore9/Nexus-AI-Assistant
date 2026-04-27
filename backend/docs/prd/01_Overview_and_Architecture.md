# 01 - Project Overview & Architecture

## 📋 1. Project Summary
The **Full-Stack MCP Tool Calling App** is an intelligent assistant that leverages the Model Context Protocol (MCP) to interact with external APIs (Weather, News, Search). The goal is to provide a seamless natural language interface where users can ask complex, multi-intent questions and receive aggregated, structured results.

## 🎯 2. Primary Objectives
*   **Intelligent Orchestration**: Use an LLM-based agent to dynamically select and chain tools.
*   **Performance**: Implement caching to minimize external API costs and latency.
*   **User Experience**: Deliver a high-end, responsive UI with modern aesthetics (Glassmorphism).
*   **Security**: Ensure all user data and API interactions are secured via JWT and environment variables.

## 🏗️ 3. High-Level Architecture
The application consists of three main tiers:

### A. Frontend (Client Layer)
*   **Tech**: HTML5, Tailwind CSS, Vanilla JavaScript.
*   **Role**: Handles user input, displays results, manages authentication tokens locally, and triggers animations.

### B. Backend (Orchestration Layer)
*   **Tech**: FastAPI (Python).
*   **Role**: Serves the API, handles authentication middleware, manages sessions, and interfaces with the MCP Layer.

### C. MCP Layer (Intelligence Layer)
*   **Tech**: LangChain / OpenAI / Groq.
*   **Role**: The "Brain" of the app. It parses natural language, decides which tools to call, and formats the final output.

## 🛠️ 4. External Integrations
1.  **OpenWeatherMap API**: For real-time weather data.
2.  **NewsAPI.org**: For fetching headlines and top stories.
3.  **DuckDuckGo/SerpAPI**: For wide-web search capabilities.

---
> [!NOTE]
> This document serves as the foundation for the entire project lifecycle.
