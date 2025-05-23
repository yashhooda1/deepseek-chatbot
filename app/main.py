from together import Together
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="DeepSeek Chatbot", layout="centered")
st.title("🤖 DeepSeek AI Chatbot")
st.markdown("Powered by deepseek-ai/DeepSeek-V3 on Together.ai")

user_input = st.text_input("You:", "", key="user_input")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=st.session_state.chat_history
    )
    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

if st.session_state.chat_history:
    for chat in st.session_state.chat_history:
        speaker = "You" if chat["role"] == "user" else "Bot"
        st.markdown(f"**{speaker}:** {chat['content']}")