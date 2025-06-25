from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
import fitz
from PIL import Image 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, resume_text, input_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_prompt, resume_text, input_text])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("PaperWhiz AI")
uploaded_file=st.file_uploader("Upload your research paper",type=["pdf"])
input_text=st.text_area("Ask your questions ",key="input")



if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Summarize the PDF")

submit2 = st.button("Answer my questions")

input_prompt1 = """
You are an expert academic assistant.

Your task is to:
1. Read and analyze the uploaded academic paper or research article.
2. Generate a concise and simplified summary that captures the key objectives, methodology, and findings of the paper.
3. Explain the core concepts and technical terms in simple language so that even non-experts can understand.
4. Keep the tone clear, objective, and informative.

Avoid jargon unless it's explained. The summary should help a student or professional quickly grasp what the paper is about.
"""

input_prompt2 = """
You are an academic research expert.

You will be given a research paper and a specific question from the user.
Based on the content of the paper, provide an accurate, concise, and well-explained answer to the user's question.
If the answer is not explicitly in the paper, make an educated guess based on its content, but clearly state that.

Use professional tone, and refer to paper sections or findings where appropriate.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("Summary")
        st.write(response)
    else:
        st.write("Please upload the research paper")

elif submit2:
    if uploaded_file is not None:
        if input_text.strip() != "":
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
            st.subheader("Answers")
            st.write(response)
        else:
            st.warning("Please enter a question before submitting.")
    else:
        st.write("Please upload the research paper")