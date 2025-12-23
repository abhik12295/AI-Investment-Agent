import streamlit as st
from app.utils.constants import SECTORS
from app.agents.intake_agent import suggest_strategy


def render_intake():
    st.subheader("Investment Preferences")

    horizon = st.selectbox("Holding Period", ["Days", "Weeks", "Months", "1+ Year"])
    risk = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
    sectors = st.multiselect("Preferred Sectors", SECTORS)
    market_caps = st.multiselect("Market Cap Preference", ["Large", "Mid", "Small"])

    suggestion = suggest_strategy(horizon, risk)
    st.info(f"Suggested Strategy: **{suggestion}**")

    return {
        "strategy": suggestion,
        "horizon": horizon,
        "risk": risk,
        "sectors": sectors,
        "market_caps": market_caps
    }
