<div align="center">

# 🤖 Groq QnA ChatBot

**A fast, LLM-powered question-answering chatbot built with Groq API and Streamlit.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-LLM_API-orange?style=for-the-badge)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Yash%20Brahmankar-green?style=for-the-badge)](https://github.com/loisekk)

> *"Ask anything. Get instant answers powered by Groq AI."* ⚡🤖

</div>

---

## 📌 Overview

**Groq QnA ChatBot** is an AI-powered conversational interface built on top of Groq's ultra-fast LLM inference API, rendered through a clean Streamlit chat UI.

Users type natural language questions and receive instant, intelligent responses — no setup friction, no latency bottleneck. This project demonstrates end-to-end LLM integration: API communication, secure key handling, session state management, and web deployment.

---

## 🎥 Demo

<div align="center">
  <img src="assets/demo.gif" width="700" alt="Groq QnA ChatBot Demo"/>
  <br/>
  <sub>Live chat — question input, Groq API response, real-time rendering</sub>
</div>

---

## ✨ Features

| Feature | Details |
|---|---|
| 💬 Chat UI | Message-style interface via Streamlit `st.chat_message` |
| ⚡ Ultra-Fast Inference | Groq hardware delivers sub-second LLM responses |
| 🧠 LLM Backend | `openai/gpt-oss-20b` via Groq Python SDK |
| 🔐 Secure Key Handling | API key loaded from environment variables, never hardcoded |
| 🔄 Session Memory | Conversation history preserved via `st.session_state` |
| 🌐 Web Deployment | Runs locally or deployable on Streamlit Cloud |

---

## ⚙️ How It Works

```
User types question
        ↓
Query sent to Groq API (openai/gpt-oss-20b)
        ↓
LLM processes input → streams response
        ↓
Answer rendered in chat UI
        ↓
Conversation history updated in session state
```

---

## 🛠 Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| Language | Python 3.x | Core application logic |
| LLM API | Groq SDK | Ultra-fast inference backend |
| Model | `openai/gpt-oss-20b` | Language model for QnA |
| Web UI | Streamlit | Chat interface + deployment |
| Config | `os.environ` / `.env` | Secure API key management |

---

## 🚀 Getting Started

**Clone the repo:**

```bash
git clone https://github.com/loisekk/Groq-QnA-ChatBot.git
cd Groq-QnA-ChatBot
```

**Install dependencies:**

```bash
pip install streamlit groq python-dotenv
```

**Set API key:**

```bash
# macOS / Linux
export GROQ_API_KEY="your_api_key_here"

# Windows
setx GROQ_API_KEY "your_api_key_here"
```

> Get your free API key at [console.groq.com](https://console.groq.com)

**Run the app:**

```bash
streamlit run app.py
```

App opens at `http://localhost:8501`.

---

## 📂 Project Structure

```
Groq-QnA-ChatBot/
├── app.py               # Main Streamlit app — UI, session state, API calls
├── .env                 # API key (never commit this)
├── .gitignore           # Excludes .env from version control
├── requirements.txt     # Project dependencies
├── assets/
│   └── demo.gif         # App demo
└── README.md
```

---

## ⚠️ Security Notes

- Never hardcode `GROQ_API_KEY` in source code
- Add `.env` to `.gitignore` before first commit
- Rotate key immediately if accidentally pushed to GitHub

---

## 🎯 Use Cases

- Learning end-to-end LLM API integration
- Hackathon AI chatbot prototype
- Personal AI assistant base
- Portfolio demonstration of Groq + Streamlit stack
- Foundation for RAG or multi-turn chat apps

---



## 👨‍💻 Author

**Yash Brahmankar**
B.Tech AI & ML | OIST, 2024–2028

[![GitHub](https://img.shields.io/badge/GitHub-loisekk-181717?style=flat-square&logo=github)](https://github.com/loisekk)
[![Email](https://img.shields.io/badge/Email-yashbrahmankar95@gmail.com-D14836?style=flat-square&logo=gmail)](mailto:yashbrahmankar95@gmail.com)

---

## 📄 License

Licensed under the [MIT License](LICENSE) — free to use, modify, and distribute.

---

<div align="center">
  <sub>Built with Python · Powered by Groq · Deployed on Streamlit</sub>
</div>
