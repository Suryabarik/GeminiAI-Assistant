from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model to get responses
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input:  # assuming input should be a non-empty string or meaningful value
        response = model.generate_content(input, image)
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")

st.header("Future prediction")

input_prompt = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me the future of the Image")
    if submit and image:
        response = get_gemini_response(input_prompt, image)
        st.subheader("The Response is")
        st.write(response)
