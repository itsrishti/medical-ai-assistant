import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit UI
st.set_page_config(page_title="Medical AI Assistant", layout="centered")
st.title("🧠 Medical AI Assistant")
st.markdown("Upload a medical image (e.g., an X-ray, MRI, or scan) and get instant AI-generated diagnostic insights.")

# Image uploader
uploaded_file = st.file_uploader("📷 Upload a Medical Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='🩻 Uploaded Image', use_column_width=True)

    # Ask for user prompt
    user_prompt = st.text_input("🔍 What do you want the AI to analyze or answer about this image?", value="What are the signs of disease in this image?")

    if st.button("🧠 Analyze Image"):
        with st.spinner("Analyzing image and generating insights..."):
            try:
                response = model.generate_content([
                    user_prompt,
                    image
                ])
                st.success("✅ Diagnosis Completed")
                st.markdown("### 📝 AI Diagnostic Report:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")
