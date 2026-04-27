from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Project settings loaded from environment variables / .env file
    """
    APP_NAME: str = "Nexus AI Assistant"
    DEBUG: bool = False

    # External Tool APIs
    OPENWEATHER_API_KEY: str = ""
    NEWS_API_KEY: str = ""

    # LLM Orchestrators (Groq primary, OpenAI/Anthropic fallback)
    OPENAI_API_KEY: str = ""          # Primary — put your Groq key here
    FALLBACK_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None

    class Config:
        env_file = ("../.env", ".env")
        extra = "ignore"

# Workaround for Pydantic V2
Settings.model_rebuild()

def get_settings():
    return Settings()
