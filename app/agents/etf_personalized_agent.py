'''
Docstring for app.agents.etf_personalized_agent
- takes etf symbol
- takes intake input
- generates personalized ETF recommendation based on the intake input
'''


from app.agents.etf_explainer_agent import explain_etf
from llm.client import load_llm
import streamlit as st

@st.cache_data(ttl=86400)
def explain_etf_for_user(symbol: str, profile: dict) -> str:
    # base_explanation = explain_etf(symbol)
    llm = load_llm()
    prompt = f"""
            You are a financial advisor. 
            User has provided their financial profile: {profile}.
            - Holding Period: {profile['horizon']}
            - Risk tolerance: {profile['risk']}
            - Preferred sector: {', '.join(profile['sectors']) or 'Any'}
            - Market cap preference: {', '.join(profile['market_caps']) or 'Any'}
            ETF is {symbol}
            Explain WHY this ETF is suitable for this user.
            Be concise, practical, and honest.
            Limit to 2-3 sentences.
            """
    response = llm(prompt, max_new_tokens=150)
    return response[0]["generated_text"]


