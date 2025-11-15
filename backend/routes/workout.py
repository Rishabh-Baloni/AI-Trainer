"""
Workout & Exercise API Routes
Exercise database from ExerciseDB API + Workout plan generation
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/workout", tags=["Workout"])

EXERCISEDB_API_KEY = os.getenv("EXERCISEDB_API_KEY")
EXERCISEDB_API_HOST = os.getenv("EXERCISEDB_API_HOST")


# ========== EXERCISE DATABASE ENDPOINTS ==========

@router.get("/exercises")
async def get_exercises(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Get list of exercises from ExerciseDB API
    """
    try:
        url = f"https://{EXERCISEDB_API_HOST}/api/v1/exercises"
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        params = {
            "limit": limit,
            "offset": offset
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            
            return {
                "success": True,
                "total": len(data.get("data", [])),
                "exercises": data.get("data", [])
            }
    
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exercises: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/exercises/search")
async def search_exercises(
    query: str = Query(..., min_length=1),
    limit: int = Query(20, ge=1, le=100)
):
    """
    Search exercises by name
    """
    try:
        url = f"https://{EXERCISEDB_API_HOST}/api/v1/exercises/search"
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        params = {
            "search": query,
            "limit": limit
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            
            return {
                "success": True,
                "query": query,
                "total": len(data.get("data", [])),
                "exercises": data.get("data", [])
            }
    
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error searching exercises: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/exercises/bodypart/{bodypart}")
async def get_exercises_by_bodypart(
    bodypart: str,
    limit: int = Query(100, ge=1, le=200)
):
    """
    Get exercises filtered by body part (client-side filtering)
    """
    try:
        # Fetch all exercises and filter client-side since API doesn't support bodypart filtering
        url = f"https://{EXERCISEDB_API_HOST}/api/v1/exercises"
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        params = {
            "limit": 200,  # Get more exercises to filter from
            "offset": 0
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            
            # Filter exercises by body part
            exercises = data.get("data", [])
            bodypart_upper = bodypart.upper()
            
            filtered_exercises = [
                ex for ex in exercises 
                if bodypart_upper in [bp.upper() for bp in ex.get("bodyParts", [])]
            ][:limit]
            
            return {
                "success": True,
                "bodypart": bodypart,
                "total": len(filtered_exercises),
                "exercises": filtered_exercises
            }
    
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exercises: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/exercises/equipment/{equipment}")
async def get_exercises_by_equipment(
    equipment: str,
    limit: int = Query(100, ge=1, le=200)
):
    """
    Get exercises filtered by equipment (client-side filtering)
    """
    try:
        # Fetch all exercises and filter client-side since API doesn't support equipment filtering
        url = f"https://{EXERCISEDB_API_HOST}/api/v1/exercises"
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        params = {
            "limit": 200,  # Get more exercises to filter from
            "offset": 0
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            
            # Filter exercises by equipment
            exercises = data.get("data", [])
            equipment_upper = equipment.upper()
            
            filtered_exercises = [
                ex for ex in exercises 
                if equipment_upper in [eq.upper() for eq in ex.get("equipments", [])]
            ][:limit]
            
            return {
                "success": True,
                "equipment": equipment,
                "total": len(filtered_exercises),
                "exercises": filtered_exercises
            }
    
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exercises: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/exercises/{exercise_id}")
async def get_exercise_by_id(exercise_id: str):
    """
    Get detailed information about a specific exercise
    """
    try:
        url = f"https://{EXERCISEDB_API_HOST}/api/v1/exercises/{exercise_id}"
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            
            return {
                "success": True,
                "exercise": data
            }
    
    except httpx.HTTPError as e:
        raise HTTPException(status_code=404, detail=f"Exercise not found: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/bodyparts")
async def get_available_bodyparts():
    """
    Get list of available body parts for filtering
    """
    try:
        # Fetch exercises to extract unique body parts
        url = f"https://{EXERCISEDB_API_HOST}/api/v1/exercises"
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        params = {"limit": 100, "offset": 0}
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            
            # Extract unique body parts
            exercises = data.get("data", [])
            body_parts_set = set()
            for ex in exercises:
                for bp in ex.get("bodyParts", []):
                    body_parts_set.add(bp)
            
            body_parts = sorted(list(body_parts_set))
            
            return {
                "success": True,
                "total": len(body_parts),
                "bodyParts": body_parts
            }
    
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching body parts: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/equipments")
async def get_available_equipments():
    """
    Get list of available equipment types for filtering
    """
    try:
        # Fetch exercises to extract unique equipment types
        url = f"https://{EXERCISEDB_API_HOST}/api/v1/exercises"
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        params = {"limit": 100, "offset": 0}
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            data = response.json()
            
            # Extract unique equipment types
            exercises = data.get("data", [])
            equipments_set = set()
            for ex in exercises:
                for eq in ex.get("equipments", []):
                    equipments_set.add(eq)
            
            equipments = sorted(list(equipments_set))
            
            return {
                "success": True,
                "total": len(equipments),
                "equipments": equipments
            }
    
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching equipments: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


# ========== WORKOUT PLAN ENDPOINTS (ML Integration Pending) ==========

class WorkoutRequest(BaseModel):
    user_id: str
    duration_minutes: int = 30
    difficulty: str = "intermediate"


@router.post("/generate")
async def generate_workout_plan(request: WorkoutRequest):
    """
    Generate personalized workout plan (ML integration pending)
    """
    return {
        "message": "Workout plan generation endpoint - ML integration pending",
        "status": "not_implemented",
        "user_id": request.user_id
    }


@router.get("/history/{user_id}")
async def get_workout_history(user_id: str):
    """
    Get user's workout history (Database integration pending)
    """
    return {
        "message": "Workout history endpoint - Database integration pending",
        "user_id": user_id
    }


@router.post("/track")
async def track_workout_session():
    """
    Track completed workout session (Database integration pending)
    """
    return {
        "message": "Workout tracking endpoint - Database integration pending"
    }
