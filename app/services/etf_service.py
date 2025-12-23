import yfinance as yf
import pandas as pd
import streamlit as st
from app.services.etf_domains import ETF_DOMAINS

@st.cache_data(ttl=86400)
def get_top_etfs_by_domain():
    domain_results = {}

    for domain, symbols in ETF_DOMAINS.items():
        rows = []

        for symbol in symbols:
            try:
                t = yf.Ticker(symbol)
                hist = t.history(period="1y")

                if hist.empty or len(hist) < 2:
                    continue

                cagr = (hist["Close"].iloc[-1] / hist["Close"].iloc[0]) - 1

                rows.append({
                    "symbol": symbol,
                    "cagr": round(cagr * 100, 2)
                })

            except Exception:
                continue

        df = pd.DataFrame(rows)
        if not df.empty:
            domain_results[domain] = (
                df.sort_values("cagr", ascending=False)
                .head(5)
            )

    return domain_results
