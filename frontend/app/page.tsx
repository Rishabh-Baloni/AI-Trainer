'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'

export default function Home() {
  const [scrolled, setScrolled] = useState(false)
  const [activeFeature, setActiveFeature] = useState(0)

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveFeature((prev) => (prev + 1) % 3)
    }, 3000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-white">
      {/* Navigation */}
      <nav className={`fixed w-full z-50 transition-all duration-300 ${scrolled ? 'bg-white shadow-md' : 'bg-transparent'}`}>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <span className="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
                AI Fitness Trainer
              </span>
            </div>
            <div className="hidden md:flex items-center space-x-8">
              <a href="#features" className="text-gray-700 hover:text-indigo-600 transition">Features</a>
              <a href="#how-it-works" className="text-gray-700 hover:text-indigo-600 transition">How It Works</a>
              <Link href="/analytics" className="text-gray-700 hover:text-indigo-600 transition">Analytics</Link>
              <a href="#pricing" className="text-gray-700 hover:text-indigo-600 transition">Pricing</a>
              <Link href="/dashboard" className="bg-indigo-600 text-white px-6 py-2 rounded-full hover:bg-indigo-700 transition">
                Get Started
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section - ENHANCED WITH REAL DESIGN */}
      <section className="relative pt-32 pb-20 px-4 overflow-hidden">
        {/* Animated Background */}
        <div className="absolute inset-0 bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500">
          <div className="absolute inset-0 opacity-30">
            <div className="absolute top-20 left-10 w-72 h-72 bg-white rounded-full mix-blend-overlay filter blur-3xl animate-pulse"></div>
            <div className="absolute top-40 right-20 w-96 h-96 bg-pink-300 rounded-full mix-blend-overlay filter blur-3xl animate-pulse" style={{animationDelay: '1s'}}></div>
            <div className="absolute bottom-20 left-1/3 w-80 h-80 bg-yellow-300 rounded-full mix-blend-overlay filter blur-3xl animate-pulse" style={{animationDelay: '2s'}}></div>
          </div>
        </div>

        <div className="max-w-7xl mx-auto relative z-10">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            {/* Left Content */}
            <div className="text-white">
              <div className="inline-flex items-center gap-2 mb-6 px-4 py-2 bg-white/20 backdrop-blur-sm rounded-full text-sm font-semibold border border-white/30">
                <span className="relative flex h-3 w-3">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
                </span>
                <span>AI-Powered • Real-time Analysis</span>
              </div>
              
              <h1 className="text-6xl md:text-7xl font-black mb-6 leading-tight">
                AI-Powered
                <span className="block text-yellow-300">Fitness Trainer</span>
              </h1>
              
              <p className="text-xl text-indigo-100 mb-8 leading-relaxed">
                Real-time pose detection with MediaPipe, automatic rep counting, and smart workout analytics—powered by machine learning.
              </p>
              
              <div className="flex flex-col sm:flex-row gap-4 mb-8">
                <Link href="/dashboard" className="group bg-white text-indigo-600 px-8 py-4 rounded-2xl text-lg font-bold hover:shadow-2xl transition-all duration-300 text-center flex items-center justify-center gap-2">
                  <span>Start Your Journey</span>
                  <svg className="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </Link>
                <Link href="/pose-detection" className="bg-white/10 backdrop-blur-sm text-white border-2 border-white/30 px-8 py-4 rounded-2xl text-lg font-bold hover:bg-white/20 transition text-center">
                  Try Demo
                </Link>
              </div>

              {/* Trust Badges */}
              <div className="flex items-center gap-8 text-sm">
                <div className="flex items-center gap-2">
                  <svg className="w-5 h-5 text-green-300" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  <span className="text-indigo-100">Free & Open Source</span>
                </div>
                <div className="flex items-center gap-2">
                  <svg className="w-5 h-5 text-green-300" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  <span className="text-indigo-100">Browser-Based</span>
                </div>
                <div className="flex items-center gap-2">
                  <svg className="w-5 h-5 text-green-300" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  <span className="text-indigo-100">No Installation</span>
                </div>
              </div>
            </div>

            {/* Right - Interactive Feature Showcase */}
            <div className="relative">
              {/* Main Card */}
              <div className="relative bg-white rounded-3xl shadow-2xl overflow-hidden">
                {/* Animated Feature Tabs */}
                <div className="flex border-b border-gray-200">
                  {['Pose Detection', 'Workouts', 'Nutrition'].map((tab, idx) => (
                    <button
                      key={idx}
                      onClick={() => setActiveFeature(idx)}
                      className={`flex-1 px-4 py-4 text-sm font-semibold transition-all ${
                        activeFeature === idx
                          ? 'text-indigo-600 border-b-2 border-indigo-600 bg-indigo-50'
                          : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                      }`}
                    >
                      {tab}
                    </button>
                  ))}
                </div>

                {/* Feature Content */}
                <div className="p-8">
                  {activeFeature === 0 && (
                    <div className="space-y-4 animate-fadeIn">
                      <div className="aspect-video bg-gradient-to-br from-blue-500 to-cyan-500 rounded-2xl flex items-center justify-center relative overflow-hidden">
                        <div className="absolute inset-0 bg-grid-white/10"></div>
                        <div className="relative text-white text-center">
                          <div className="text-6xl mb-3">📹</div>
                          <p className="font-semibold text-lg">Real-time Form Analysis</p>
                        </div>
                      </div>
                      <div className="grid grid-cols-2 gap-3">
                        <div className="bg-green-50 p-4 rounded-xl border border-green-200">
                          <div className="flex items-center gap-2 mb-2">
                            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                            <span className="text-sm font-semibold text-green-900">Excellent Form</span>
                          </div>
                          <p className="text-xs text-green-700">95% Accuracy</p>
                        </div>
                        <div className="bg-blue-50 p-4 rounded-xl border border-blue-200">
                          <div className="flex items-center gap-2 mb-2">
                            <div className="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></div>
                            <span className="text-sm font-semibold text-blue-900">Live Tracking</span>
                          </div>
                          <p className="text-xs text-blue-700">30 FPS</p>
                        </div>
                      </div>
                    </div>
                  )}

                  {activeFeature === 1 && (
                    <div className="space-y-4 animate-fadeIn">
                      <div className="aspect-video bg-gradient-to-br from-purple-500 to-pink-500 rounded-2xl flex items-center justify-center">
                        <div className="text-white text-center">
                          <div className="text-6xl mb-3">💪</div>
                          <p className="font-semibold text-lg">Personalized Plans</p>
                        </div>
                      </div>
                      <div className="space-y-2">
                        {['Full Body Circuit', 'Upper Body Focus', 'Core Strength'].map((workout, idx) => (
                          <div key={idx} className="flex items-center justify-between p-3 bg-gray-50 rounded-xl">
                            <div className="flex items-center gap-3">
                              <div className="w-8 h-8 bg-purple-600 rounded-lg flex items-center justify-center text-white text-sm font-bold">
                                {idx + 1}
                              </div>
                              <span className="font-semibold text-gray-900">{workout}</span>
                            </div>
                            <span className="text-sm text-gray-500">30 min</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {activeFeature === 2 && (
                    <div className="space-y-4 animate-fadeIn">
                      <div className="aspect-video bg-gradient-to-br from-orange-500 to-red-500 rounded-2xl flex items-center justify-center">
                        <div className="text-white text-center">
                          <div className="text-6xl mb-3">🍎</div>
                          <p className="font-semibold text-lg">Smart Nutrition</p>
                        </div>
                      </div>
                      <div className="grid grid-cols-4 gap-2">
                        {[
                          { label: 'Calories', value: '1800', color: 'orange' },
                          { label: 'Protein', value: '120g', color: 'blue' },
                          { label: 'Carbs', value: '180g', color: 'green' },
                          { label: 'Fats', value: '60g', color: 'yellow' }
                        ].map((macro, idx) => (
                          <div key={idx} className={`bg-${macro.color}-50 p-3 rounded-xl text-center`}>
                            <div className={`text-lg font-bold text-${macro.color}-600`}>{macro.value}</div>
                            <div className="text-xs text-gray-600">{macro.label}</div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              </div>

              {/* Floating Stats */}
              <div className="absolute -bottom-6 -left-6 bg-white rounded-2xl shadow-xl p-4 border border-gray-100">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                    <span className="text-2xl">🤖</span>
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-gray-900">3 AI Models</div>
                    <div className="text-xs text-gray-600">ML Powered</div>
                  </div>
                </div>
              </div>

              <div className="absolute -top-6 -right-6 bg-white rounded-2xl shadow-xl p-4 border border-gray-100">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
                    <span className="text-2xl">🎯</span>
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-gray-900">Real-Time</div>
                    <div className="text-xs text-gray-600">Pose Detection</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-4 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">AI-Powered Features</h2>
            <p className="text-xl text-gray-600">Machine Learning technology for your fitness journey</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: '📹',
                title: 'MediaPipe Pose Detection',
                description: 'Real-time pose tracking using Google\'s MediaPipe. Tracks 33 body landmarks with instant form feedback.',
                color: 'from-blue-500 to-cyan-500'
              },
              {
                icon: '🔢',
                title: 'Automatic Rep Counting',
                description: 'AI analyzes your movement and counts reps automatically for squats, pushups, and planks.',
                color: 'from-purple-500 to-pink-500'
              },
              {
                icon: '📊',
                title: 'Smart Analytics Engine',
                description: 'Track workout history, calories burned, and get personalized insights with linear regression predictions.',
                color: 'from-orange-500 to-red-500'
              },
              {
                icon: '⚡',
                title: 'WebSocket Real-Time',
                description: 'Live video processing at 30 FPS with smooth performance and instant feedback on your form.',
                color: 'from-green-500 to-teal-500'
              },
              {
                icon: '💯',
                title: 'Form Score Calculation',
                description: 'Get a 0-100% form score based on body angles, alignment, and proper exercise technique.',
                color: 'from-indigo-500 to-blue-500'
              },
              {
                icon: '🔥',
                title: 'Gamification & Rewards',
                description: 'Stay motivated with streaks, badges, challenges, and a supportive community.',
                color: 'from-yellow-500 to-orange-500'
              }
            ].map((feature, index) => (
              <div key={index} className="group relative bg-white rounded-2xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 border border-gray-100 hover:border-transparent">
                <div className={`absolute inset-0 bg-gradient-to-r ${feature.color} rounded-2xl opacity-0 group-hover:opacity-10 transition-opacity`}></div>
                <div className="relative">
                  <div className="text-5xl mb-4">{feature.icon}</div>
                  <h3 className="text-xl font-bold text-gray-900 mb-3">{feature.title}</h3>
                  <p className="text-gray-600 leading-relaxed">{feature.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section id="how-it-works" className="py-20 px-4 bg-gray-50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">How It Works</h2>
            <p className="text-xl text-gray-600">Get started in 3 simple steps</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              { step: '01', title: 'Create Your Profile', description: 'Tell us about your fitness level, goals, and preferences. Our AI analyzes your data to create a personalized plan.', icon: '👤' },
              { step: '02', title: 'Start Your Workout', description: 'Follow AI-guided exercises with real-time form correction through your camera. Get instant feedback and tips.', icon: '🏋️' },
              { step: '03', title: 'Track Progress', description: 'Monitor your improvements with detailed analytics. AI adapts your plan as you get stronger and fitter.', icon: '📈' }
            ].map((item, index) => (
              <div key={index} className="relative">
                <div className="bg-white rounded-2xl p-8 shadow-lg">
                  <div className="text-6xl mb-4 text-center">{item.icon}</div>
                  <div className="text-5xl font-bold text-indigo-100 absolute top-4 right-4">{item.step}</div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-4">{item.title}</h3>
                  <p className="text-gray-600 leading-relaxed">{item.description}</p>
                </div>
                {index < 2 && (
                  <div className="hidden md:block absolute top-1/2 -right-4 transform -translate-y-1/2 text-4xl text-indigo-300">→</div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 px-4 bg-gradient-to-r from-indigo-600 to-purple-600 text-white">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 text-center">
            {[
              { number: '33+', label: 'Body Landmarks' },
              { number: '3', label: 'Exercise Types' },
              { number: 'Real-Time', label: 'Form Analysis' },
              { number: 'Auto', label: 'Rep Counting' }
            ].map((stat, index) => (
              <div key={index}>
                <div className="text-5xl font-bold mb-2">{stat.number}</div>
                <div className="text-indigo-100">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
            Ready to Start Your AI-Powered Fitness Journey?
          </h2>
          <p className="text-xl text-gray-600 mb-8">
            Experience the future of fitness training with real-time AI pose detection and personalized analytics.
          </p>
          <Link href="/dashboard" className="inline-block bg-indigo-600 text-white px-12 py-4 rounded-full text-lg font-semibold hover:bg-indigo-700 transition transform hover:scale-105">
            Try Pose Detection Now
          </Link>
          <p className="text-sm text-gray-500 mt-4">Free to use • No signup required</p>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-12 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="text-2xl font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent mb-4">
                AI Fitness Trainer
              </div>
              <p className="text-sm text-gray-400">Your AI-powered personal fitness coach, available 24/7.</p>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Product</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white transition">Features</a></li>
                <li><a href="#" className="hover:text-white transition">Pricing</a></li>
                <li><a href="#" className="hover:text-white transition">FAQ</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Company</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white transition">About</a></li>
                <li><a href="#" className="hover:text-white transition">Blog</a></li>
                <li><a href="#" className="hover:text-white transition">Contact</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Legal</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white transition">Privacy</a></li>
                <li><a href="#" className="hover:text-white transition">Terms</a></li>
                <li><a href="#" className="hover:text-white transition">License</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-sm text-gray-500">
            <p>&copy; 2025 AI Fitness Trainer. Academic Project by Rishabh Baloni & Siddhant Negi.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
