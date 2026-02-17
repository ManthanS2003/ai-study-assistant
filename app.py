import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Automatically select a valid model
available_models = genai.list_models()
valid_model = None
for m in available_models:
    if 'generateContent' in m.supported_generation_methods:
        valid_model = m.name
        break

if not valid_model:
    st.error("No suitable model found. Check your API key and internet connection.")
    st.stop()

model = genai.GenerativeModel(valid_model)

st.set_page_config(page_title="AI Study Assistant", page_icon="🤖")
st.title("🤖AI Study Assistant")
st.write("Ask any question, or upload a PDF to ask about its content.")

tab1, tab2 = st.tabs(["Ask a Question", "Upload PDF & Ask"])

with tab1:
    user_question = st.text_input("Your question:", placeholder="e.g., Ask Me, Any Type of Question!")
    if st.button("Get Answer", key="ask_btn"):
        if user_question:
            with st.spinner("Thinking..."):
                response = model.generate_content(user_question)
                st.write("### Answer")
                st.write(response.text)
        else:
            st.warning("Please enter a question.")

with tab2:
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        with st.expander("Show extracted text preview"):
            st.write(text[:1000] + "...")
        
        pdf_question = st.text_input("Ask about the PDF:", placeholder="e.g., What is the main topic?")
        if st.button("Get Answer from PDF", key="pdf_btn"):
            if pdf_question:
                prompt = f"Based on the following document, answer the question.\n\nDocument:\n{text}\n\nQuestion: {pdf_question}"
                with st.spinner("Analyzing document..."):
                    response = model.generate_content(prompt)
                    st.write("### Answer")
                    st.write(response.text)
            else:
                st.warning("Please enter a question.")