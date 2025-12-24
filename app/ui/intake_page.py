import streamlit as st
from app.utils.constants import SECTORS
from app.agents.intake_agent import suggest_strategy


# def render_intake():
#     st.subheader("Investment Preferences")

#     horizon = st.selectbox("Holding Period", ["Days", "Weeks", "Months", "1+ Year"])
#     risk = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
#     sectors = st.multiselect("Preferred Sectors", SECTORS)
#     market_caps = st.multiselect("Market Cap Preference", ["Large", "Mid", "Small"])

#     suggestion = suggest_strategy(horizon, risk)
#     st.info(f"Suggested Strategy: **{suggestion}**")

#     return {
#         "strategy": suggestion,
#         "horizon": horizon,
#         "risk": risk,
#         "sectors": sectors,
#         "market_caps": market_caps
#     }

def render_intake():
    st.subheader("Investment Preferences")

    with st.form("investment_intake_form"):
        focus = st.radio(
            "What do you want to focus on?",
            ["Stocks", "ETFs", "Both"],
            horizontal=True
        )

        horizon = st.selectbox("Holding Period", ["Days", "Weeks", "Months", "1+ Year"])
        risk = st.radio("Risk Tolerance", ["Low", "Medium", "High"])
        sectors = st.multiselect("Preferred Sectors", SECTORS)
        market_caps = st.multiselect("Market Cap Preference", ["Large", "Mid", "Small"])

        submit = st.form_submit_button("🚀 Analyze & Recommend")

    if not submit:
        return None

    suggestion = suggest_strategy(horizon, risk)
    st.success(f"Suggested Strategy: **{suggestion}**")

    return {
        "focus": focus,
        "strategy": suggestion,
        "horizon": horizon,
        "risk": risk,
        "sectors": sectors,
        "market_caps": market_caps,
        "submitted": True
    }
