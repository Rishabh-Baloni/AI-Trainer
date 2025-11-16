"""
Workout Recommendation System
Generates personalized workout plans based on user profile and goals
"""

import json
import os
import random
from datetime import datetime, timedelta


class WorkoutRecommender:
    """
    AI-powered workout plan generator
    """
    
    def __init__(self):
        """
        Initialize recommendation engine
        """
        self.exercise_database = {}
        self.user_profiles = {}
        self.load_exercise_database()
    
    def load_exercise_database(self):
        """
        Load exercise database from JSON file
        """
        json_path = os.path.join(os.path.dirname(__file__), 'exercises.json')
        try:
            with open(json_path, 'r') as f:
                self.exercise_database = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Exercise database not found at {json_path}")
            self.exercise_database = {}
    
    def filter_exercises(self, difficulty=None, muscle_group=None, equipment=None):
        """
        Filter exercises based on criteria
        
        Args:
            difficulty: beginner, intermediate, advanced
            muscle_group: Target muscle group
            equipment: Available equipment
            
        Returns:
            list: Filtered exercise keys
        """
        filtered = []
        
        for ex_id, ex_data in self.exercise_database.items():
            # Check difficulty
            if difficulty and ex_data['difficulty'] != difficulty:
                continue
            
            # Check muscle group
            if muscle_group:
                if isinstance(ex_data['muscle_group'], list):
                    if muscle_group not in ex_data['muscle_group']:
                        continue
                elif ex_data['muscle_group'] != muscle_group:
                    continue
            
            # Check equipment
            if equipment:
                if isinstance(equipment, list):
                    if ex_data['equipment'] not in equipment:
                        continue
                elif ex_data['equipment'] != equipment:
                    continue
            
            filtered.append(ex_id)
        
        return filtered
    
    def generate_workout_plan(self, user_profile, days_per_week=3, duration_minutes=30):
        """
        Generate personalized weekly workout plan
        
        Args:
            user_profile: UserProfile object
            days_per_week: Number of workout days (3-6)
            duration_minutes: Target duration per session
            
        Returns:
            dict: Weekly workout plan
        """
        fitness_level = user_profile.fitness_level
        equipment = user_profile.available_equipment
        goals = user_profile.goals if user_profile.goals else ['general_fitness']
        
        # Define workout split based on days per week
        if days_per_week <= 3:
            split = ['full_body', 'full_body', 'full_body']
        elif days_per_week == 4:
            split = ['upper_body', 'lower_body', 'upper_body', 'lower_body']
        elif days_per_week == 5:
            split = ['chest_triceps', 'back_biceps', 'legs', 'shoulders', 'core_cardio']
        else:
            split = ['chest', 'back', 'legs', 'shoulders', 'arms', 'core_cardio']
        
        weekly_plan = {}
        
        for day_num, focus in enumerate(split[:days_per_week], 1):
            daily_workout = self.create_daily_workout(
                focus, fitness_level, equipment, duration_minutes, goals
            )
            weekly_plan[f'Day {day_num}'] = daily_workout
        
        return weekly_plan
    
    def create_daily_workout(self, focus, fitness_level, equipment, duration_minutes, goals):
        """
        Create a single day's workout
        
        Args:
            focus: Workout focus (full_body, upper_body, etc.)
            fitness_level: beginner, intermediate, advanced
            equipment: List of available equipment
            duration_minutes: Target duration
            goals: User goals
            
        Returns:
            dict: Daily workout details
        """
        workout = {
            'focus': focus,
            'duration': duration_minutes,
            'exercises': [],
            'estimated_calories': 0
        }
        
        # Determine muscle groups for this workout
        muscle_groups = self.get_muscle_groups_for_focus(focus)
        
        # Select exercises
        exercises_per_group = max(1, 5 // len(muscle_groups))
        selected_exercises = []
        
        for muscle_group in muscle_groups:
            matching = self.filter_exercises(
                difficulty=fitness_level,
                muscle_group=muscle_group,
                equipment=equipment
            )
            
            if matching:
                # Pick random exercises
                count = min(exercises_per_group, len(matching))
                selected = random.sample(matching, count)
                selected_exercises.extend(selected)
        
        # If not enough exercises, add some general ones
        if len(selected_exercises) < 4:
            general = self.filter_exercises(difficulty=fitness_level, equipment=equipment)
            needed = 4 - len(selected_exercises)
            additional = random.sample([ex for ex in general if ex not in selected_exercises], 
                                     min(needed, len(general)))
            selected_exercises.extend(additional)
        
        # Build exercise list with sets/reps
        total_calories = 0
        for ex_id in selected_exercises[:6]:  # Limit to 6 exercises
            ex_data = self.exercise_database[ex_id]
            
            # Determine sets and reps based on fitness level
            sets, reps = self.get_sets_reps(fitness_level, goals)
            
            exercise_detail = {
                'name': ex_data['name'],
                'sets': sets,
                'reps': ex_data['reps'],
                'muscle_group': ex_data['muscle_group'],
                'instructions': ex_data['instructions']
            }
            
            # Estimate calories
            calories = ex_data['calories_per_rep'] * sets * 12  # Assume avg 12 reps
            total_calories += calories
            
            workout['exercises'].append(exercise_detail)
        
        workout['estimated_calories'] = round(total_calories)
        
        return workout
    
    def get_muscle_groups_for_focus(self, focus):
        """Get muscle groups for a workout focus"""
        focus_map = {
            'full_body': ['legs', 'chest', 'back', 'core'],
            'upper_body': ['chest', 'back', 'shoulders'],
            'lower_body': ['legs', 'glutes'],
            'chest_triceps': ['chest', 'triceps'],
            'back_biceps': ['back', 'biceps'],
            'legs': ['legs', 'glutes'],
            'shoulders': ['shoulders'],
            'arms': ['biceps', 'triceps'],
            'core_cardio': ['core', 'cardio'],
            'chest': ['chest'],
            'back': ['back']
        }
        return focus_map.get(focus, ['full_body'])
    
    def get_sets_reps(self, fitness_level, goals):
        """Determine sets based on fitness level and goals"""
        if fitness_level == 'beginner':
            sets = 2
        elif fitness_level == 'intermediate':
            sets = 3
        else:
            sets = 4
        
        # Adjust for goals
        if 'endurance' in goals:
            sets += 1
        
        return sets, "See exercise details"
    
    def calculate_workout_calories(self, workout_plan):
        """Calculate total calories for a workout"""
        total = 0
        for exercise in workout_plan.get('exercises', []):
            total += exercise.get('estimated_calories', 0)
        return total
    
    def adapt_difficulty(self, user_id, performance_data):
        """
        Adapt workout difficulty based on performance
        
        Args:
            user_id: User identifier
            performance_data: Dict with completion_rate, form_scores, etc.
            
        Returns:
            str: Recommendation (increase, maintain, decrease)
        """
        completion_rate = performance_data.get('completion_rate', 0)
        avg_form_score = performance_data.get('avg_form_score', 0)
        
        if completion_rate > 0.9 and avg_form_score > 80:
            return 'increase'
        elif completion_rate < 0.6 or avg_form_score < 60:
            return 'decrease'
        else:
            return 'maintain'
        pass
    
    def recommend_progressive_overload(self, current_plan, progress):
        """
        Implement progressive overload for continuous improvement
        
        Args:
            current_plan: Current workout routine
            progress: User progress metrics
            
        Returns:
            next_plan: Advanced workout plan
        """
        pass
