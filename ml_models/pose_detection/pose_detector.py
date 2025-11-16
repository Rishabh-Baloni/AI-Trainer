"""
Pose Detection Module
Uses MediaPipe for real-time human pose estimation and exercise form analysis
"""

import cv2
import mediapipe as mp
import numpy as np


class PoseDetector:
    """
    Real-time pose detection and analysis for fitness exercises
    """
    
    def __init__(self, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        """
        Initialize MediaPipe Pose detector
        
        Args:
            min_detection_confidence: Minimum confidence for person detection
            min_tracking_confidence: Minimum confidence for pose tracking
        """
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
            smooth_landmarks=True
        )
        self.results = None
    
    def detect_pose(self, frame, draw=True):
        """
        Detect pose landmarks in a video frame
        
        Args:
            frame: Input image/video frame (BGR format)
            draw: Whether to draw landmarks on frame
            
        Returns:
            tuple: (processed_frame, landmarks)
        """
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process with MediaPipe
        self.results = self.pose.process(rgb_frame)
        
        # Draw landmarks if requested
        if draw and self.results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                frame,
                self.results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)
            )
        
        return frame, self.results.pose_landmarks
    
    def calculate_angle(self, point1, point2, point3):
        """
        Calculate angle between three points (for joint angles)
        
        Args:
            point1, point2, point3: Coordinates [x, y] of the three points
            
        Returns:
            Angle in degrees (0-180)
        """
        point1 = np.array(point1)
        point2 = np.array(point2)
        point3 = np.array(point3)
        
        # Calculate vectors
        radians = np.arctan2(point3[1] - point2[1], point3[0] - point2[0]) - \
                  np.arctan2(point1[1] - point2[1], point1[0] - point2[0])
        
        angle = np.abs(radians * 180.0 / np.pi)
        
        if angle > 180.0:
            angle = 360 - angle
        
        return angle
    
    def get_landmark_coords(self, landmarks, landmark_id):
        """
        Extract x, y coordinates for a specific landmark
        
        Args:
            landmarks: MediaPipe pose landmarks
            landmark_id: Landmark enum value
            
        Returns:
            list: [x, y] coordinates
        """
        landmark = landmarks.landmark[landmark_id]
        return [landmark.x, landmark.y]
    
    def get_visibility(self, landmarks, landmark_id):
        """
        Get visibility score for a landmark
        
        Args:
            landmarks: MediaPipe pose landmarks
            landmark_id: Landmark enum value
            
        Returns:
            float: Visibility score (0-1)
        """
        return landmarks.landmark[landmark_id].visibility
    
    def is_body_visible(self, landmarks, min_visibility=0.5):
        """
        Check if body is sufficiently visible in frame
        
        Args:
            landmarks: MediaPipe pose landmarks
            min_visibility: Minimum visibility threshold
            
        Returns:
            bool: True if body is visible enough
        """
        if not landmarks:
            return False
        
        # Check key landmarks (shoulders, hips, knees)
        key_landmarks = [
            self.mp_pose.PoseLandmark.LEFT_SHOULDER,
            self.mp_pose.PoseLandmark.RIGHT_SHOULDER,
            self.mp_pose.PoseLandmark.LEFT_HIP,
            self.mp_pose.PoseLandmark.RIGHT_HIP,
            self.mp_pose.PoseLandmark.LEFT_KNEE,
            self.mp_pose.PoseLandmark.RIGHT_KNEE
        ]
        
        visible_count = sum(
            1 for lm_id in key_landmarks
            if self.get_visibility(landmarks, lm_id.value) > min_visibility
        )
        
        return visible_count >= 4  # At least 4 key points visible
    
    def close(self):
        """Release MediaPipe resources"""
        self.pose.close()
