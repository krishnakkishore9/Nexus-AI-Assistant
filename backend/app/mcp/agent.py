import json
import logging
import re
from datetime import datetime
from groq import Groq
from app.mcp.tools import get_weather, get_news, web_search
from app.core.config import get_settings

settings = get_settings()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NEXUS_SPEED")

class NativeGroqAgent:
    def __init__(self):
        self.client = Groq(api_key=settings.OPENAI_API_KEY)
        # 8b-instant is much faster and more reliable right now
        # Using the smarter 70b versatile model for much better instruction following
        self.model = "llama-3.3-70b-versatile"
        self.tools_map = {"get_weather": get_weather, "get_news": get_news, "web_search": web_search}

    async def run(self, user_input: str):
        current_date = datetime.now().strftime("%B %d, %Y")
        messages = [
            {"role": "system", "content": f"""You are 'Nexus', an elite AI assistant. Today is {current_date}. 
            
            DIRECTIONS:
            1. If you need external data (like weather, news, search), you MUST call exactly one tool using this exact format:
               [TOOL: tool_name] {{"query": "..."}} [/TOOL]
            2. Available tools are ONLY: get_weather, get_news, web_search.
            3. Do not use your own knowledge for real-time information; only report what the tool returns.
            4. If the user provides a 'RESULT', or you do not need a tool, DO NOT output a tool tag. Instead, provide a comprehensive FINAL ANSWER in markdown.
            5. Never output just a single word like "WEATHER" or "NEWS"."""},
            {"role": "user", "content": user_input}
        ]

        for i in range(5):
            try:
                # We remove the stop sequence to allow the AI to finish its final answer
                # if it's NOT calling a tool.
                completion = self.client.chat.completions.create(
                    messages=messages, model=self.model, temperature=0.0, timeout=20.0
                )
                content = (completion.choices[0].message.content or "").strip()
                logger.info(f"AI Iteration {i+1}: {content}")

                # Pattern detection for tool calls
                match = re.search(r"\[TOOL:\s*([^\]]+)\]\s*({.*?})\s*\[/TOOL\]", content, re.DOTALL)
                
                if not match:
                    # If no tool tag, it's either the final answer or a refusal
                    if i == 0:
                        # Force a search on the first pass if it tries to be lazy
                        messages.append({"role": "user", "content": "Please use a tool to get real-time info before answering."})
                        continue
                    return content

                f_name = match.group(1).strip()
                f_args_str = match.group(2).strip()
                
                if f_name in self.tools_map:
                    try:
                        f_args = json.loads(f_args_str)
                        # Ensure we don't repeat the same search
                        # res = await self.tools_map[f_name](**f_args)
                        # Actually, we should just run it.
                        res = await self.tools_map[f_name](**f_args)
                        
                        messages.append({"role": "assistant", "content": content})
                        messages.append({"role": "user", "content": f"RESULT: {res}\n\nBased on this information, provide the final answer to the user."})
                        continue
                    except Exception as e:
                        messages.append({"role": "user", "content": f"Tool error: {str(e)}. Try again with correct JSON."})
                        continue
                else:
                    messages.append({"role": "user", "content": f"Tool '{f_name}' not found. Use get_weather, get_news, or web_search."})
                    continue

            except Exception as e:
                logger.error(f"Search Loop Error: {e}")
                return "The connection is currently busy. Please try refreshing or wait a moment."

        return "Search completed with no final summary."

class AgentWrapper:
    def __init__(self, agent):
        self.agent = agent

    async def ainvoke(self, input_data: dict):
        query = input_data.get("input")
        output = await self.agent.run(query)
        return {"output": str(output)}

def get_wrapped_agent():
    return AgentWrapper(NativeGroqAgent())
