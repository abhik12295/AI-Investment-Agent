from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_llm():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-large",
        max_length=256
    )
