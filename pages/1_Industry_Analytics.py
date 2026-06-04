import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("🏭 Industry Analytics")

industry_stats = (
    df.groupby("Industry")
    .agg({
        "Funding Amount (M USD)":"sum",
        "Valuation (M USD)":"mean",
        "Revenue (M USD)":"mean"
    })
    .reset_index()
)

fig = px.treemap(
    industry_stats,
    path=["Industry"],
    values="Funding Amount (M USD)",
    color="Revenue (M USD)"
)

st.plotly_chart(fig,
                use_container_width=True)
