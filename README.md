# 🍳 AI Recipe Generator using Gemini API

Generate personalized recipes instantly using Google Gemini AI — based on your available ingredients, cuisine preference, and dietary needs.

Built with **Python**, **Streamlit**, and **Google Gemini API**.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Tools & Tech](#️-tools--tech)
- [Architecture](#-architecture)
- [Skills Demonstrated](#-skills-demonstrated)
- [Project Structure](#-project-structure)
- [Walkthrough](#-walkthrough)
- [How to Run](#️-how-to-run)
- [Sample Input & Output](#-sample-input--output)
- [Results](#-results)
- [Future Work](#-future-work)
- [Author & Contact](#-author--contact)

---

## 🔍 Overview
This is an AI-powered web application that turns a simple list of ingredients into a complete, structured recipe. The user enters what they have on hand, picks a cuisine and dietary preference, and Gemini generates a recipe title, ingredient list, step-by-step instructions, and estimated cooking time — all through a clean Streamlit interface.

The project demonstrates practical LLM integration: prompt design, structured output generation, and wrapping an API-driven model inside a usable, user-facing product.

## ❓ Problem Statement
Deciding what to cook with limited or random ingredients is a common daily friction point. Most recipe apps rely on static databases and rigid search filters, which fail when the user's exact ingredient combination isn't pre-catalogued. This project solves that by using an LLM to generate a recipe on the fly for *any* combination of ingredients, cuisine, and diet — no fixed database required.

## 🛠️ Tools & Tech
| Technology | Purpose |
|---|---|
| Python | Backend logic |
| Streamlit | Web application UI |
| Google Gemini API | Recipe generation (LLM) |
| python-dotenv | Secure API key management |

## 🏗️ Architecture
```
User Input (Ingredients, Cuisine, Diet)
        │
        ▼
Prompt Construction (Prompt Engineering)
        │
        ▼
Google Gemini API Call
        │
        ▼
Structured Response Parsing (Title, Ingredients, Steps, Time)
        │
        ▼
Streamlit UI Rendering
```

## 💡 Skills Demonstrated
- LLM API Integration (Google Gemini)
- Prompt Engineering for structured, consistent output
- Environment variable / secrets management (`.env`)
- Streamlit application development
- Python application design (modular, readable `app.py`)

## 📂 Project Structure
```text
AI-Recipe-Generator-Gemini-Streamlit/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed to repo)
├── README.md
│
└── screenshots/        # App UI screenshots
```

## 🚶 Walkthrough

**1. User Input**
The user enters comma-separated ingredients and selects cuisine type and dietary preference from dropdowns.

**2. Prompt Engineering**
User inputs are formatted into a structured prompt instructing Gemini to return a recipe with a defined format: title, ingredients, numbered steps, and cooking time — keeping output consistent and parseable.

**3. API Call**
The formatted prompt is sent to the Gemini API using the key loaded securely from `.env`.

**4. Response Rendering**
The generated recipe is parsed and displayed in a clean, readable layout within the Streamlit app.

## ⚙️ How to Run

### 1. Clone Repository
```bash
git clone https://github.com/Sahajahanur/AI-Recipe-Generator-Gemini-Streamlit.git
cd AI-Recipe-Generator-Gemini-Streamlit
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```
Activate it:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Gemini API Key
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_api_key_here
```
Get your key from: [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Run the App
```bash
streamlit run app.py
```
Opens at: `http://localhost:8501`

## 📸 Sample Input & Output

**Input**
| Field | Value |
|---|---|
| Ingredients | Tomato, Onion, Lentils, Salt, Jeera |
| Cuisine | Indian |
| Diet | Vegan |

<img width="1112" height="732" alt="image" src="https://github.com/user-attachments/assets/e4b0b54b-6c93-4439-8cde-2f6141f0393f" />


**Output — Simple Tomato Dal**

*Ingredients*
- 1 cup red lentils
- 1 tomato
- 1 onion
- 1 tsp jeera
- Salt to taste


<img width="915" height="746" alt="image" src="https://github.com/user-attachments/assets/bfed54f2-f28a-4cec-a4c1-7e3755080896" />


  
*Instructions*
1. Wash and boil lentils until soft.
2. Sauté onion and tomato.
3. Add jeera and seasoning.
4. Combine with lentils.
5. Simmer for 5 minutes.
6. Serve hot with rice or roti.

## 📊 Results
- Successfully generates coherent, structured recipes across multiple cuisines and dietary constraints
- Consistent output format achieved through prompt engineering (title, ingredients, steps, time) without additional post-processing logic
- Lightweight, fast, single-page app suitable for quick local deployment

## 🔮 Future Enhancements
- [ ] Nutrition & calorie breakdown per recipe
- [ ] PDF export of generated recipes
- [ ] Recipe history storage (per user session or database)
- [ ] Multiple recipe suggestions per query
- [ ] Ingredient-frequency / cuisine-preference analytics dashboard
- [ ] Cloud deployment (Streamlit Community Cloud / Render)
- [ ] User authentication for saved recipe collections

## 👨‍💻 Author & Contact
**Sahajahanur Rahman**
- 📧 Email: connectingsrl@gmail.com
- 💻 GitHub: [Sahajahanur](https://github.com/Sahajahanur)

---
⭐ If you found this project useful, consider giving the repository a star!
