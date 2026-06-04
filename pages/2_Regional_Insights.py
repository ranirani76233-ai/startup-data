import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("🌎 Regional Insights")

region_count = (
    df.groupby("Region")
    .size()
    .reset_index(name="Count")
)

fig = px.pie(
    region_count,
    names="Region",
    values="Count",
    hole=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)
