import httpx
import logging
from duckduckgo_search import DDGS
from app.core.config import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)

async def get_weather(**kwargs):
    """Fetch real-time weather data - hardened to accept any arg name."""
    # Auto-resolve city/query/location
    city = kwargs.get("city") or kwargs.get("query") or kwargs.get("location")
    if not city:
        return "Error: No city provided."
        
    # Strip common extra words the LLM might hallucinate into the query
    city_clean = city.replace("weather", "").replace("in", "").replace("current", "").strip()
    if not city_clean:
    	city_clean = city
        
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_clean}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            data = response.json()
            if response.status_code == 200:
                output = f"Weather in {data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}. Humidity: {data['main']['humidity']}%"
                return output.encode('ascii', 'ignore').decode('ascii')
            return f"Error: {data.get('message', 'City not found')}"
        except Exception as e:
            return f"Failed to fetch weather: {str(e)}"

async def get_news(**kwargs):
    """Fetch actual news headlines - prioritized by NewsAPI, fallback to DDGS."""
    query = kwargs.get("query") or kwargs.get("city") or kwargs.get("topic")
    if not query:
        return "Error: No query provided."
        
    results = []
    
    # Priority 1: NewsAPI (more reliable)
    if settings.NEWS_API_KEY:
        try:
            logger.info(f"Attempting NewsAPI for: {query}")
            url = f"https://newsapi.org/v2/everything?q={query}&apiKey={settings.NEWS_API_KEY}&pageSize=5"
            async with httpx.AsyncClient() as client:
                response = await client.get(url, timeout=10.0)
                if response.status_code == 200:
                    data = response.json()
                    for article in data.get("articles", []):
                        title = article.get("title", "No Title")
                        desc = article.get("description", "No Description")
                        results.append(f"HEADLINE: {title}\nDETAILS: {desc}\n")
                    if results:
                        logger.info(f"NewsAPI success: {len(results)} articles found.")
                        return "\n---\n".join(results)
                else:
                    logger.warning(f"NewsAPI returned status {response.status_code}")
        except Exception as e:
            logger.warning(f"NewsAPI failed: {str(e)}")

    # Priority 2: DuckDuckGo News
    try:
        logger.info(f"Attempting DDG News fallback for: {query}")
        with DDGS() as ddgs:
            news_gen = ddgs.news(query, max_results=5)
            for r in news_gen:
                clean_title = r['title'].encode('ascii', 'ignore').decode('ascii')
                clean_body = r['body'].encode('ascii', 'ignore').decode('ascii')
                results.append(f"HEADLINE: {clean_title}\nDETAILS: {clean_body}\n")
        
        if results:
            logger.info(f"DDG News success: {len(results)} articles found.")
            return "\n---\n".join(results)
    except Exception as e:
        logger.warning(f"DDG News failed: {str(e)}")

    # Priority 3: Deep Web Search Fallback (Resilient)
    try:
        logger.info(f"Attempting Deep Search fallback for: {query}")
        with DDGS() as ddgs:
            search_gen = ddgs.text(f"latest news {query}", max_results=5)
            for r in search_gen:
                clean_body = r['body'].encode('ascii', 'ignore').decode('ascii')
                results.append(f"NEWS-INSIGHT: {clean_body}\n")
        
        if results:
            logger.info(f"Deep Search success: {len(results)} insights found.")
            return "\n---\n".join(results)
        return "No news or search results found for this topic at this moment."
    except Exception as e:
        logger.error(f"Everything failed for {query}: {str(e)}")
        if results: 
            return "\n---\n".join(results)
        return f"Service limitation: The news service is currently overloaded (403). Please try again in a few minutes or try a more general search."

async def web_search(**kwargs):
    """General web search - hardened args."""
    query = kwargs.get("query") or kwargs.get("q")
    if not query:
        return "Error: No query provided."
        
    try:
        results = []
        with DDGS() as ddgs:
            search_gen = ddgs.text(query, max_results=5)
            for r in search_gen:
                clean_body = r['body'].encode('ascii', 'ignore').decode('ascii')
                results.append(f"INFO: {clean_body}\n")
        
        return "\n---\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"
