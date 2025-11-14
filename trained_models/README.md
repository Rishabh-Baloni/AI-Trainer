# Trained Models Directory

Store all trained ML models here.

## Model Storage Structure:
```
trained_models/
├── pose_detection/
│   ├── pose_model_v1.h5
│   └── exercise_classifier.pkl
├── workout_recommendation/
│   └── recommender_model.pkl
├── diet_recommendation/
│   └── diet_planner.pkl
└── analytics/
    └── progress_predictor.pkl
```

## Model Versioning:
- Use semantic versioning (v1.0, v1.1, v2.0)
- Keep changelog of model updates
- Save model metadata (accuracy, training date, dataset used)

## Notes:
- Don't commit large model files to git
- Use model compression where possible
- Document model architecture and performance metrics
