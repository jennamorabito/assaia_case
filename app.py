import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
st.title('Turnaround Check-up ✈️')
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

with st.container():
    returns = departures[departures['D Returned To Gate'] == True]
    returns_freq_by_company = returns['D Company Iata'].value_counts()
    
    st.write('Departures returned to gate by airline')
    st.bar_chart(data=returns_freq_by_company)

# Assaia's data
st.subheader('Subprocesses level')

# KPIs
# create three columns
kpi1, kpi2, kpi3 = st.columns(3)

# kpi 1: humans without a vest
no_vest = df[df['Human Without Vest Start Ts'].notnull()]
kpi1.metric(
    label='People without vests',
    value=no_vest.shape[0],
)
kpi_dataset = pd.read_csv('data/sub_processes_delta.csv')
kpi2.metric(
    label='Median turnaround time',
    value=f'{kpi_dataset.iloc[8,1]}',
)

kpi3.metric(
    label='Longest process',
    value=f'{kpi_dataset.iloc[5,0]}@{kpi_dataset.iloc[5,1]}',
)

# with st.container():
#     corr_matrix = pd.read_csv('data/corr_matrix.csv')
#     st.title('Correlation Heatmap Example')

#     # Display the correlation heatmap using seaborn
#     st.set_option('deprecation.showPyplotGlobalUse', False)
#     plt.figure(figsize=(10, 8))
#     sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
#     st.pyplot()


st.write('Interesting finding: No strong correlation was found between a plane departing late and any flight-readiness subprocesses, but when the passenger bridge retracted had the strongest correlation')