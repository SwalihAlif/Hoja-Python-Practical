import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Get the API key from environment
api_key = os.getenv("GCP_API_KEY")

# Initialize client with secure key
client = genai.Client(api_key=api_key)

st.title("Swalih's Utility Toolkit")

task = st.selectbox(
    "Choose a task",
    [
        "Professional Email Writer",
        "Resume Analyzer",
        "Grammar Corrector"
    ]
)

user_input = st.text_area("Enter your content")

if st.button("Generate"):
    prompt = f"""
    You are an AI assistant.

    Task: {task}

    User input:
    {user_input}

    Give a clear and useful response.
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    st.write(response.text)