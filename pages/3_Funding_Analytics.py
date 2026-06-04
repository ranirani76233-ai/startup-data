import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("💰 Funding Analytics")

fig = px.box(
    df,
    x="Industry",
    y="Funding Amount (M USD)",
    color="Industry"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

corr = df.select_dtypes(
    include="number"
).corr()

fig2 = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
