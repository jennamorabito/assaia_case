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
st.title('Turnaround Check-up')
st.subheader('Flight level')

# Departures and arrivals, airport data
tab1, tab2 = st.tabs(['Departures', 'Arrivals']) 
with tab1:
    departures = df[df['D Departure Or Arrival'] == 'departure']
    total_departures = len(departures.index)

    kpid1, kpid2, kpid3 = st.columns(3)

    returned = df[df["D Returned To Gate"] == True].shape[0]
    kpid1.metric(
        label='Returned to gate',
        value=f'{returned}',
    )
    
    kpid2.metric(
        label='Cancelled departures',
        value=departures[departures['D Flight Status'] == 'X'].shape[0],
    )   

    kpid3.metric(
        label='Late departures',
        value=departures[departures['D Scheduled Date Time'] < departures['D Actual Off Block Time']].shape[0],
    ) 
 
with tab2:
    arrivals = df[df['A Departure Or Arrival'] == 'arrival']
    
    kpia1, kpia2, kpia3 = st.columns(3)

    kpia2.metric(
        label='Late arrivals',
        value=arrivals[arrivals['A Scheduled Date Time'] < arrivals['A Actual In Block Time']].shape[0],
    )

# Assaia's data

st.subheader('Subprocesses level')
st.write('Safety')

# KPIs
# create three columns
# kpi1, kpi2, kpi3 = st.columns(3)

# # kpi 1: humans without a vest
# no_vest = df[df['Human Without Vest Start Ts'].notnull()]

# kpi1.metric(
#     label='People without vests',
#     value=no_vest.shape[0],
# )

st.title('KPI Grid Example')

# num_columns = 3

# for i, (kpi_name, kpi_value) in enumerate(kpi_dataset.items(), start=1):
#     col_idx = (i - 1) % num_columns
#     st.metric(label=kpi_name, value=kpi_value, delta=None)

kpi_dataset = pd.read_csv('data/sub_processes_delta.csv')
st.dataframe(kpi_dataset)

st.write('Interesting finding: No correlation was found between a departing plane returning to the gate and any flight-readiness subprocesses, but for between fueling, catering, and cargo, fueling had the strongest correlation')