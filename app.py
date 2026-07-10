import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Streamlit page config
st.set_page_config(
    page_title="AI Recipe Generator",
    page_icon="🍳"
)

st.title("🍳 AI Recipe Generator")
st.write("Generate recipes using Gemini AI based on ingredients, cuisine, and diet preferences.")

# Check API key
if not api_key:
    st.error("GOOGLE_API_KEY not found in .env file")
    st.stop()

# User Inputs
ingredients = st.text_area(
    "Enter Ingredients (comma separated)",
    placeholder="Tomato, Onion, Lentils, Salt, Jeera"
)

cuisine = st.selectbox(
    "Select Cuisine",
    ["Indian", "Italian", "Mexican", "Chinese", "Thai", "Any"]
)

diet = st.selectbox(
    "Select Diet",
    ["Any", "Vegetarian", "Vegan", "Jain", "Keto"]
)

# Generate Recipe Button
if st.button("Generate Recipe"):

    if not ingredients.strip():
        st.warning("Please enter some ingredients.")
    else:

        prompt = f"""
        Generate one recipe using these ingredients:
        {ingredients}

        Cuisine: {cuisine}
        Diet: {diet}

        Requirements:
        - Give recipe name
        - List ingredients
        - Provide step-by-step instructions
        - Mention cooking time
        - Keep response under 250 words
        """

        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.subheader("🍽 Generated Recipe")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")