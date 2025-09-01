import streamlit as st
from app.chatbot import chat

# Page config
st.set_page_config(page_title="Smart Librarian", page_icon="📚")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #e6f9f0, #c2f0c2);
    }
    .main {
        background: transparent;
        padding: 2rem;
    }
    h1, h2, h3 {
        color: #2e7d32;
        font-family: 'Segoe UI', sans-serif;
    }
    div[data-testid="stTextInput"] label {
        font-weight: bold;
        color: #2e7d32;
    }
    .stButton>button {
        background-color: #66bb6a;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #388e3c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("📚 Smart Librarian")
st.subheader("Get book recommendations based on your interests")

# Set up session state to store the last response
if "last_response" not in st.session_state:
    st.session_state.last_response = ""

# Input text box
user_input = st.text_input("What are you interested in?", placeholder="e.g., magic and adventure")

# Get Recommendation button
if st.button("Get Recommendation") and user_input.strip():
    with st.spinner("Thinking..."):
        response = chat(user_input)
        st.session_state.last_response = response

# Display the chatbot response if available
if st.session_state.last_response:
    st.markdown("### 🤖 Recommendation")
    st.write(st.session_state.last_response)
