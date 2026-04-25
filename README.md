# 🎧 VibeAgent AI Music Recommender

## Original Project (Module 3)
This project is based on my earlier **Music Recommender Simulation** from Module 3.  
The original system focused on recommending songs using simple scoring rules based on genre, mood, and energy.

In this final version, I extended it into a **full applied AI system** by adding an agent workflow, guardrails, and evaluation steps.

---

## Title & Summary
VibeAgent is an AI-powered music recommender that generates personalized song suggestions based on user preferences.

It matters because it demonstrates how AI systems:
- Process user input
- Apply reasoning
- Generate explanations
- Validate outputs for reliability

---

## Architecture Overview

![Architecture Diagram](assets/architecture.png)

The system is made up of:
- CLI Interface (`main.py`)
- Recommender Agent (`Recommender` class)
- Dataset (`songs.csv`)
- Scoring Engine
- Guardrails (input validation)
- Self-check evaluator

Data flows from **user input → validation → retrieval → scoring → output → self-check**

---

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone <repo-link>
cd applied-ai-music-recommender-final