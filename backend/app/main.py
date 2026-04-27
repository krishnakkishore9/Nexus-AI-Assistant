from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.core.limiter import limiter

from app.core.config import get_settings
from app.api.query import router as query_router

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="A Public AI Assistant leveraging MCP and Tool Calling",
    version="1.0.0"
)

# Apply Rate Limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(query_router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# NOTE: StaticFiles mount removed — frontend is served by Vercel's CDN directly.
# For local development, open frontend/index.html directly in a browser
# or serve it with: python -m http.server 3000 --directory frontend

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
