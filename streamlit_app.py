import streamlit as st
from dotenv import load_dotenv
from scripts.azure_openai import send_message

load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Streamlit Chatbot", page_icon=":robot:", layout="wide"
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state["messages"] = []


# Define function to display chat messages
def display_messages():
    for message in st.session_state.messages:
        st.chat_message(message[0]).write(message[1])


st.markdown("## Streamlit Chatbot Powered By GPT-4")
if user_question := st.chat_input("Message Chatbot!"):
    display_messages()
    st.chat_message("user").write(user_question)
    with st.spinner("Thinking..."):
        response = send_message(user_question)
        st.session_state.messages.append(["user", user_question])
        st.session_state.messages.append(["assistant", response])
        st.chat_message("assistant").write(response)
