"""
Diet Recommendation API Routes
Meal planning and nutrition tracking using Spoonacular API
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/diet", tags=["Diet & Nutrition"])

# Spoonacular API Configuration
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
SPOONACULAR_BASE_URL = "https://api.spoonacular.com"


class MealPlanRequest(BaseModel):
    timeframe: str = "day"  # "day" or "week"
    target_calories: int = 2000
    diet: Optional[str] = None  # ketogenic, vegetarian, vegan, paleo, etc.
    exclude: Optional[str] = None  # Comma-separated list of ingredients to exclude


@router.get("/meal-plan")
async def get_sample_meal_plan(diet_type: str = "balanced"):
    """
    Get a sample meal plan
    """
    plans = {
        "balanced": {
            "name": "Balanced Meal Plan",
            "daily_calories": 2000,
            "meals": [
                {"meal": "Breakfast", "name": "Oatmeal with berries", "calories": 350},
                {"meal": "Lunch", "name": "Grilled chicken salad", "calories": 500},
                {"meal": "Dinner", "name": "Salmon with vegetables", "calories": 600},
                {"meal": "Snacks", "name": "Greek yogurt & nuts", "calories": 300}
            ],
            "macros": {"protein": "25%", "carbs": "45%", "fats": "30%"}
        },
        "keto": {
            "name": "Keto Meal Plan",
            "daily_calories": 1800,
            "meals": [
                {"meal": "Breakfast", "name": "Eggs with avocado", "calories": 400},
                {"meal": "Lunch", "name": "Caesar salad with chicken", "calories": 500},
                {"meal": "Dinner", "name": "Steak with broccoli", "calories": 700},
                {"meal": "Snacks", "name": "Cheese and almonds", "calories": 200}
            ],
            "macros": {"protein": "25%", "carbs": "5%", "fats": "70%"}
        },
        "vegetarian": {
            "name": "Vegetarian Meal Plan",
            "daily_calories": 1900,
            "meals": [
                {"meal": "Breakfast", "name": "Smoothie bowl", "calories": 350},
                {"meal": "Lunch", "name": "Quinoa Buddha bowl", "calories": 500},
                {"meal": "Dinner", "name": "Lentil curry with rice", "calories": 550},
                {"meal": "Snacks", "name": "Hummus with veggies", "calories": 250}
            ],
            "macros": {"protein": "20%", "carbs": "50%", "fats": "30%"}
        }
    }
    
    plan = plans.get(diet_type.lower(), plans["balanced"])
    return {
        "status": "success",
        "diet_type": diet_type,
        "plan": plan
    }


@router.post("/meal-plan/generate")
async def generate_meal_plan(request: MealPlanRequest):
    """
    Generate a personalized meal plan
    
    - **timeframe**: "day" or "week"
    - **target_calories**: Target daily calories (e.g., 2000)
    - **diet**: Diet type (ketogenic, vegetarian, vegan, paleo, primal, whole30)
    - **exclude**: Ingredients to exclude (comma-separated)
    """
    try:
        params = {
            "apiKey": SPOONACULAR_API_KEY,
            "timeFrame": request.timeframe,
            "targetCalories": request.target_calories
        }
        
        if request.diet:
            params["diet"] = request.diet
        if request.exclude:
            params["exclude"] = request.exclude
        
        response = requests.get(
            f"{SPOONACULAR_BASE_URL}/mealplanner/generate",
            params=params,
            timeout=15
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "data": response.json()
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error generating meal plan: {str(e)}")


@router.get("/recipe/{recipe_id}")
async def get_recipe_details(recipe_id: int):
    """
    Get detailed information about a specific recipe
    
    - **recipe_id**: Spoonacular recipe ID
    """
    try:
        params = {
            "apiKey": SPOONACULAR_API_KEY,
            "includeNutrition": True
        }
        
        response = requests.get(
            f"{SPOONACULAR_BASE_URL}/recipes/{recipe_id}/information",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "data": response.json()
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recipe details: {str(e)}")


@router.get("/recipe/search")
async def search_recipes(
    query: str = Query(..., min_length=1),
    diet: Optional[str] = None,
    cuisine: Optional[str] = None,
    max_calories: Optional[int] = None,
    number: int = Query(10, ge=1, le=100)
):
    """
    Search for recipes based on query and filters
    
    - **query**: Search term (e.g., "pasta", "chicken")
    - **diet**: Diet type filter
    - **cuisine**: Cuisine type (italian, mexican, asian, etc.)
    - **max_calories**: Maximum calories per serving
    - **number**: Number of results to return
    """
    try:
        params = {
            "apiKey": SPOONACULAR_API_KEY,
            "query": query,
            "number": number,
            "addRecipeInformation": True,
            "fillIngredients": True
        }
        
        if diet:
            params["diet"] = diet
        if cuisine:
            params["cuisine"] = cuisine
        if max_calories:
            params["maxCalories"] = max_calories
        
        response = requests.get(
            f"{SPOONACULAR_BASE_URL}/recipes/complexSearch",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "query": query,
            "data": response.json()
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error searching recipes: {str(e)}")


@router.get("/nutrition/ingredient/{ingredient_id}")
async def get_ingredient_nutrition(
    ingredient_id: int,
    amount: float = 100,
    unit: str = "grams"
):
    """
    Get nutritional information for a specific ingredient
    
    - **ingredient_id**: Spoonacular ingredient ID
    - **amount**: Quantity of ingredient
    - **unit**: Unit of measurement (grams, cups, oz, etc.)
    """
    try:
        params = {
            "apiKey": SPOONACULAR_API_KEY,
            "amount": amount,
            "unit": unit
        }
        
        response = requests.get(
            f"{SPOONACULAR_BASE_URL}/food/ingredients/{ingredient_id}/information",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "data": response.json()
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching ingredient nutrition: {str(e)}")


@router.get("/diets")
async def get_diet_types():
    """
    Get list of supported diet types
    """
    return {
        "success": True,
        "diets": [
            {"value": "ketogenic", "label": "Ketogenic", "description": "High fat, low carb"},
            {"value": "vegetarian", "label": "Vegetarian", "description": "No meat"},
            {"value": "vegan", "label": "Vegan", "description": "No animal products"},
            {"value": "paleo", "label": "Paleo", "description": "Whole foods, no processed"},
            {"value": "primal", "label": "Primal", "description": "Similar to paleo with dairy"},
            {"value": "whole30", "label": "Whole30", "description": "30-day whole food diet"},
            {"value": "glutenfree", "label": "Gluten Free", "description": "No gluten"},
            {"value": "dairyfree", "label": "Dairy Free", "description": "No dairy products"},
        ]
    }


@router.get("/cuisines")
async def get_cuisine_types():
    """
    Get list of supported cuisine types
    """
    return {
        "success": True,
        "cuisines": [
            "African", "American", "British", "Cajun", "Caribbean", "Chinese",
            "Eastern European", "European", "French", "German", "Greek", "Indian",
            "Irish", "Italian", "Japanese", "Jewish", "Korean", "Latin American",
            "Mediterranean", "Mexican", "Middle Eastern", "Nordic", "Southern",
            "Spanish", "Thai", "Vietnamese"
        ]
    }
