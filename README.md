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

pip install pytest
python src/main.py

-----

### 🎮 Sample Interactions
🔹 Example 1: High-Energy Afrobeats

Input:
Genre: Afrobeat
Mood: Happy
Energy: 0.9
Acoustic: No

Output:
--- SYSTEM TRACE ---
Step 1: Validate user preferences.
Step 2: Retrieve candidate songs from the dataset.
Step 3: Rank 4 candidate songs using scoring rules.
Step 4: Self-check recommendation quality.

🎵 TOP RECOMMENDATIONS:

1. Golden Fire by Luna Vale
   Score: 4.75
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.93), non-acoustic preference match (+0.82)

2. Sunrise Parade by Temi Cole
   Score: 4.75
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.89), non-acoustic preference match (+0.86)

🔍 SELF CHECK:
Top recommendation passed because it matches the user's genre or mood preference.

🔹 Example 2: Chill Lofi

Input:
Genre: Lofi
Mood: Calm
Energy: 0.3
Acoustic: Yes

Output:
--- SYSTEM TRACE ---
Step 1: Validate user preferences.
Step 2: Retrieve candidate songs from the dataset.
Step 3: Rank 5 candidate songs using scoring rules.
Step 4: Self-check recommendation quality.

🎵 TOP RECOMMENDATIONS:

1. Library Rain by Paper Lanterns
   Score: 4.86
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+1.00), acoustic preference match (+0.86)

2. Midnight Coding by LoRoom
   Score: 4.64
   Why: genre match (+2.0), mood match (+1.0), energy similarity (+0.93), acoustic preference match (+0.71)

🔍 SELF CHECK:
Top recommendation passed because it matches the user's genre or mood preference.

🔹 Example 3: Invalid Input (Guardrail)

Input:
Genre: Pop
Mood: Happy
Energy: 2.0
Acoustic: No

Output:
--- SYSTEM TRACE ---
Step 1: Validate user preferences.

❌ Guardrail blocked this input:
- target_energy must be between 0 and 1.

-----

### ⚙️Design Decisions
I used an agent-based workflow (validate → retrieve → rank → self-check) to make the system more structured.
I chose rule-based scoring instead of ML models for simplicity and clarity.
I added explanations to make the system transparent and easier to understand.

Trade-off:

Simpler logic = easier to debug
But less powerful than real machine learning systems

-----

### Testing Summary

What worked:

Recommendations generated correctly
Guardrails blocked invalid inputs
Self-check validated outputs

What didn’t:

Early bugs with missing methods (agent_recommend)
Import errors during integration

What I learned:

AI systems require strong testing and debugging
Components must be connected correctly to work

-----

### 💭Reflection

In this project, I extended a basic recommender into a full AI system with reasoning and validation.

AI tools helped me debug issues and implement features like the agent workflow, but sometimes gave incorrect suggestions, which I had to manually fix. This showed me that AI is useful but still requires human understanding.

Adding guardrails and a self-check improved the system’s reliability and made it more trustworthy.

One limitation is that the system uses simple scoring instead of machine learning. In the future, I would improve it by using larger datasets and more advanced models.

Overall, this project helped me understand how real AI systems combine data, logic, and evaluation to produce meaningful results.

------

