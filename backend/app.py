"""
FastAPI Backend for AI Fitness Trainer
Main application entry point
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Import routers
from routes.workout import router as workout_router
from routes.diet import router as diet_router
from routes.auth import router as auth_router
from routes.pose import router as pose_router
from routes.analytics import router as analytics_router

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

# Include routers
app.include_router(workout_router)
app.include_router(diet_router)
app.include_router(auth_router)
app.include_router(pose_router)
app.include_router(analytics_router)


@app.get("/")
async def root():
    """
    Health check endpoint
    """
    return {
        "message": "AI Fitness Trainer API is running",
        "version": "1.0.0",
        "status": "healthy",
        "endpoints": {
            "workout": "/api/workout",
            "diet": "/api/diet",
            "auth": "/api/auth",
            "pose": "/api/pose",
            "analytics": "/api/analytics",
            "docs": "/docs"
        }
    }


@app.get("/api/health")
async def health_check():
    """
    API health check
    """
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
