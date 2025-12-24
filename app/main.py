import streamlit as st
from app.ui.intake_page import render_intake
from app.services.market_data import get_daily_movers
from app.ui.components import render_movers, render_etfs
from app.services.etf_service import get_top_etfs_by_domain
from app.agents.etf_explainer_agent import explain_etf

from app.agents.etf_personalized_agent import explain_etf_for_user


st.set_page_config(
    page_title="AI Investment Agent",
    layout="wide"
)

st.title("🤖 AI Investment Agent")

# User Intake
preferences = render_intake()

if not preferences:
    st.info("👆 Set your preferences and click **Analyze & Recommend** to continue.")
    st.stop()


st.divider()

#  Market Data
st.subheader("📈 Daily Market Movers")

movers = get_daily_movers()
if movers:
    render_movers(movers)
else:
    st.info("Market data unavailable (market closed or data delay).")

st.divider()

# ETFs (Always visible)
if preferences["focus"] in ["ETFs", "Both"]:

    st.divider()
    st.subheader("🧺 Top ETFs Picked for You")

    with st.spinner("Analyzing ETFs based on your profile..."):
        etf_domains = get_top_etfs_by_domain()

    shown = 0
    MAX_ETFS = 3

    for domain, df in etf_domains.items():
        if shown >= MAX_ETFS:
            break

        # Simple Phase-1 filtering logic
        if preferences["risk"] == "Low":
            df = df[df["cagr"] < 12]
        elif preferences["risk"] == "Medium":
            df = df[df["cagr"] >= 12 & (df["cagr"] < 20)]
        elif preferences["risk"] == "High":
            df = df[df["cagr"] >= 20]

        for _, row in df.head(1).iterrows():
            if shown >= MAX_ETFS:
                break

            st.markdown(f"### 📌 {row['symbol']} ({domain})")
            st.caption(f"📈 {row['cagr']}% 1Y CAGR")

            with st.spinner("Explaining ETF..."):
                st.write(explain_etf(row["symbol"]))

            with st.spinner("Personalizing for you..."):
                reasoning = explain_etf_for_user(row["symbol"], preferences)
                st.info(reasoning)

            shown += 1
