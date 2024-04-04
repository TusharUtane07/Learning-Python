import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def generateGeminiResponse(query):
    response = chat.send_message(query, stream=True)
    return response


st.set_page_config(
    page_title = 'Generate_Blogs',
    layout= 'centered',
    initial_sidebar_state = 'collapsed'
)

st.header("Conversational Chatbot powered by GeminiPro")

if 'chat_history' not in st.session_state:
    st.session_state ['chat_history'] = []


input_text = st.text_input("Enter query: ", key="input_text")
button = st.button("Submit")

if input_text and input_text:
    response = generateGeminiResponse(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("Here's your response: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("Chat History: ")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")