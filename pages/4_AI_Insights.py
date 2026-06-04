import streamlit as st
import pandas as pd

df = pd.read_csv("data/startup_data.csv")

st.title("🤖 AI Business Insights")

best_industry = (
    df.groupby("Industry")
    ["Valuation (M USD)"]
    .mean()
    .idxmax()
)

best_region = (
    df.groupby("Region")
    ["Funding Amount (M USD)"]
    .sum()
    .idxmax()
)

highest_revenue = (
    df.loc[
        df["Revenue (M USD)"].idxmax(),
        "Startup Name"
    ]
)

st.success(
    f"🏆 Highest Valuation Industry: {best_industry}"
)

st.info(
    f"🌍 Most Funded Region: {best_region}"
)

st.warning(
    f"💰 Highest Revenue Startup: {highest_revenue}"
)
