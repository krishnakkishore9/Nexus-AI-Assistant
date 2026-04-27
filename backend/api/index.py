# backend/api/index.py
# Vercel Python serverless entry point.
# When Vercel's Root Directory is set to `backend/`, this file sits at
# the top of the project from Vercel's perspective, so imports use `app.*`

from app.main import app  # noqa: F401
