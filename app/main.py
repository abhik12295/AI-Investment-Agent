import streamlit as st

from app.ui.intake_page import render_intake
from app.services.market_data import get_daily_movers
from app.services.etf_service import get_top_etfs_by_domain
from app.agents.etf_explainer_agent import explain_etf
from app.ui.components import render_movers

st.set_page_config(
    page_title="AI Investment Agent",
    layout="wide"
)

st.title("🤖 AI Investment Agent")

# 1️⃣ User Intake
preferences = render_intake()

st.divider()

# 2️⃣ Market Data
st.subheader("📈 Daily Market Movers")

movers = get_daily_movers()
if movers:
    render_movers(movers)
else:
    st.info("Market data unavailable (market closed or data delay).")

st.divider()

# 3️⃣ ETFs (Always visible)
st.subheader("🧺 Top ETFs by Domain (1Y CAGR)")

with st.spinner("Analyzing ETFs across domains..."):
    etf_domains = get_top_etfs_by_domain()

for domain, df in etf_domains.items():
    with st.expander(f"📌 {domain} ETFs"):
        for _, row in df.iterrows():
            st.markdown(f"### {row['symbol']} — {row['cagr']}% CAGR")

            with st.spinner("Generating AI explanation..."):
                explanation = explain_etf(row["symbol"])

            st.write(explanation)