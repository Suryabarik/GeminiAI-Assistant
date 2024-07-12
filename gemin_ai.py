from dotenv import load_dotenv
load_dotenv()##loading all the enviroment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemin pro model to get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(questions):
   response = model.generate_content(questions)
   return response.text

## inheritize our streamlit app

st.set_page_config(page_title="Q&A DEMO")

st.header("Gemini LLM Application")

input = st.text_input("Input:",key="input")
submit = st.button("Ask me a Question")

##when submit is clicked

if submit:
   response = get_gemini_response(input)
   st.subheader("The Response is")
   st.write(response)


