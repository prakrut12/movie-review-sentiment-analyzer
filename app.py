import streamlit as st
from google import genai  # Official Gemini SDK

# 🔑 Directly put your API key here
API_KEY = "AIzaSyC8yn2Zrbd9r60N7ut6hB6orPT13yn9jM4"

# Initialize client
client = genai.Client(api_key=API_KEY)

st.title("🎬 Movie Review Sentiment Analyzer (Gemini)")
st.write("Enter a movie review and let Gemini analyze its sentiment!")

# Input box
user_input = st.text_area("Movie Review", "I absolutely loved the movie! Brilliant performance.")

if st.button("Analyze Sentiment"):
    try:
        # Ask Gemini to analyze sentiment
        prompt = f"""
        Analyze the sentiment of this movie review:
        "{user_input}"
        
        Return the result in JSON with these keys:
        - sentiment: Positive, Negative, or Neutral
        - confidence: a number between 0 and 1
        - explanation: short explanation of why
        - key_phrases: list of important words/phrases
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        st.subheader("📊 Sentiment Analysis Result")
        st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")
