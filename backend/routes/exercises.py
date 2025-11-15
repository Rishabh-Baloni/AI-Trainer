"""
Exercise Database API Routes
Fetch exercises from ExerciseDB API
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/exercises", tags=["Exercises"])

# ExerciseDB API Configuration
EXERCISEDB_API_KEY = os.getenv("EXERCISEDB_API_KEY")
EXERCISEDB_API_HOST = os.getenv("EXERCISEDB_API_HOST", "exercisedb-api1.p.rapidapi.com")
BASE_URL = f"https://{EXERCISEDB_API_HOST}/api/v1"


@router.get("/")
async def get_exercises(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Get list of exercises from ExerciseDB API
    
    - **limit**: Number of exercises to return (1-100)
    - **offset**: Number of exercises to skip for pagination
    """
    try:
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        response = requests.get(
            f"{BASE_URL}/exercises",
            headers=headers,
            params={"limit": limit, "offset": offset},
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "data": response.json(),
            "count": len(response.json().get("exercises", [])),
            "limit": limit,
            "offset": offset
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exercises: {str(e)}")


@router.get("/search")
async def search_exercises(
    query: str = Query(..., min_length=1),
    limit: int = Query(20, ge=1, le=100)
):
    """
    Search exercises by name or description
    
    - **query**: Search term (exercise name, muscle, equipment, etc.)
    - **limit**: Maximum number of results to return
    """
    try:
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        response = requests.get(
            f"{BASE_URL}/exercises/search",
            headers=headers,
            params={"search": query, "limit": limit},
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "query": query,
            "data": response.json(),
            "count": len(response.json().get("exercises", []))
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error searching exercises: {str(e)}")


@router.get("/bodypart/{bodypart}")
async def get_exercises_by_bodypart(
    bodypart: str,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Get exercises filtered by body part
    
    - **bodypart**: Target body part (e.g., chest, back, legs, arms, shoulders, core, cardio)
    - **limit**: Number of exercises to return
    - **offset**: Number of exercises to skip for pagination
    """
    try:
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        response = requests.get(
            f"{BASE_URL}/exercises/bodypart/{bodypart.lower()}",
            headers=headers,
            params={"limit": limit, "offset": offset},
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "bodypart": bodypart,
            "data": response.json(),
            "count": len(response.json().get("exercises", [])),
            "limit": limit,
            "offset": offset
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exercises for {bodypart}: {str(e)}")


@router.get("/equipment/{equipment}")
async def get_exercises_by_equipment(
    equipment: str,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Get exercises filtered by equipment type
    
    - **equipment**: Equipment type (e.g., barbell, dumbbell, bodyweight, cable, machine)
    - **limit**: Number of exercises to return
    - **offset**: Number of exercises to skip for pagination
    """
    try:
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        response = requests.get(
            f"{BASE_URL}/exercises/equipment/{equipment.lower()}",
            headers=headers,
            params={"limit": limit, "offset": offset},
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "equipment": equipment,
            "data": response.json(),
            "count": len(response.json().get("exercises", [])),
            "limit": limit,
            "offset": offset
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exercises for {equipment}: {str(e)}")


@router.get("/{exercise_id}")
async def get_exercise_details(exercise_id: str):
    """
    Get detailed information about a specific exercise
    
    - **exercise_id**: Unique exercise identifier
    """
    try:
        headers = {
            "x-rapidapi-key": EXERCISEDB_API_KEY,
            "x-rapidapi-host": EXERCISEDB_API_HOST
        }
        
        response = requests.get(
            f"{BASE_URL}/exercises/exercise/{exercise_id}",
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "data": response.json()
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exercise details: {str(e)}")


@router.get("/filters/bodyparts")
async def get_body_parts():
    """
    Get list of all available body parts for filtering
    """
    return {
        "success": True,
        "bodyparts": [
            "back",
            "cardio",
            "chest",
            "lower arms",
            "lower legs",
            "neck",
            "shoulders",
            "upper arms",
            "upper legs",
            "waist"
        ]
    }


@router.get("/filters/equipment")
async def get_equipment_types():
    """
    Get list of all available equipment types for filtering
    """
    return {
        "success": True,
        "equipment": [
            "assisted",
            "band",
            "barbell",
            "body weight",
            "bosu ball",
            "cable",
            "dumbbell",
            "elliptical machine",
            "ez barbell",
            "hammer",
            "kettlebell",
            "leverage machine",
            "medicine ball",
            "olympic barbell",
            "resistance band",
            "roller",
            "rope",
            "skierg machine",
            "sled machine",
            "smith machine",
            "stability ball",
            "stationary bike",
            "stepmill machine",
            "tire",
            "trap bar",
            "upper body ergometer",
            "weighted",
            "wheel roller"
        ]
    }
