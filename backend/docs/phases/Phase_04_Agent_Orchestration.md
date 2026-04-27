# Phase 4: MCP Layer - Agent Orchestration

## 🎯 Goal
Combine the core tools into a reasoning agent capable of multi-intent processing.

## 🛠️ Tasks

### 1. LangChain Agent Setup
- Initialize the LLM (OpenAI, Groq, or OpenRouter).
- Define the `Tool` objects using `StructuredTool` from LangChain.

### 2. Prompt Engineering
- Create a `SystemPrompt` that instructs the agent to:
  - Be concise.
  - Call multiple tools if the user has multiple requests.
  - Always return data in a specific structured JSON format.

### 3. Agent Execution
- Implement the `AgentExecutor`.
- Enable "Verbose" mode during development to see the agent's "Thought" process.

### 4. Memory Integration
- Add `ConversationBufferMemory` to allow the user to ask follow-up questions (e.g., "What about in Paris?").

## ✅ Success Criteria
- [ ] Agent correctly identifies when to call the Weather vs. News tool.
- [ ] Complex query: "Weather in Tokyo and AI news" results in TWO tool calls.
- [ ] Agent responds with a coherent summary combining all tool data.
