"""
Simple Pose Detection Demo - Run without Jupyter
Just run: python run_pose_demo.py
"""

print("🔄 Checking dependencies...")

try:
    import cv2
    import mediapipe as mp
    import numpy as np
    print("✅ All packages imported successfully!")
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("\n📦 Please install required packages:")
    print("   pip install mediapipe opencv-python numpy")
    exit(1)

print("\n🏋️ Starting AI Fitness Trainer - Pose Detection Demo")
print("=" * 60)

# Initialize MediaPipe
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Color scheme
POSE_COLOR = (0, 255, 0)
UPPER_COLOR = (255, 150, 0)
LOWER_COLOR = (150, 0, 255)

# Exercise state
exercise_mode = "squat"
rep_count = 0
stage = None
form_score = 0
feedback_messages = []

def calculate_angle(a, b, c):
    """Calculate angle between three points"""
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
    
    return angle

def analyze_squat(landmarks):
    """Analyze squat form and count reps"""
    global rep_count, stage, form_score, feedback_messages
    
    # Get landmarks
    hip = [landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].x,
           landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].y]
    knee = [landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].x,
            landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].y]
    ankle = [landmarks[mp_holistic.PoseLandmark.LEFT_ANKLE.value].x,
             landmarks[mp_holistic.PoseLandmark.LEFT_ANKLE.value].y]
    shoulder = [landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
    
    # Calculate angles
    knee_angle = calculate_angle(hip, knee, ankle)
    back_angle = calculate_angle(shoulder, hip, knee)
    
    feedback_messages = []
    score_components = []
    
    # Check depth
    if knee_angle < 90:
        if stage != "down":
            stage = "down"
        score_components.append(100)
    elif knee_angle < 120:
        score_components.append(70)
        feedback_messages.append("Go deeper")
    else:
        if stage == "down":
            stage = "up"
            rep_count += 1
        score_components.append(50)
    
    # Check back straightness
    if 160 < back_angle < 200:
        score_components.append(100)
    else:
        score_components.append(50)
        feedback_messages.append("Keep back straight")
    
    # Check knee alignment
    knee_x = knee[0]
    ankle_x = ankle[0]
    if abs(knee_x - ankle_x) < 0.1:
        score_components.append(100)
    else:
        score_components.append(60)
        if knee_x > ankle_x:
            feedback_messages.append("Knees too forward")
    
    form_score = int(np.mean(score_components)) if score_components else 0
    
    return knee_angle, back_angle

def analyze_pushup(landmarks):
    """Analyze pushup form and count reps"""
    global rep_count, stage, form_score, feedback_messages
    
    # Get landmarks
    shoulder = [landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].x,
             landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].x,
             landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].y]
    hip = [landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].x,
           landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].y]
    knee = [landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].x,
            landmarks[mp_holistic.PoseLandmark.LEFT_KNEE.value].y]
    
    # Calculate angles
    elbow_angle = calculate_angle(shoulder, elbow, wrist)
    body_angle = calculate_angle(shoulder, hip, knee)
    
    feedback_messages = []
    score_components = []
    
    # Check depth
    if elbow_angle < 90:
        if stage != "down":
            stage = "down"
        score_components.append(100)
    elif elbow_angle < 120:
        score_components.append(70)
        feedback_messages.append("Go lower")
    else:
        if stage == "down":
            stage = "up"
            rep_count += 1
        score_components.append(50)
    
    # Check body alignment
    if 160 < body_angle < 200:
        score_components.append(100)
    else:
        score_components.append(50)
        if body_angle < 160:
            feedback_messages.append("Hips too low")
        else:
            feedback_messages.append("Hips too high")
    
    form_score = int(np.mean(score_components)) if score_components else 0
    
    return elbow_angle, body_angle

def draw_stats(frame, rep_count, form_score, exercise_mode, feedback_messages):
    """Draw statistics overlay"""
    # Semi-transparent background
    overlay = frame.copy()
    cv2.rectangle(overlay, (10, 10), (400, 200), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
    
    # Exercise mode
    cv2.putText(frame, f"Exercise: {exercise_mode.upper()}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    # Rep counter
    cv2.putText(frame, f"Reps: {rep_count}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)
    
    # Form score with color
    score_color = (0, 255, 0) if form_score > 80 else (0, 165, 255) if form_score > 60 else (0, 0, 255)
    cv2.putText(frame, f"Form: {form_score}%", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, score_color, 2)
    
    # Feedback messages
    y_offset = 160
    for msg in feedback_messages:
        cv2.putText(frame, msg, (20, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
        y_offset += 30
    
    # Instructions
    cv2.putText(frame, "Press 'q': Squat | 'p': Pushup | 'r': Reset | 's': Stop",
                (10, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

# Initialize MediaPipe Holistic
holistic = mp_holistic.Holistic(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    smooth_landmarks=True
)

# Open webcam
print("\n📹 Opening webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open webcam!")
    print("   - Check if webcam is connected")
    print("   - Close other apps using webcam (Zoom, Teams, etc.)")
    exit(1)

print("✅ Webcam opened successfully!")
print("\n🎮 Controls:")
print("   'q' - Switch to Squat mode")
print("   'p' - Switch to Pushup mode")
print("   'r' - Reset rep counter")
print("   's' - Stop and exit")
print("\n📊 Starting pose detection...")
print("=" * 60)

cv2.namedWindow("AI Fitness Trainer", cv2.WINDOW_NORMAL)
cv2.resizeWindow("AI Fitness Trainer", 1280, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break
    
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = holistic.process(rgb)
    
    if result.pose_landmarks:
        lm = result.pose_landmarks.landmark
        
        # Draw pose skeleton
        mp_drawing.draw_landmarks(
            frame,
            result.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=POSE_COLOR, thickness=2, circle_radius=3),
            mp_drawing.DrawingSpec(color=POSE_COLOR, thickness=2)
        )
        
        # Analyze exercise
        if exercise_mode == "squat":
            analyze_squat(lm)
        elif exercise_mode == "pushup":
            analyze_pushup(lm)
    
    # Draw stats overlay
    draw_stats(frame, rep_count, form_score, exercise_mode, feedback_messages)
    
    cv2.imshow("AI Fitness Trainer", frame)
    
    if cv2.getWindowProperty("AI Fitness Trainer", cv2.WND_PROP_VISIBLE) < 1:
        break
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        break
    elif key == ord('q'):
        exercise_mode = "squat"
        rep_count = 0
        stage = None
        print("✅ Switched to SQUAT mode")
    elif key == ord('p'):
        exercise_mode = "pushup"
        rep_count = 0
        stage = None
        print("✅ Switched to PUSHUP mode")
    elif key == ord('r'):
        rep_count = 0
        stage = None
        print("✅ Rep counter reset")

cap.release()
cv2.destroyAllWindows()

print("\n" + "=" * 60)
print("✅ Session Complete!")
print(f"   Total Reps: {rep_count}")
print(f"   Final Form Score: {form_score}%")
print("=" * 60)
