import yfinance as yf
import pandas as pd
import streamlit as st
from pandas_market_calendars import get_calendar
import yaml

@st.cache_data(ttl=86400)
def get_daily_movers():
    # Market calendar check
    nyse = get_calendar("NYSE")
    today = pd.Timestamp.now(tz="US/Eastern").date()

    valid_days = nyse.valid_days(start_date=today, end_date=today)
    if valid_days.empty:
        return {}

    # Load stock universe (Phase 1 safe)
    with open("data/universe.yaml") as f:
        symbols = yaml.safe_load(f)

    rows = []

    for symbol in symbols:
        try:
            t = yf.Ticker(symbol)
            info = t.info

            if "marketCap" not in info:
                print(f"Skipping {symbol} due to missing market cap")
                continue

            hist = t.history(period="2d")
            if len(hist) < 2:
                continue

            pct = (
                (hist["Close"].iloc[-1] - hist["Close"].iloc[-2])
                / hist["Close"].iloc[-2]
            ) * 100

            rows.append({
                "symbol": symbol,
                "pct_change": round(pct, 2),
                "market_cap": info["marketCap"]
            })

        except Exception:
            continue  # fail-safe

    df = pd.DataFrame(rows)
    if df.empty:
        return {}

    # Market cap segmentation
    large = df[df.market_cap > 10e9]
    mid = df[(df.market_cap > 2e9) & (df.market_cap <= 10e9)]
    small = df[df.market_cap <= 2e9]

    return {
        "large": large.sort_values("pct_change", ascending=False),
        "mid": mid.sort_values("pct_change", ascending=False),
        "small": small.sort_values("pct_change", ascending=False),
    }
