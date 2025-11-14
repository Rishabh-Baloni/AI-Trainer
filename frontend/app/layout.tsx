import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'AI Fitness Trainer - Transform Your Fitness Journey',
  description: 'AI-powered personal fitness trainer with real-time pose detection, personalized workouts, and smart nutrition planning',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className="antialiased">{children}</body>
    </html>
  )
}
