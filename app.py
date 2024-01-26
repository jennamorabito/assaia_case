import streamlit as st
import pandas as pd
# pip install plotly?

# PAGE SETUP
st.set_page_config(
    page_title='Assaia Case Study',
    page_icon='static/iris-logo.svg',
    layout='wide', # can change to 'centered'
)

# READ INPUT DATA
dataset_url = 'data/case_data.csv'

@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, sep=';')

df = get_data()
row_count = len(df.index)

# TITLE
st.title('Flight Readiness Check-up')
st.subheader('What\'s going well, and where to improve')

# KPIs
# create three columns
kpi1, kpi2, kpi3 = st.columns(3)

# kpi 1: humans without a vest
no_vest = df[df['Human Without Vest Start Ts'].notnull()]

kpi1.metric(
    label='People without vests',
    value=no_vest.shape[0],
)

# kpi 2: returned plants
d_returns = df[df['D Returned To Gate'] == True]

kpi2.metric(
    label='Returned departures',
    value=d_returns.shape[0],
)

# kpi 2: returned plants
d_returns = df[df['D Returned To Gate'] == True]

kpi3.metric(
    label='Returned departures',
    value=d_returns.shape[0],
)