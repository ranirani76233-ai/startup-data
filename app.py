import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide"
)

# Load Data
df = pd.read_csv("data/startup_data.csv")

# Header
st.title("🚀 Startup Analytics Dashboard")
st.markdown("Deep Analytics & Business Intelligence")

# KPI Metrics
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Startups",
    f"{len(df)}"
)

col2.metric(
    "Total Funding",
    f"${df['Funding Amount (M USD)'].sum():,.0f} M"
)

col3.metric(
    "Avg Valuation",
    f"${df['Valuation (M USD)'].mean():,.0f} M"
)

col4.metric(
    "Total Revenue",
    f"${df['Revenue (M USD)'].sum():,.0f} M"
)

profit_rate = (
    df['Profitable'].mean()*100
)

col5.metric(
    "Profitability",
    f"{profit_rate:.1f}%"
)

st.divider()

# Funding vs Valuation

fig = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    color="Industry",
    size="Employees",
    hover_name="Startup Name",
    title="Funding vs Valuation Analysis"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Industry Funding

industry_funding = (
    df.groupby("Industry")
    ["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    industry_funding,
    x="Industry",
    y="Funding Amount (M USD)",
    color="Industry",
    title="Funding by Industry"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
