# 🧠 FemMind AI: Women's Wellness Companion

FemMind AI is an intelligent multi-agent women’s wellness assistant built using the **Google Agent Development Kit (ADK)**.  
It helps women with:

- 💪 Fitness  
- 🧠 Mental Health  
- 🍎 Nutrition  
- 🌸 Reproductive Health  
- 🌿 Lifestyle & General Wellness  

A central **Wellness Root Agent** routes user questions to the right specialized wellness agent to provide accurate, safe, friendly, and supportive answers.

![FemMind AI Thumbnail](app/assets/thumbnail.png)

---

## 🎯 Problem Statement

Women often struggle to find trusted, personalized, and friendly guidance about their health and wellness.  
Information is scattered, confusing, and often not beginner-friendly.

---

## 💡 Solution Statement

FemMind AI brings all major wellness categories into one place using a powerful multi-agent AI system.  
Each agent specializes in one domain and works together to provide:

- Simple health advice  
- Emotional support  
- Beginner-friendly fitness guidance  
- Nutrition suggestions  
- Reproductive health awareness  

The result is a **safe and supportive wellness experience for women**.

---

## 🏛️ Architecture

FemMind AI uses a multi-agent system designed for clarity, modularity, and scalability.  
The system consists of one orchestrator (**Wellness Root Agent**) and five specialized wellness agents:

![FemMind AI Architecture](app/assets/architecture.png)

### 🌿 1. Wellness Root Agent (Orchestrator)
- Understands the user’s message  
- Determines the required wellness domain  
- Routes the query to the correct sub-agent  
- Collects and unifies the final response  

### 🍎 2. Nutrition Agent
- Meal suggestions  
- Vitamin/mineral guidance  
- Weight loss/gain food plans  
- Healthy eating routines  

### 🧠 3. Mental Health Agent
- Emotional support  
- Stress and anxiety relief tips  
- Mindfulness and self-care routines  

### 🌸 4. Reproductive Health Agent
- Menstrual cycle awareness  
- PMS/PCOS/PCOD education  
- Hormonal wellness guidance  
- Pregnancy-related general advice  

### 💪 5. Fitness Agent
- Workout routines  
- Home exercises  
- Fat loss/muscle gain tips  
- Beginner-friendly fitness plans  

---

## 🔄 Workflow

1. User sends a message  
2. Root Agent analyzes intent  
3. Root Agent selects the correct sub-agent(s)  
4. Sub-agent generates domain-specific answer  
5. Root Agent returns the final, unified response  

This ensures **accuracy, safety, and a supportive tone**.

---

## 🧩 Project Structure

femmind-ai/
├── app/
│   ├── models/
│   │   ├── agents.py      # Multi-agent AI system
│   │   ├── memory.py      # Memory system with Pandas/NumPy
│   │   └── __init__.py
│   ├── routes.py          # Flask web interface for chat & analytics
│   ├── main.py            # Entry point
│   └── assets/
│       ├── thumbnail.png
│       └── architecture.png
├── requirements.txt       # Required packages
└── README.md

Notes:

agents.py contains the multi-agent system and agent logic

memory.py contains the MemorySystem class for storing user interactions and analytics

routes.py contains the Flask routes (/, /chat) and web UI

main.py starts the app

# ⚙️ Installation

Clone the repository:
git clone https://github.com/yourusername/femmind-ai.git
cd femmind-ai

2. Create virtual environment:
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

# ▶️ Running Locally (Optional)

Start the Flask app:

python main.py


Open your browser at:
http://127.0.0.1:5000

⚠️ This only works on your local machine. Mainly for developers who want to test or contribute.

# 🌐 Live Demo (Recommended)

Try FemMind AI online:
https://uroojzaidi.pythonanywhere.com/

# 🏁 Conclusion

FemMind AI is a modern multi-agent wellness system designed specifically for women.
It combines emotional support, nutrition, fitness, and reproductive health into one intelligent and compassionate platform.

## ⭐ Key Features

Multi-agent AI design

Real-world women’s wellness applications

Google ADK integration

Modular and scalable architecture

Beautiful web interface with Flask

FemMind AI empowers women with accessible, compassionate, and intelligent wellness support anytime, anywhere.

# 🏷️ GitHub Badges

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AI](https://img.shields.io/badge/AI-MultiAgent-purple)
![Gemini](https://img.shields.io/badge/Google-ADK-orange)
![Wellness](https://img.shields.io/badge/Women's_Health-pink)

# ✅ Summary

5 specialized AI wellness agents

Multi-agent coordination system

Gemini AI integration

Pandas/NumPy analytics

Beautiful Flask UI for interactive chat

Live Demo: https://uroojzaidi.pythonanywhere.com
