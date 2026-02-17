# AI Study Assistant 🤖

**A text-based AI study helper** – ask questions, upload PDFs, and get answers using Google's Gemini AI.  
Built with Python, Streamlit, and a touch of curiosity.

## ✨ Features
- **Ask Anything** – Type any question, get a clear answer from Gemini 1.5 Flash.
- **PDF Q&A** – Upload a PDF and ask questions about its content (text extraction only – works best with digital PDFs).
- **Simple & Clean UI** – Two tabs for easy navigation.
- **100% Text-Based** – This project focuses on text interactions (no images/voice).

## 🛠️ Tech Stack
- Python 3.13
- Streamlit – for the web app
- Google Generative AI (Gemini) – for answers
- PyPDF2 – for reading PDF text

## 🚀 How to Run Locally
1. Clone the repo:  
   `git clone https://github.com/ManthanS2003/ai-study-assistant.git`
2. Create a virtual environment (optional):  
   `python -m venv venv` and activate it.
3. Install dependencies:  
   `pip install -r requirements.txt`
4. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
5. Create a `.env` file in the project folder with:  
   `GEMINI_API_KEY=your_key_here`
6. Run the app:  
   `streamlit run app.py`

## ☁️ Live Demo
You can try the live version here: https://ai-study-assistant-nzzewjhkkaebv4ffnzrcdx.streamlit.app/

## 🔒 Security Note
The `.env` file containing your API key is **not** committed to GitHub (it's in `.gitignore`). When deploying to Streamlit Cloud or Render, add the key as a secret/environment variable.

## 📝 License
MIT
