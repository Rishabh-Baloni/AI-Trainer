"""
FastAPI Backend for AI Fitness Trainer
Main application entry point
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="AI Fitness Trainer API",
    description="Backend API for AI-powered virtual fitness trainer",
    version="1.0.0"
)

# CORS middleware for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Health check endpoint
    """
    return {
        "message": "AI Fitness Trainer API is running",
        "version": "1.0.0",
        "status": "healthy"
    }


@app.get("/api/health")
async def health_check():
    """
    API health check
    """
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
