from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"]=""
# Function for loading the OpenAI model & get the responses
def get_openai_response(query):
    # Initializing OpenAI with the API key
    llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model_name="GPT-3.5 Turbo", temperature=0.6)
    # Getting response
    response = llm(query)
    return response

# Initializing streamlit app
st.set_page_config(page_title="Q&A Chat")
st.header("Simple Q & A Chat-bot")

input_text = st.text_input("Input: ")

if st.button("Ask the question"):
    response = get_openai_response(input_text)
    st.subheader("The response is:")
    st.write(response)