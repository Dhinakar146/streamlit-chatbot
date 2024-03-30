import streamlit as st
from dotenv import load_dotenv
from scripts.azure_openai import get_response
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()

# app config
st.set_page_config(page_title="Streamlit Chatbot", page_icon="🤖", layout="wide")
st.title("Streamlit Chatbot")

with st.sidebar:
    model = st.selectbox('LLM Model', ['GPT-4'])

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a bot. How can I help you?"),
    ]

# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        if model == 'GPT-4':
            response = st.write_stream(get_response(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=response))
