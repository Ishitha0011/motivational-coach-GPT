import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Motivational Coach GPT 💪")

user_input = st.text_input("What’s on your mind?")

if st.button("Motivate Me"):
    if user_input:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a motivational coach who gives uplifting, wise advice to people struggling with stress, failure or low energy."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response.choices[0].message['content'])
