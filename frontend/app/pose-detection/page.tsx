'use client'

import { useState } from 'react'

export default function PoseDetectionPage() {
  const [isDetecting, setIsDetecting] = useState(false)
  const [selectedExercise, setSelectedExercise] = useState('squat')

  const exercises = [
    { id: 'squat', name: 'Squat', icon: '🏋️' },
    { id: 'pushup', name: 'Push-up', icon: '💪' },
    { id: 'plank', name: 'Plank', icon: '🧘' },
    { id: 'lunge', name: 'Lunge', icon: '🦵' },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex items-center gap-4">
            <a href="/dashboard" className="text-indigo-600 hover:text-indigo-700">← Back</a>
            <h1 className="text-2xl font-bold text-gray-900">Pose Detection</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Camera Feed */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Camera Feed</h2>
              
              {/* Placeholder for camera/video */}
              <div className="aspect-video bg-gray-900 rounded-lg flex items-center justify-center mb-4">
                {isDetecting ? (
                  <div className="text-center text-white">
                    <div className="text-6xl mb-4">📹</div>
                    <p className="text-lg">Camera Active - Detecting Pose...</p>
                    <p className="text-sm text-gray-400 mt-2">ML Model will be integrated here</p>
                  </div>
                ) : (
                  <div className="text-center text-white">
                    <div className="text-6xl mb-4">📷</div>
                    <p className="text-lg">Click "Start Detection" to begin</p>
                  </div>
                )}
              </div>

              {/* Controls */}
              <div className="flex gap-4">
                <button
                  onClick={() => setIsDetecting(!isDetecting)}
                  className={`flex-1 py-3 rounded-lg font-semibold transition ${
                    isDetecting
                      ? 'bg-red-600 hover:bg-red-700 text-white'
                      : 'bg-indigo-600 hover:bg-indigo-700 text-white'
                  }`}
                >
                  {isDetecting ? 'Stop Detection' : 'Start Detection'}
                </button>
                <button className="px-6 py-3 bg-gray-200 hover:bg-gray-300 rounded-lg font-semibold">
                  📸 Capture
                </button>
              </div>
            </div>

            {/* Real-time Feedback */}
            <div className="bg-white rounded-lg shadow-lg p-6 mt-6">
              <h2 className="text-xl font-semibold mb-4">Real-time Feedback</h2>
              <div className="space-y-3">
                <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                  <div className="flex items-center gap-2">
                    <span className="text-green-600">✓</span>
                    <span className="text-green-800">Good back posture!</span>
                  </div>
                </div>
                <div className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                  <div className="flex items-center gap-2">
                    <span className="text-yellow-600">⚠</span>
                    <span className="text-yellow-800">Lower your hips slightly</span>
                  </div>
                </div>
                <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                  <div className="flex items-center gap-2">
                    <span className="text-blue-600">ℹ</span>
                    <span className="text-blue-800">Keep your knees aligned with toes</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Exercise Selection */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Select Exercise</h2>
              <div className="space-y-2">
                {exercises.map((exercise) => (
                  <button
                    key={exercise.id}
                    onClick={() => setSelectedExercise(exercise.id)}
                    className={`w-full p-4 rounded-lg text-left transition ${
                      selectedExercise === exercise.id
                        ? 'bg-indigo-600 text-white'
                        : 'bg-gray-100 hover:bg-gray-200 text-gray-900'
                    }`}
                  >
                    <div className="flex items-center gap-3">
                      <span className="text-2xl">{exercise.icon}</span>
                      <span className="font-semibold">{exercise.name}</span>
                    </div>
                  </button>
                ))}
              </div>
            </div>

            {/* Stats */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Session Stats</h2>
              <div className="space-y-4">
                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-600">Form Score</span>
                    <span className="font-semibold text-indigo-600">85%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-indigo-600 h-2 rounded-full" style={{ width: '85%' }}></div>
                  </div>
                </div>
                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-600">Reps Completed</span>
                    <span className="font-semibold">12</span>
                  </div>
                </div>
                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-600">Duration</span>
                    <span className="font-semibold">5:23</span>
                  </div>
                </div>
                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-600">Calories</span>
                    <span className="font-semibold">45</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
