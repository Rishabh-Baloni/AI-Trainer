"""
User Profile Management
Handle user data for personalized recommendations
"""


class UserProfile:
    """
    User profile data structure
    """
    
    def __init__(self, user_id, age=None, weight=None, height=None, gender='male'):
        """
        Initialize user profile
        
        Args:
            user_id: Unique user identifier
            age: User age in years
            weight: Weight in kg
            height: Height in cm
            gender: 'male' or 'female'
        """
        self.user_id = user_id
        self.age = age
        self.gender = gender.lower() if gender else 'male'
        self.height = height  # cm
        self.weight = weight  # kg
        self.fitness_level = 'beginner'  # beginner, intermediate, advanced
        self.goals = []  # weight_loss, muscle_gain, endurance, flexibility
        self.medical_conditions = []
        self.available_equipment = ['none']
        self.workout_frequency = 3  # days per week
        self.available_time = 30  # minutes per session
    
    def calculate_bmi(self):
        """
        Calculate Body Mass Index
        
        Returns:
            float: BMI value
        """
        if not self.weight or not self.height:
            return None
        
        height_m = self.height / 100
        bmi = self.weight / (height_m ** 2)
        return round(bmi, 2)
    
    def get_bmi_category(self):
        """Get BMI category"""
        bmi = self.calculate_bmi()
        if not bmi:
            return "Unknown"
        
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def calculate_tdee(self, activity_level='moderate'):
        """
        Calculate Total Daily Energy Expenditure
        
        Args:
            activity_level: sedentary, light, moderate, active, very_active
            
        Returns:
            float: Calories burned per day
        """
        if not all([self.weight, self.height, self.age]):
            return None
        
        # Calculate BMR using Mifflin-St Jeor
        if self.gender == 'male':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        
        activity_multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        
        multiplier = activity_multipliers.get(activity_level, 1.55)
        return round(bmr * multiplier, 2)
    
    def get_fitness_score(self):
        """
        Calculate overall fitness score based on various metrics
        
        Returns:
            int: Fitness score (1-3)
        """
        levels = {'beginner': 1, 'intermediate': 2, 'advanced': 3}
        return levels.get(self.fitness_level, 1)
    
    def update_progress(self, metrics):
        """
        Update user progress metrics
        
        Args:
            metrics: Dictionary of progress data (weight, measurements, etc.)
        """
        if 'weight' in metrics:
            self.weight = metrics['weight']
        if 'fitness_level' in metrics:
            self.fitness_level = metrics['fitness_level']
    
    def to_dict(self):
        """Export profile as dictionary"""
        return {
            'user_id': self.user_id,
            'age': self.age,
            'weight': self.weight,
            'height': self.height,
            'gender': self.gender,
            'fitness_level': self.fitness_level,
            'goals': self.goals,
            'bmi': self.calculate_bmi(),
            'bmi_category': self.get_bmi_category(),
            'tdee': self.calculate_tdee()
        }
