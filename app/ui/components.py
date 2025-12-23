import streamlit as st

def render_movers(movers):
    for cap, df in movers.items():
        st.markdown(f"### {cap.capitalize()} Cap")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Top Gainers**")
            st.dataframe(df.head(5)[["symbol", "pct_change"]])

        with col2:
            st.markdown("**Top Losers**")
            st.dataframe(df.tail(5)[["symbol", "pct_change"]])

def render_etfs(df):
    st.dataframe(df)
