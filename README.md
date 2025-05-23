# 🧠 DeepSeek AI Chatbot 🤖

An open-source Streamlit chatbot powered by [DeepSeek-V3](https://together.ai/models/deepseek-ai/DeepSeek-V3) via the Together API.  
This project features conversational memory, clean UI, and serves as a launchpad for building full-stack AI agents with tool use, voice, and vector search.

---

## 🚀 Features
- ✨ Powered by DeepSeek-V3 (Together API)
- 💬 Conversational memory with `st.session_state`
- 🌐 Simple, elegant Streamlit interface
- 🔐 API key managed via `.env` (never hard-coded)
- 🛠️ Clean modular structure for easy scaling

---

## 📁 Project Structure
```
deepseek-chatbot/
├── app/
│   └── main.py          # Core chatbot app
├── .env                 # Environment variables (API keys)
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignore sensitive or temp files
├── run.sh               # One-click launcher
└── README.md            # You are here
```

---

## 🧪 Quickstart

1. **Clone the repo**
```bash
git clone https://github.com/yashhooda1/deepseek-chatbot.git
cd deepseek-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set your Together API key in `.env`**
```
TOGETHER_API_KEY=your_actual_api_key_here
```

4. **Run the app**
```bash
./run.sh
```

Open `http://localhost:8501` in your browser to chat!

---

## 🧰 Built With
- [Streamlit](https://streamlit.io)
- [Together AI](https://together.ai)
- [DeepSeek-V3 Model](https://huggingface.co/deepseek-ai/DeepSeek-V3)

---

## 🧩 Coming Soon
- 🗣️ Whisper-powered voice input + TTS
- 🧠 Vector DB memory (Chroma or FAISS)
- 🛠️ LangChain tool integrations
- 🌍 Hugging Face Spaces / Fly.io deployment

---

## 💡 License
MIT — use it, fork it, build your own version. Credit appreciated!
