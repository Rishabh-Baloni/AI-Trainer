'use client'

import { useState } from 'react'

export default function WorkoutPage() {
  const [selectedDuration, setSelectedDuration] = useState(30)
  const [selectedLevel, setSelectedLevel] = useState('intermediate')

  const todayWorkout = [
    { exercise: 'Warm-up', duration: '5 min', sets: '-', reps: '-' },
    { exercise: 'Squats', duration: '3 min', sets: '3', reps: '15' },
    { exercise: 'Push-ups', duration: '3 min', sets: '3', reps: '12' },
    { exercise: 'Lunges', duration: '4 min', sets: '3', reps: '10 each' },
    { exercise: 'Plank', duration: '3 min', sets: '3', reps: '45 sec' },
    { exercise: 'Cool-down', duration: '5 min', sets: '-', reps: '-' },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex items-center gap-4">
            <a href="/dashboard" className="text-indigo-600 hover:text-indigo-700">← Back</a>
            <h1 className="text-2xl font-bold text-gray-900">Workout Plan</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-6">
            {/* Today's Workout */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-semibold">Today's Workout</h2>
                <span className="px-4 py-2 bg-green-100 text-green-800 rounded-full text-sm font-semibold">
                  Full Body
                </span>
              </div>

              <div className="space-y-3">
                {todayWorkout.map((item, index) => (
                  <div key={index} className="flex items-center justify-between p-4 bg-gray-50 hover:bg-gray-100 rounded-lg transition">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 bg-indigo-600 text-white rounded-full flex items-center justify-center font-semibold">
                        {index + 1}
                      </div>
                      <div>
                        <h4 className="font-semibold text-gray-900">{item.exercise}</h4>
                        <p className="text-sm text-gray-600">{item.duration}</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <p className="text-sm text-gray-600">
                        {item.sets !== '-' && `${item.sets} sets × ${item.reps}`}
                        {item.sets === '-' && item.reps}
                      </p>
                    </div>
                  </div>
                ))}
              </div>

              <button className="w-full mt-6 bg-indigo-600 hover:bg-indigo-700 text-white py-3 rounded-lg font-semibold transition">
                Start Workout
              </button>
            </div>

            {/* Weekly Schedule */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Weekly Schedule</h2>
              <div className="grid grid-cols-7 gap-2">
                {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map((day, index) => (
                  <div
                    key={day}
                    className={`p-3 rounded-lg text-center ${
                      index === 0
                        ? 'bg-indigo-600 text-white'
                        : 'bg-gray-100 text-gray-600'
                    }`}
                  >
                    <div className="text-xs font-semibold">{day}</div>
                    <div className="text-lg mt-1">
                      {index === 0 ? '✓' : index < 5 ? '💪' : '😴'}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Customize Workout */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Customize</h2>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Duration
                  </label>
                  <select
                    value={selectedDuration}
                    onChange={(e) => setSelectedDuration(Number(e.target.value))}
                    className="w-full p-2 border border-gray-300 rounded-lg"
                  >
                    <option value={15}>15 minutes</option>
                    <option value={30}>30 minutes</option>
                    <option value={45}>45 minutes</option>
                    <option value={60}>60 minutes</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Difficulty Level
                  </label>
                  <select
                    value={selectedLevel}
                    onChange={(e) => setSelectedLevel(e.target.value)}
                    className="w-full p-2 border border-gray-300 rounded-lg"
                  >
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                  </select>
                </div>

                <button className="w-full bg-gray-900 hover:bg-gray-800 text-white py-2 rounded-lg font-semibold transition">
                  Generate New Plan
                </button>
              </div>
            </div>

            {/* Progress This Week */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">This Week</h2>
              <div className="space-y-4">
                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-sm text-gray-600">Workouts</span>
                    <span className="text-sm font-semibold">4/5</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-green-600 h-2 rounded-full" style={{ width: '80%' }}></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-sm text-gray-600">Calories</span>
                    <span className="text-sm font-semibold">1,450/1,800</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-orange-600 h-2 rounded-full" style={{ width: '80%' }}></div>
                  </div>
                </div>

                <div className="pt-4 border-t">
                  <div className="text-center">
                    <div className="text-3xl font-bold text-indigo-600">7</div>
                    <div className="text-sm text-gray-600">Day Streak 🔥</div>
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
