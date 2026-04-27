# 03 - Backend & MCP Layer Design

## ⚙️ 1. Backend Framework
The backend is built with **FastAPI**, utilizing asynchronous endpoints for high throughput and performance.

## 🧠 2. Advanced MCP (Model Context Protocol)
The core logic resides in the Tool Calling Orchestrator.

### A. Agent Configuration
*   **Engine**: LangChain `OpenAIFunctionsAgent` or `StructuredChatAgent`.
*   **LLM**: GPT-4o, Groq (Llama-3), or OpenRouter models.
*   **Memory**: `ConversationBufferMemory` to maintain context across queries.

### B. Tool Definitions
Each tool must have a clear Pydantic schema for its input.

#### 1. Weather Tool (`get_weather`)
*   **Purpose**: Get current weather for a specific city.
*   **Input**: `city_name` (string).
*   **API**: OpenWeatherMap.

#### 2. News Tool (`get_news`)
*   **Purpose**: Fetch latest news headlines.
*   **Input**: `query` (string), `category` (optional enum).
*   **API**: NewsAPI.org.

#### 3. Search Tool (`web_search`)
*   **Purpose**: Search the web for general knowledge.
*   **Input**: `search_query` (string).
*   **API**: DuckDuckGo Search (via LangChain utilities).

## 🔄 3. Orchestration Logic
1.  **Intent Detection**: The LLM analyzes the user prompt.
2.  **Parallel Execution**: If multiple intents are detected (e.g., "Weather in London and news about NASA"), the agent executes tools in parallel where possible.
3.  **Aggregation**: The agent collects all tool outputs and synthesizes a structured JSON response.

## 📁 4. Project Structure (Backend)
```plaintext
backend/
├── app/
│   ├── main.py          # FastAPI initialization
│   ├── auth/           # JWT & Auth logic
│   ├── mcp/            # LangChain Agent & Tool definitions
│   ├── api/            # Route handlers
│   └── core/           # Config and Database setup
├── .env                 # Environment variables
└── requirements.txt     # Python dependencies
```

---
> [!TIP]
> Use LangChain's `AgentExecutor` to handle retries and error handling during tool calls automatically.
