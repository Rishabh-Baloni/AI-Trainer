"""
Analytics Engine
Provides workout analytics, progress tracking, and goal predictions
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class AnalyticsEngine:
    """
    Analyzes workout history and provides insights
    """
    
    def __init__(self):
        self.workouts = []
    
    def add_workout(self, workout_data: Dict):
        """Add a workout session to history"""
        workout_data['date'] = datetime.now().isoformat()
        self.workouts.append(workout_data)
    
    def calculate_weekly_stats(self, user_workouts: List[Dict]) -> Dict:
        """
        Calculate weekly statistics from workout history
        
        Args:
            user_workouts: List of workout dictionaries
            
        Returns:
            Dictionary with weekly stats
        """
        if not user_workouts:
            return {
                'total_workouts': 0,
                'total_calories': 0,
                'total_duration': 0,
                'avg_intensity': 0,
                'most_common_exercise': 'None',
                'workout_streak': 0
            }
        
        df = pd.DataFrame(user_workouts)
        
        # Convert date strings to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Filter last 7 days
        week_ago = datetime.now() - timedelta(days=7)
        df_week = df[df['date'] >= week_ago]
        
        # Calculate stats
        stats = {
            'total_workouts': len(df_week),
            'total_calories': int(df_week['calories_burned'].sum()) if 'calories_burned' in df_week else 0,
            'total_duration': int(df_week['duration_minutes'].sum()) if 'duration_minutes' in df_week else 0,
            'avg_intensity': round(df_week['intensity'].mean(), 1) if 'intensity' in df_week else 0,
            'most_common_exercise': df_week['exercise_type'].mode()[0] if 'exercise_type' in df_week and len(df_week) > 0 else 'None',
            'workout_streak': self._calculate_streak(df)
        }
        
        return stats
    
    def _calculate_streak(self, df: pd.DataFrame) -> int:
        """Calculate current workout streak in days"""
        if df.empty:
            return 0
        
        df = df.sort_values('date', ascending=False)
        df['date_only'] = df['date'].dt.date
        unique_dates = df['date_only'].unique()
        
        streak = 0
        current_date = datetime.now().date()
        
        for date in unique_dates:
            if date == current_date or date == current_date - timedelta(days=streak):
                streak += 1
            else:
                break
        
        return streak
    
    def predict_goal_achievement(self, current_progress: float, goal: float, 
                                 history: List[Dict]) -> Dict:
        """
        Predict when user will achieve their goal
        
        Args:
            current_progress: Current metric value (e.g., weight, reps)
            goal: Target value
            history: Historical data points
            
        Returns:
            Prediction dictionary with estimated days and confidence
        """
        if not history or len(history) < 2:
            return {
                'estimated_days': None,
                'confidence': 'low',
                'prediction': 'Need more data',
                'weekly_progress_rate': 0
            }
        
        df = pd.DataFrame(history)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        # Simple linear regression
        days_elapsed = (df['date'] - df['date'].min()).dt.days.values
        values = df['value'].values
        
        if len(days_elapsed) < 2 or np.std(values) == 0:
            return {
                'estimated_days': None,
                'confidence': 'low',
                'prediction': 'Insufficient variance in data',
                'weekly_progress_rate': 0
            }
        
        # Calculate slope (rate of change)
        slope = np.polyfit(days_elapsed, values, 1)[0]
        
        if slope == 0:
            return {
                'estimated_days': None,
                'confidence': 'low',
                'prediction': 'No progress detected',
                'weekly_progress_rate': 0
            }
        
        # Predict days to reach goal
        days_to_goal = (goal - current_progress) / slope
        
        # Calculate confidence based on consistency
        residuals = values - np.polyval(np.polyfit(days_elapsed, values, 1), days_elapsed)
        r_squared = 1 - (np.sum(residuals**2) / np.sum((values - np.mean(values))**2))
        
        confidence = 'high' if r_squared > 0.7 else 'medium' if r_squared > 0.4 else 'low'
        
        weekly_rate = slope * 7
        
        return {
            'estimated_days': int(days_to_goal) if days_to_goal > 0 else 0,
            'confidence': confidence,
            'prediction': f"{int(days_to_goal)} days" if days_to_goal > 0 else "Goal achieved!",
            'weekly_progress_rate': round(weekly_rate, 2),
            'r_squared': round(r_squared, 3)
        }
    
    def generate_insights(self, user_data: Dict) -> List[str]:
        """
        Generate personalized insights based on user data
        
        Args:
            user_data: Dictionary with workout history and goals
            
        Returns:
            List of insight strings
        """
        insights = []
        
        workouts = user_data.get('workouts', [])
        if not workouts:
            return ["Start tracking workouts to get personalized insights!"]
        
        df = pd.DataFrame(workouts)
        df['date'] = pd.to_datetime(df['date'])
        
        # Recent activity
        week_ago = datetime.now() - timedelta(days=7)
        recent_workouts = df[df['date'] >= week_ago]
        
        if len(recent_workouts) >= 3:
            insights.append(f"🔥 Great job! You've worked out {len(recent_workouts)} times this week!")
        elif len(recent_workouts) == 0:
            insights.append("⏰ No workouts this week. Let's get moving!")
        
        # Consistency check
        if 'consistency_score' in user_data and user_data['consistency_score'] > 80:
            insights.append("⭐ Excellent consistency! You're building a strong habit.")
        
        # Calorie tracking
        if 'calories_burned' in df.columns:
            avg_calories = df['calories_burned'].tail(7).mean()
            if avg_calories > 300:
                insights.append(f"💪 Burning an average of {int(avg_calories)} calories per workout!")
        
        # Improvement trend
        if len(df) >= 5 and 'intensity' in df.columns:
            recent_intensity = df['intensity'].tail(3).mean()
            older_intensity = df['intensity'].head(3).mean()
            if recent_intensity > older_intensity * 1.1:
                insights.append("📈 Your workout intensity is increasing - keep pushing!")
        
        # Rest day reminder
        if len(df) > 0:
            last_workout = df['date'].max()
            days_since = (datetime.now() - last_workout).days
            if days_since > 2:
                insights.append(f"💤 It's been {days_since} days since your last workout. Ready to get back?")
        
        return insights if insights else ["Keep up the good work! 💪"]
    
    def calculate_performance_metrics(self, workouts: List[Dict]) -> Dict:
        """Calculate comprehensive performance metrics"""
        if not workouts:
            return {
                'total_workouts': 0,
                'total_time_minutes': 0,
                'avg_workout_duration': 0,
                'total_calories_burned': 0,
                'favorite_exercises': [],
                'peak_performance_day': 'Not enough data',
                'consistency_percentage': 0
            }
        
        df = pd.DataFrame(workouts)
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate day of week distribution
        df['day_of_week'] = df['date'].dt.day_name()
        day_counts = df['day_of_week'].value_counts()
        
        # Find favorite exercises
        if 'exercise_type' in df.columns:
            favorite_exercises = df['exercise_type'].value_counts().head(3).index.tolist()
        else:
            favorite_exercises = []
        
        # Calculate consistency (workouts in last 30 days / 30 * 100)
        thirty_days_ago = datetime.now() - timedelta(days=30)
        recent_count = len(df[df['date'] >= thirty_days_ago])
        consistency = (recent_count / 30) * 100
        
        metrics = {
            'total_workouts': len(df),
            'total_time_minutes': int(df['duration_minutes'].sum()) if 'duration_minutes' in df else 0,
            'avg_workout_duration': round(df['duration_minutes'].mean(), 1) if 'duration_minutes' in df else 0,
            'total_calories_burned': int(df['calories_burned'].sum()) if 'calories_burned' in df else 0,
            'favorite_exercises': favorite_exercises,
            'peak_performance_day': day_counts.index[0] if len(day_counts) > 0 else 'Not enough data',
            'consistency_percentage': round(min(consistency, 100), 1)
        }
        
        return metrics
