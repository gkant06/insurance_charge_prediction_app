# import module
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Title
st.title("Demographic information of insurance buyers")

# Loading the dataset

df = pd.read_csv('insurance.csv')

df_summary = df.describe()
df_summary = df_summary[['age','bmi','children','charges']].iloc[5]
df_summary

# Histogram for age

data = df.age
bins = len(set(data))
fig = px.histogram(data, nbins=bins)
# Customize the layout
fig.update_layout(
    title="Age distribution",
    xaxis_title="Age",
    yaxis_title="Frequency",
    font=dict(size=12),
    width = 300,
    height = 300,
    showlegend = False
)

# Show the figure in Streamlit
st.plotly_chart(fig)

# Histogram for age

data = df.children
bins = len(set(data))
fig = px.histogram(data, nbins=bins)
# Customize the layout
fig.update_layout(
    title="No. of children distribution",
    xaxis_title="No. of children",
    yaxis_title="Frequency",
    font=dict(size=12),
    width = 300,
    height = 300,
    bargap = 0.2,
    showlegend = False
)

# Show the figure in Streamlit
st.plotly_chart(fig)

# Histogram for region

data = df.region
bins = len(set(data))
fig = px.histogram(data, nbins=bins)
# Customize the layout
fig.update_layout(
    title="Distribution by region",
    xaxis_title="Region No.",
    yaxis_title="Frequency",
    font=dict(size=12),
    width = 300,
    height = 300,
    bargap = 0.2,
    showlegend = False
)

# Show the figure in Streamlit
st.plotly_chart(fig)