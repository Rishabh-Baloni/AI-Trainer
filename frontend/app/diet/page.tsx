'use client'

import { useState } from 'react'

export default function DietPage() {
  const [selectedDay, setSelectedDay] = useState('today')

  const mealPlan = {
    breakfast: {
      name: 'Protein Oatmeal Bowl',
      calories: 420,
      protein: 25,
      carbs: 55,
      fats: 12,
      items: ['Oats', 'Banana', 'Protein Powder', 'Almonds', 'Honey']
    },
    lunch: {
      name: 'Grilled Chicken Salad',
      calories: 550,
      protein: 45,
      carbs: 35,
      fats: 20,
      items: ['Chicken Breast', 'Mixed Greens', 'Quinoa', 'Olive Oil', 'Avocado']
    },
    dinner: {
      name: 'Salmon with Vegetables',
      calories: 600,
      protein: 40,
      carbs: 45,
      fats: 25,
      items: ['Salmon Fillet', 'Brown Rice', 'Broccoli', 'Sweet Potato', 'Lemon']
    },
    snacks: {
      name: 'Protein Shake & Fruits',
      calories: 230,
      protein: 20,
      carbs: 25,
      fats: 5,
      items: ['Protein Shake', 'Apple', 'Greek Yogurt']
    }
  }

  const totalNutrition = {
    calories: 1800,
    protein: 130,
    carbs: 160,
    fats: 62
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex items-center gap-4">
            <a href="/dashboard" className="text-indigo-600 hover:text-indigo-700">← Back</a>
            <h1 className="text-2xl font-bold text-gray-900">Diet Plan</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-6">
            {/* Daily Overview */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-semibold mb-6">Today's Meal Plan</h2>
              
              {/* Nutrition Summary */}
              <div className="grid grid-cols-4 gap-4 mb-6 p-4 bg-indigo-50 rounded-lg">
                <div className="text-center">
                  <div className="text-2xl font-bold text-indigo-600">{totalNutrition.calories}</div>
                  <div className="text-sm text-gray-600">Calories</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-blue-600">{totalNutrition.protein}g</div>
                  <div className="text-sm text-gray-600">Protein</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-green-600">{totalNutrition.carbs}g</div>
                  <div className="text-sm text-gray-600">Carbs</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-orange-600">{totalNutrition.fats}g</div>
                  <div className="text-sm text-gray-600">Fats</div>
                </div>
              </div>

              {/* Meals */}
              <div className="space-y-4">
                {/* Breakfast */}
                <div className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition">
                  <div className="flex justify-between items-start mb-3">
                    <div>
                      <div className="text-sm text-gray-500 mb-1">🌅 Breakfast</div>
                      <h3 className="text-lg font-semibold">{mealPlan.breakfast.name}</h3>
                    </div>
                    <div className="text-right">
                      <div className="text-lg font-bold text-indigo-600">{mealPlan.breakfast.calories}</div>
                      <div className="text-xs text-gray-500">calories</div>
                    </div>
                  </div>
                  <div className="flex gap-4 text-sm text-gray-600 mb-3">
                    <span>P: {mealPlan.breakfast.protein}g</span>
                    <span>C: {mealPlan.breakfast.carbs}g</span>
                    <span>F: {mealPlan.breakfast.fats}g</span>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {mealPlan.breakfast.items.map((item, i) => (
                      <span key={i} className="px-2 py-1 bg-gray-100 text-gray-700 rounded text-xs">
                        {item}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Lunch */}
                <div className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition">
                  <div className="flex justify-between items-start mb-3">
                    <div>
                      <div className="text-sm text-gray-500 mb-1">☀️ Lunch</div>
                      <h3 className="text-lg font-semibold">{mealPlan.lunch.name}</h3>
                    </div>
                    <div className="text-right">
                      <div className="text-lg font-bold text-indigo-600">{mealPlan.lunch.calories}</div>
                      <div className="text-xs text-gray-500">calories</div>
                    </div>
                  </div>
                  <div className="flex gap-4 text-sm text-gray-600 mb-3">
                    <span>P: {mealPlan.lunch.protein}g</span>
                    <span>C: {mealPlan.lunch.carbs}g</span>
                    <span>F: {mealPlan.lunch.fats}g</span>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {mealPlan.lunch.items.map((item, i) => (
                      <span key={i} className="px-2 py-1 bg-gray-100 text-gray-700 rounded text-xs">
                        {item}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Dinner */}
                <div className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition">
                  <div className="flex justify-between items-start mb-3">
                    <div>
                      <div className="text-sm text-gray-500 mb-1">🌙 Dinner</div>
                      <h3 className="text-lg font-semibold">{mealPlan.dinner.name}</h3>
                    </div>
                    <div className="text-right">
                      <div className="text-lg font-bold text-indigo-600">{mealPlan.dinner.calories}</div>
                      <div className="text-xs text-gray-500">calories</div>
                    </div>
                  </div>
                  <div className="flex gap-4 text-sm text-gray-600 mb-3">
                    <span>P: {mealPlan.dinner.protein}g</span>
                    <span>C: {mealPlan.dinner.carbs}g</span>
                    <span>F: {mealPlan.dinner.fats}g</span>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {mealPlan.dinner.items.map((item, i) => (
                      <span key={i} className="px-2 py-1 bg-gray-100 text-gray-700 rounded text-xs">
                        {item}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Snacks */}
                <div className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition">
                  <div className="flex justify-between items-start mb-3">
                    <div>
                      <div className="text-sm text-gray-500 mb-1">🍪 Snacks</div>
                      <h3 className="text-lg font-semibold">{mealPlan.snacks.name}</h3>
                    </div>
                    <div className="text-right">
                      <div className="text-lg font-bold text-indigo-600">{mealPlan.snacks.calories}</div>
                      <div className="text-xs text-gray-500">calories</div>
                    </div>
                  </div>
                  <div className="flex gap-4 text-sm text-gray-600 mb-3">
                    <span>P: {mealPlan.snacks.protein}g</span>
                    <span>C: {mealPlan.snacks.carbs}g</span>
                    <span>F: {mealPlan.snacks.fats}g</span>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {mealPlan.snacks.items.map((item, i) => (
                      <span key={i} className="px-2 py-1 bg-gray-100 text-gray-700 rounded text-xs">
                        {item}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Goals */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Your Goals</h2>
              <div className="space-y-4">
                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-sm text-gray-600">Daily Calories</span>
                    <span className="text-sm font-semibold">1800/2000</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-green-600 h-2 rounded-full" style={{ width: '90%' }}></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-sm text-gray-600">Protein</span>
                    <span className="text-sm font-semibold">130/150g</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-blue-600 h-2 rounded-full" style={{ width: '87%' }}></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between mb-1">
                    <span className="text-sm text-gray-600">Water</span>
                    <span className="text-sm font-semibold">2.1/3L</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-cyan-600 h-2 rounded-full" style={{ width: '70%' }}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Quick Actions */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Quick Actions</h2>
              <div className="space-y-2">
                <button className="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 rounded-lg font-semibold transition">
                  Log Meal
                </button>
                <button className="w-full bg-gray-900 hover:bg-gray-800 text-white py-2 rounded-lg font-semibold transition">
                  Generate New Plan
                </button>
                <button className="w-full bg-gray-200 hover:bg-gray-300 text-gray-900 py-2 rounded-lg font-semibold transition">
                  View Recipes
                </button>
              </div>
            </div>

            {/* Dietary Preferences */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Preferences</h2>
              <div className="space-y-2">
                <div className="flex items-center gap-2">
                  <span className="text-green-600">✓</span>
                  <span className="text-sm">High Protein</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-green-600">✓</span>
                  <span className="text-sm">Low Carb</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-gray-400">○</span>
                  <span className="text-sm text-gray-500">Vegetarian</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-gray-400">○</span>
                  <span className="text-sm text-gray-500">Vegan</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
