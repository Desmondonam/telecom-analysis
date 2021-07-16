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
print(df.head())

st.sidebar.checkbox("Show Analysis by handset", True, key=1)
select = st.sidebar.selectbox('Select a State',df['handset_manufacturer'])

#get the state selected in the selectbox
state_data = df[df['handset_manufacturer'] == select]
select_status = st.sidebar.radio("Covid-19 patient's status", ('Confirmed',
'Active', 'Recovered', 'Deceased'))