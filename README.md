# 🎧 VibeAgent AI Music Recommender

## Overview
This project is an applied AI system that recommends music based on a user’s preferences such as genre, mood, energy level, and acoustic preference.

It extends a basic recommender into an **agent-based AI system** that:
- Validates user input (guardrails)
- Retrieves relevant songs from a dataset
- Scores and ranks songs
- Explains recommendations
- Performs a self-check for reliability

---

## ⚙️ How It Works

1. User enters preferences (genre, mood, energy, acoustic)
2. System validates input (guardrails)
3. AI retrieves matching songs from dataset
4. Songs are scored based on similarity
5. Top recommendations are returned
6. System explains WHY each song was chosen
7. AI performs a self-check to ensure quality

---

## AI Features Implemented

### ✅ Agentic Workflow
The system follows a step-by-step reasoning process:
- Validate → Retrieve → Rank → Self-check

### ✅ Guardrails (Reliability)
- Blocks invalid inputs (e.g., energy outside 0–1)
- Prevents incorrect recommendations

### ✅ Explanation System
Each recommendation includes:
- Score
- Reason (genre match, mood match, energy similarity)

### ✅ Self-Check
The system verifies whether the top result matches user preferences.

---

## System Architecture

![Architecture Diagram](assets/architecture.png)

The system includes:
- CLI Interface (main.py)
- Recommender Agent
- Dataset (songs.csv)
- Scoring Engine
- Self-check Evaluator

---

## Testing & Reliability

- Unit tests using `pytest`
- Manual CLI testing with multiple profiles:
  - High-energy Afrobeat
  - Chill lofi
  - Conflicting preferences
  - Invalid input (guardrail test)

---

## ▶️ How to Run

```bash
pip install pytest
python src/main.py
