"""
Database models using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    """
    User model
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password_hash = Column(String)
    age = Column(Integer)
    gender = Column(String)
    height = Column(Float)  # cm
    weight = Column(Float)  # kg
    fitness_level = Column(String)  # beginner, intermediate, advanced
    goals = Column(JSON)  # List of goals
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    workouts = relationship("Workout", back_populates="user")
    meals = relationship("Meal", back_populates="user")


class Workout(Base):
    """
    Workout session model
    """
    __tablename__ = "workouts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exercise_type = Column(String)
    duration_minutes = Column(Integer)
    calories_burned = Column(Float)
    form_score = Column(Float)  # 0-100
    completed_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="workouts")


class Meal(Base):
    """
    Meal tracking model
    """
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    meal_type = Column(String)  # breakfast, lunch, dinner, snack
    foods = Column(JSON)  # List of food items
    total_calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fats = Column(Float)
    consumed_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="meals")
