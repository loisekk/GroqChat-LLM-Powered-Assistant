import streamlit as st
from groq import Groq


st.set_page_config(
    page_title="GroqQnA",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 GroqQnA")
st.caption("LLM-Powered Chatbot using Streamlit & Groq")


if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ GROQ_API_KEY not found. Add it to Streamlit secrets.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])



if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Ask anything...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Groq API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=st.session_state.messages
            )

            answer = response.choices[0].message.content
            st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
