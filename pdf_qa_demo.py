import streamlit as st
import os
import openai
from lyzr import QABot

# Set up your OpenAI API key (ensure to keep it secure in production)
openai.api_key = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = openai.api_key

def process_pdf(file, query):
    """Process the uploaded PDF and return the response for the query."""
    if file is not None and query is not None:
        with st.spinner('Processing...'):
            # Save the uploaded file
            with open(file.name, "wb") as f:
                f.write(file.getbuffer())

            # Initialize QABot
            qa_bot = QABot.pdf_qa(input_files=[file.name])
            response = qa_bot.query(query)
            return response.response

# Streamlit page configuration
st.set_page_config(page_title='PDF QA Bot', layout='wide')

# App title
st.title('PDF Query Bot')

# File upload widget
uploaded_file = st.file_uploader("Upload a PDF", type=['pdf'])

# Query text input
query = st.text_input("Enter your query")

# Submit button
if st.button('Submit'):
    if uploaded_file is not None and query != "":
        result = process_pdf(uploaded_file, query)
        st.write(result)
    else:
        st.warning("Please upload a PDF file and enter a query.")
