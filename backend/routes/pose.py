"""
Pose Detection API Routes
Handle pose detection and exercise analysis requests
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/api/pose", tags=["Pose Detection"])


class PoseAnalysisRequest(BaseModel):
    """Request model for pose analysis"""
    exercise_type: str  # squat, pushup, plank
    image_data: Optional[str] = None  # base64 encoded image (optional)


class PoseAnalysisResponse(BaseModel):
    """Response model for pose analysis"""
    exercise: str
    rep_count: int
    form_score: int
    feedback: List[str]
    status: str


@router.get("/exercises")
async def get_supported_exercises():
    """
    Get list of exercises that support pose detection
    """
    exercises = [
        {
            "name": "squat",
            "supported": True,
            "description": "Bodyweight squats with knee angle and back posture analysis",
            "key_points": ["Knee angle < 90°", "Back straight", "Knees aligned with ankles"]
        },
        {
            "name": "pushup",
            "supported": True,
            "description": "Push-ups with elbow angle and body alignment analysis",
            "key_points": ["Elbow angle < 90°", "Body straight", "Controlled movement"]
        },
        {
            "name": "plank",
            "supported": True,
            "description": "Plank hold with body alignment analysis",
            "key_points": ["Straight body line", "Hips not sagging", "Core engaged"]
        },
        {
            "name": "lunge",
            "supported": False,
            "description": "Coming soon - Lunges with knee and hip analysis"
        },
        {
            "name": "bicep_curl",
            "supported": False,
            "description": "Coming soon - Bicep curls with elbow tracking"
        }
    ]
    
    return {
        "total": len(exercises),
        "supported_count": sum(1 for e in exercises if e.get("supported", False)),
        "exercises": exercises
    }


@router.post("/analyze", response_model=PoseAnalysisResponse)
async def analyze_pose(request: PoseAnalysisRequest):
    """
    Analyze pose for a specific exercise (Demo Mode)
    
    Note: For full real-time functionality, run the standalone script:
    ml_models/pose_detection/run_pose_demo.py
    """
    
    if request.exercise_type not in ["squat", "pushup", "plank"]:
        raise HTTPException(
            status_code=400,
            detail=f"Exercise '{request.exercise_type}' not supported. Use: squat, pushup, or plank"
        )
    
    # Demo response (simulated analysis)
    demo_responses = {
        "squat": {
            "exercise": "squat",
            "rep_count": 0,
            "form_score": 85,
            "feedback": [
                "Position yourself in front of camera",
                "Stand with feet shoulder-width apart",
                "Lower until thighs parallel to ground",
                "Push through heels to stand up"
            ],
            "status": "demo_mode"
        },
        "pushup": {
            "exercise": "pushup",
            "rep_count": 0,
            "form_score": 80,
            "feedback": [
                "Position camera to see your side profile",
                "Start in plank position",
                "Lower chest to ground (elbow 90°)",
                "Push back up keeping body straight"
            ],
            "status": "demo_mode"
        },
        "plank": {
            "exercise": "plank",
            "rep_count": 0,
            "form_score": 90,
            "feedback": [
                "Position yourself sideways to camera",
                "Keep body in straight line",
                "Don't let hips sag or pike up",
                "Hold position and breathe steadily"
            ],
            "status": "demo_mode"
        }
    }
    
    response = demo_responses[request.exercise_type]
    
    if not request.image_data:
        response["feedback"].append(
            "💡 For live pose detection, run: python ml_models/pose_detection/run_pose_demo.py"
        )
    
    return response


@router.get("/stats")
async def get_pose_detection_stats():
    """
    Get pose detection system statistics and capabilities
    """
    try:
        import cv2
        import mediapipe as mp
        opencv_available = True
        mediapipe_available = True
        cv2_version = cv2.__version__
        mp_version = mp.__version__
    except ImportError:
        opencv_available = False
        mediapipe_available = False
        cv2_version = "Not installed"
        mp_version = "Not installed"
    
    return {
        "system_status": "ready" if (opencv_available and mediapipe_available) else "demo_mode",
        "opencv_installed": opencv_available,
        "opencv_version": cv2_version,
        "mediapipe_installed": mediapipe_available,
        "mediapipe_version": mp_version,
        "supported_exercises": ["squat", "pushup", "plank"],
        "planned_exercises": ["lunge", "bicep_curl", "shoulder_press"],
        "features": {
            "rep_counting": True,
            "form_scoring": True,
            "real_time_feedback": True,
            "angle_calculation": True,
            "body_alignment_check": True
        },
        "installation_command": "pip install mediapipe opencv-python numpy",
        "demo_script": "ml_models/pose_detection/run_pose_demo.py"
    }


@router.get("/demo-info")
async def get_demo_info():
    """
    Get information about running the pose detection demo
    """
    return {
        "title": "AI Fitness Trainer - Pose Detection Demo",
        "description": "Real-time exercise form analysis with automatic rep counting",
        "setup_steps": [
            "1. Install packages: pip install mediapipe opencv-python numpy",
            "2. Navigate to: cd ml_models/pose_detection",
            "3. Run demo: python run_pose_demo.py",
            "4. Stand in front of webcam (full body visible)",
            "5. Press 'q' for squats, 'p' for pushups",
            "6. Press 'r' to reset counter, 's' to stop"
        ],
        "features": [
            "✅ Real-time pose tracking (33 body landmarks)",
            "✅ Automatic rep counting",
            "✅ Form scoring (0-100%)",
            "✅ Live feedback messages",
            "✅ Multiple exercise support",
            "✅ Color-coded skeleton overlay"
        ],
        "requirements": {
            "hardware": "Webcam (built-in or USB)",
            "lighting": "Good lighting (not too dark)",
            "space": "2 meters in front of camera",
            "python": "Python 3.8+"
        },
        "controls": {
            "q": "Switch to squat mode",
            "p": "Switch to pushup mode",
            "r": "Reset rep counter",
            "s": "Stop and exit"
        }
    }
