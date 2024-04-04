import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Generate response function from LLAMA2
def getLLamaResponse(input_text, no_words, blog_style):
    # For giving the info which model is used
    llm = CTransformers(model = "model/llama-2-7b-chat.ggmlv3.q8_0.bin", model_type = "llama",
    config = {'max_new_tokens': 256, 'temperature': 0.01})

    # Prompt Template
    template = """
        Write a Blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """
    prompt = PromptTemplate(input_variables = ["blog_style", "input_text", "no_words"], template = template)

    # Generate response
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words = no_words))
    print(response)
    return response

# UI of the project using Streamlit
st.set_page_config(
    page_title = 'Generate_Blogs',
    layout= 'centered',
    initial_sidebar_state = 'collapsed'
)

st.header("Blog Generation")

input_text = st.text_input("Enter the topic for Blog")

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words...")

with col2:
    blog_style = st.selectbox("Writing the blog for...", ('Researchers', "Data-Scientist", "Common"), index = 0)

submit = st.button("Generate")


if submit:
    st.write(getLLamaResponse(input_text, no_words, blog_style))