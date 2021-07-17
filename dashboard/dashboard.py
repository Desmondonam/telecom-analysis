import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.set_page_config(page_title="Dashboard Telecommunication", layout="wide")


df = pd.read_csv('C:/Users/DESMOND/telecom-analysis/data/cleaned_data.csv')

st.title("Dashboard for Telecommunication Analysis")
st.markdown('The dashboard will visualize the Telecommunication situation for improvement')
st.markdown('')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")


#Bar Chart
st.bar_chart(df['youtube'])

