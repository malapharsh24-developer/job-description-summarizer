import os
from dotenv import load_dotenv

import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Job Description Summarizer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Job Description Summarizer")
st.write("Paste a Job Description below and generate a concise summary.")

# ------------------------------
# Load Environment Variables
# ------------------------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in .env file.")
    st.stop()

# ------------------------------
# Prompt Template
# ------------------------------
summary_template = """
You are an expert HR assistant.

Summarize the following Job Description in 60-100 words.

Focus on:
- Role and purpose
- Key responsibilities
- Required skills and technologies
- Experience required
- Location (if available)

Keep the summary concise, professional, and based only on the provided information.

Do not use bullet points.

Job Description:
{info}

Summary:
"""

prompt = PromptTemplate(
    input_variables=["info"],
    template=summary_template
)

# ------------------------------
# LLM
# ------------------------------
llm = init_chat_model(
    "google_genai:gemini-3.5-flash-lite",
    api_key=GOOGLE_API_KEY
)

chain = prompt | llm

# ------------------------------
# User Input
# ------------------------------
job_description = st.text_area(
    "Paste Job Description",
    height=350,
    placeholder="Paste the complete job description here..."
)

# ------------------------------
# Summarize Button
# ------------------------------
if st.button("🚀 Generate Summary", use_container_width=True):

    if not job_description.strip():
        st.warning("Please enter a Job Description.")
    else:
        with st.spinner("Generating summary..."):

            response = chain.invoke(
                {"info": job_description}
            )

        st.success("Summary Generated!")

        st.subheader("Summary")

        st.text_area(
        label="",
        value=response.text,
        height=200,
        disabled=True)