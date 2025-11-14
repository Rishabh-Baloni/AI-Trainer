'use client'

import { useState } from 'react'
import Link from 'next/link'

export default function DashboardPage() {
  const [timeRange, setTimeRange] = useState('week')

  const stats = [
    { label: 'Workouts Completed', value: '24', change: '+12%', icon: '💪', color: 'from-blue-500 to-cyan-500' },
    { label: 'Calories Burned', value: '5,420', change: '+8%', icon: '🔥', color: 'from-orange-500 to-red-500' },
    { label: 'Current Streak', value: '12 days', change: 'New Record!', icon: '⚡', color: 'from-yellow-500 to-orange-500' },
    { label: 'Form Accuracy', value: '92%', change: '+5%', icon: '🎯', color: 'from-green-500 to-teal-500' },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Top Navigation */}
      <nav className="bg-white shadow-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <Link href="/" className="flex items-center">
              <span className="text-xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
                AI Fitness Trainer
              </span>
            </Link>
            <div className="flex items-center gap-4">
              <button className="p-2 hover:bg-gray-100 rounded-lg transition">
                <span className="text-xl">🔔</span>
              </button>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-full flex items-center justify-center text-white font-semibold">
                  RB
                </div>
                <div className="hidden md:block">
                  <div className="text-sm font-semibold text-gray-900">Rishabh Baloni</div>
                  <div className="text-xs text-gray-500">Pro Member</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Welcome Banner */}
        <div className="bg-gradient-to-r from-indigo-600 to-purple-600 rounded-2xl p-8 mb-8 text-white relative overflow-hidden">
          <div className="absolute right-0 top-0 opacity-10">
            <div className="text-9xl">💪</div>
          </div>
          <div className="relative z-10">
            <h1 className="text-3xl font-bold mb-2">Welcome back, Rishabh!</h1>
            <p className="text-indigo-100 mb-6">Keep pushing toward your goals!</p>
            <div className="flex flex-wrap gap-4">
              <Link href="/workout" className="bg-white text-indigo-600 px-6 py-3 rounded-full font-semibold hover:bg-indigo-50 transition">
                Start Workout
              </Link>
              <Link href="/pose-detection" className="bg-indigo-700 text-white px-6 py-3 rounded-full font-semibold hover:bg-indigo-800 transition">
                Try Pose Detection
              </Link>
            </div>
          </div>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {stats.map((stat, index) => (
            <div key={index} className="group bg-white rounded-xl shadow-sm hover:shadow-lg transition-all p-6 relative overflow-hidden">
              <div className={`absolute inset-0 bg-gradient-to-r ${stat.color} opacity-0 group-hover:opacity-5 transition-opacity`}></div>
              <div className="relative">
                <div className="flex justify-between items-start mb-4">
                  <div className="text-3xl">{stat.icon}</div>
                  <span className="text-xs font-semibold text-green-600 bg-green-50 px-2 py-1 rounded-full">
                    {stat.change}
                  </span>
                </div>
                <div className="text-3xl font-bold text-gray-900 mb-1">{stat.value}</div>
                <div className="text-sm text-gray-600">{stat.label}</div>
              </div>
            </div>
          ))}
        </div>

        {/* Main Content Grid */}
        <div className="grid lg:grid-cols-3 gap-8">
          {/* Left Column - Main Content */}
          <div className="lg:col-span-2 space-y-6">
            {/* Quick Actions Cards */}
            <div className="grid sm:grid-cols-3 gap-4">
              <Link href="/workout" className="group bg-white rounded-xl p-6 shadow-sm hover:shadow-lg transition-all">
                <div className="text-4xl mb-3 group-hover:scale-110 transition-transform">🏋️</div>
                <h3 className="font-semibold text-gray-900 mb-1">Start Workout</h3>
                <p className="text-sm text-gray-600">Begin session</p>
              </Link>
              <Link href="/pose-detection" className="group bg-white rounded-xl p-6 shadow-sm hover:shadow-lg transition-all">
                <div className="text-4xl mb-3 group-hover:scale-110 transition-transform">📹</div>
                <h3 className="font-semibold text-gray-900 mb-1">Pose Check</h3>
                <p className="text-sm text-gray-600">Analyze form</p>
              </Link>
              <Link href="/diet" className="group bg-white rounded-xl p-6 shadow-sm hover:shadow-lg transition-all">
                <div className="text-4xl mb-3 group-hover:scale-110 transition-transform">🍎</div>
                <h3 className="font-semibold text-gray-900 mb-1">Meal Plan</h3>
                <p className="text-sm text-gray-600">View meals</p>
              </Link>
            </div>

            {/* Today's Workout */}
            <div className="bg-white rounded-xl shadow-sm p-6">
              <div className="flex justify-between items-center mb-6">
                <h2 className="text-xl font-bold text-gray-900">Today's Workout</h2>
                <Link href="/workout" className="text-indigo-600 hover:text-indigo-700 text-sm font-semibold">
                  View All →
                </Link>
              </div>
              <div className="space-y-3">
                {[
                  { name: 'Squats', sets: '3x15', completed: true },
                  { name: 'Push-ups', sets: '3x12', completed: true },
                  { name: 'Plank', sets: '3x45s', completed: false },
                  { name: 'Lunges', sets: '3x10', completed: false },
                ].map((exercise, index) => (
                  <div key={index} className={`flex items-center justify-between p-4 rounded-lg ${exercise.completed ? 'bg-green-50 border border-green-100' : 'bg-gray-50'}`}>
                    <div className="flex items-center gap-4">
                      <div className={`w-10 h-10 rounded-full flex items-center justify-center font-semibold ${exercise.completed ? 'bg-green-600 text-white' : 'bg-gray-300 text-gray-600'}`}>
                        {exercise.completed ? '✓' : index + 1}
                      </div>
                      <div>
                        <div className={`font-semibold ${exercise.completed ? 'text-green-900' : 'text-gray-900'}`}>
                          {exercise.name}
                        </div>
                        <div className="text-sm text-gray-600">{exercise.sets}</div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Weekly Progress */}
            <div className="bg-white rounded-xl shadow-sm p-6">
              <h2 className="text-xl font-bold text-gray-900 mb-6">Weekly Progress</h2>
              <div className="space-y-4">
                {[
                  { day: 'Mon', workouts: 2, percentage: 100 },
                  { day: 'Tue', workouts: 1, percentage: 70 },
                  { day: 'Wed', workouts: 2, percentage: 100 },
                  { day: 'Thu', workouts: 1, percentage: 60 },
                  { day: 'Fri', workouts: 2, percentage: 90 },
                  { day: 'Sat', workouts: 0, percentage: 0 },
                  { day: 'Sun', workouts: 0, percentage: 0 },
                ].map((day, index) => (
                  <div key={index} className="flex items-center gap-4">
                    <div className="w-12 text-sm font-medium text-gray-600">{day.day}</div>
                    <div className="flex-1">
                      <div className="w-full bg-gray-200 rounded-full h-3">
                        <div 
                          className="bg-gradient-to-r from-indigo-600 to-purple-600 h-3 rounded-full transition-all"
                          style={{ width: `${day.percentage}%` }}
                        ></div>
                      </div>
                    </div>
                    <div className="w-20 text-sm text-gray-600 text-right">
                      {day.workouts > 0 ? `${day.workouts} workout${day.workouts > 1 ? 's' : ''}` : 'Rest'}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Right Sidebar */}
          <div className="space-y-6">
            {/* Daily Goals */}
            <div className="bg-white rounded-xl shadow-sm p-6">
              <h3 className="font-semibold text-gray-900 mb-4">Daily Goals</h3>
              <div className="space-y-4">
                <div>
                  <div className="flex justify-between text-sm mb-2">
                    <span className="text-gray-600">Calories</span>
                    <span className="font-semibold text-gray-900">420/600</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-orange-500 h-2 rounded-full" style={{ width: '70%' }}></div>
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-sm mb-2">
                    <span className="text-gray-600">Active Minutes</span>
                    <span className="font-semibold text-gray-900">28/45</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-blue-500 h-2 rounded-full" style={{ width: '62%' }}></div>
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-sm mb-2">
                    <span className="text-gray-600">Water</span>
                    <span className="font-semibold text-gray-900">6/8 cups</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-cyan-500 h-2 rounded-full" style={{ width: '75%' }}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Achievements */}
            <div className="bg-white rounded-xl shadow-sm p-6">
              <h3 className="font-semibold text-gray-900 mb-4">Achievements</h3>
              <div className="space-y-3">
                {[
                  { icon: '🔥', title: '7 Day Streak', desc: 'Unlocked today!' },
                  { icon: '💪', title: 'Strong Start', desc: '25 workouts' },
                  { icon: '🎯', title: 'Form Master', desc: '90%+ accuracy' },
                ].map((achievement, index) => (
                  <div key={index} className="flex items-center gap-3 p-3 bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg">
                    <div className="text-2xl">{achievement.icon}</div>
                    <div>
                      <div className="font-semibold text-sm text-gray-900">{achievement.title}</div>
                      <div className="text-xs text-gray-600">{achievement.desc}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Nutrition Summary */}
            <div className="bg-white rounded-xl shadow-sm p-6">
              <div className="flex justify-between items-center mb-4">
                <h3 className="font-semibold text-gray-900">Nutrition</h3>
                <Link href="/diet" className="text-indigo-600 text-sm font-semibold">View</Link>
              </div>
              <div className="space-y-3">
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-600">Calories</span>
                  <span className="text-sm font-semibold">1,420/1,800</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-600">Protein</span>
                  <span className="text-sm font-semibold">85g/120g</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-600">Carbs</span>
                  <span className="text-sm font-semibold">140g/180g</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-600">Fats</span>
                  <span className="text-sm font-semibold">45g/60g</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
