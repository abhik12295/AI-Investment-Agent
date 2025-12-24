from transformers import pipeline
import streamlit as st
from llm.client import load_llm

@st.cache_data(ttl=86400)
def explain_etf(symbol: str):
    llm = load_llm()

    prompt = (
        f"Explain the ETF {symbol} in simple terms. "
        "Include what it tracks, who it is suitable for, "
        "and the risk level. Keep it concise."
        "Keep concise, 3-5 sentences."
    )

    result = llm(prompt, max_new_tokens=150)
    return result[0]["generated_text"]
