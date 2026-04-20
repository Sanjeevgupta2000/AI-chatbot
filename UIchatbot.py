import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import os

# ------------------ Page Config ------------------
st.set_page_config(page_title="AI Chat Assistant", page_icon="🤖")

st.title("🤖 AI Chat Assistant")
st.markdown("---")

# ------------------ Sidebar ------------------
with st.sidebar:
    st.header("⚙️ Settings")

    # Mode Selection (THIS WAS MISSING BEFORE)
    mode_option = st.selectbox(
        "🎭 Choose AI Mode",
        ["Funny 😂", "Angry 😡", "Sad 😢"]
    )

    # Clear Chat Button
    if st.button("🗑️ Clear Chat"):
        st.session_state.clear()
        st.rerun()

# ------------------ Mode Logic ------------------
if mode_option == "Angry 😡":
    mode = "You are Angry AI Agent and your response in aggressively ways"
elif mode_option == "Sad 😢":
    mode = "You are Sad AI Agent and your response in sad ways"
else:
    mode = "You are Funny AI agent and your response in funny ways"

# ------------------ API Key ------------------
api_key = os.getenv("enter your api key")

# ------------------ Model ------------------
model = ChatMistralAI(
    model="ministral-8b-2512",
    temperature=0,
    api_key=api_key
)

# ------------------ Session State ------------------
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

# Reset when mode changes
if st.session_state.messages[0].content != mode:
    st.session_state.messages = [SystemMessage(content=mode)]

# ------------------ Chat Display ------------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ------------------ Input ------------------
user_input = st.chat_input("Type your message (0 to exit)")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))

    if user_input == "0":
        st.warning("Application stopped")
    else:
        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    st.rerun()

# ------------------ Footer ------------------
st.markdown("---")
st.caption("Modes: Angry 😡 | Sad 😢 | Funny 😂")
