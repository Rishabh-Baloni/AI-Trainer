"""
User Profile Management
Handle user data for personalized recommendations
"""


class UserProfile:
    """
    User profile data structure
    """
    
    def __init__(self, user_id):
        """
        Initialize user profile
        
        Args:
            user_id: Unique user identifier
        """
        self.user_id = user_id
        self.age = None
        self.gender = None
        self.height = None  # cm
        self.weight = None  # kg
        self.fitness_level = None  # beginner, intermediate, advanced
        self.goals = []  # weight_loss, muscle_gain, endurance, flexibility
        self.medical_conditions = []
        self.available_equipment = []
        self.workout_frequency = None  # days per week
    
    def calculate_bmi(self):
        """
        Calculate Body Mass Index
        
        Returns:
            bmi: BMI value
        """
        pass
    
    def calculate_tdee(self):
        """
        Calculate Total Daily Energy Expenditure
        
        Returns:
            tdee: Calories burned per day
        """
        pass
    
    def get_fitness_score(self):
        """
        Calculate overall fitness score based on various metrics
        
        Returns:
            score: Fitness score (0-100)
        """
        pass
    
    def update_progress(self, metrics):
        """
        Update user progress metrics
        
        Args:
            metrics: Dictionary of progress data
        """
        pass
