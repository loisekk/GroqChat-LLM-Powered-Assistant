import os
from groq import Groq
import streamlit as st

api_key = os.getenv("GROQ_API_KEY")

llm = Groq(api_key=api_key)

st.subheader("Groq QnA ChatBot 🤖")

query = st.chat_input("Ask anything...")
if query:
    st.chat_message("user").markdown(query)

    response = llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": query}]
    )

    answer = response.choices[0].message.content
    st.chat_message("assistant").markdown(answer)
