# import library
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import library

import pandas as pd

# Membaca data dari file CSV
tian_df = pd.read_csv("dashboard/tiantan.csv")

# --- Agregasi data polusi udara berdasarkan waktu ---

# Rata-rata polusi per jam (contoh: untuk 2013-03-01)
air_polution_hour = (
    tian_df.groupby(['year', 'month', 'day', 'hour'])[
        ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    ]
    .mean()
    .reset_index()
    .sort_values(by=['year', 'month', 'day', 'hour'])
)
air_polution_hour['time'] = air_polution_hour['hour'].astype(str) + ":00"

# Rata-rata polusi per hari (contoh: 2013-03-01 sampai 2013-03-10)
air_polution_day = (
    tian_df.groupby(['year', 'month', 'day'])[
        ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    ]
    .mean()
    .reset_index()
    .sort_values(by=['year', 'month', 'day'])
)
air_polution_day['time'] = air_polution_day['year'].astype(str) + "-" + air_polution_day['month'].astype(str) + "-" + air_polution_day['day'].astype(str)

# Rata-rata polusi per bulan (contoh: 2013-03 sampai 2013-10)
air_polution_month = (
    tian_df.groupby(['year', 'month'])[
        ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    ]
    .mean()
    .reset_index()
    .sort_values(by=['year', 'month'])
)
air_polution_month['time'] = air_polution_month['year'].astype(str) + "-" + air_polution_month['month'].astype(str)

# Rata-rata polusi per tahun (contoh: 2013 sampai 2017)
air_polution_year = (
    tian_df.groupby('year')[
        ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    ]
    .mean()
    .reset_index()
    .sort_values(by='year')
)
air_polution_year['time'] = air_polution_year['year'].astype(str)

# --- Agregasi suhu dan tekanan berdasarkan waktu ---

# Per jam
air_parameters_hour = (
    tian_df.groupby(['year', 'month', 'day', 'hour'])[['TEMP', 'PRES']]
    .mean()
    .reset_index()
    .sort_values(by=['year', 'month', 'day', 'hour'])
)
air_parameters_hour['time'] = air_parameters_hour['hour'].astype(str) + ":00"


# Per hari
air_parameters_day = (
    tian_df.groupby(['year', 'month', 'day'])[['TEMP', 'PRES']]
    .mean()
    .reset_index()
    .sort_values(by=['year', 'month', 'day'])
)
air_parameters_day['time'] = air_parameters_day['year'].astype(str) + "-" + air_parameters_day['month'].astype(str) + "-" + air_parameters_day['day'].astype(str)

# Per bulan
air_parameters_month = (
    tian_df.groupby(['year', 'month'])[['TEMP', 'PRES']]
    .mean()
    .reset_index()
    .sort_values(by=['year', 'month'])
)
air_parameters_month['time'] = air_parameters_month['year'].astype(str) + "-" + air_parameters_month['month'].astype(str)

# Per tahun
air_parameters_year = (
    tian_df.groupby('year')[['TEMP', 'PRES']]
    .mean()
    .reset_index()
    .sort_values(by='year')
)
air_parameters_year['time'] = air_parameters_year['year'].astype(str)

# --- Korelasi suhu dan tekanan terhadap polutan udara ---
correlation_df = tian_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES']]
korelasi = correlation_df.corr(method='pearson')


def correlation_suhu(df):
    pm25_suhu = round(df['PM2.5'].corr(df['TEMP'], method ="pearson"),2)
    pm10_suhu = round(df['PM10'].corr(df['TEMP'], method ="pearson"),2)
    SO2_suhu = round(df['SO2'].corr(df['TEMP'], method ="pearson"),2)
    NO2_suhu = round(df['NO2'].corr(df['TEMP'], method ="pearson"),2)
    CO_suhu = round(df['CO'].corr(df['TEMP'], method ="pearson"),2)
    O3_suhu = round(df['O3'].corr(df['TEMP'], method ="pearson"),2)
    correlation_suhu = {'parameter': ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"],
                        'values' : [pm25_suhu, pm10_suhu, SO2_suhu, NO2_suhu, CO_suhu, O3_suhu]}
    correlation_suhu_df = pd.DataFrame(correlation_suhu)
    return correlation_suhu_df

korelasi_suhu = correlation_suhu(correlation_df)


def correlation_pres(df):
    pm25_pres = round(df['PM2.5'].corr(df['PRES'], method ="pearson"),2)
    pm10_pres = round(df['PM10'].corr(df['PRES'], method ="pearson"),2)
    SO2_pres = round(df['SO2'].corr(df['PRES'], method ="pearson"),2)
    NO2_pres = round(df['NO2'].corr(df['PRES'], method ="pearson"),2)
    CO_pres = round(df['CO'].corr(df['PRES'], method ="pearson"),2)
    O3_pres = round(df['O3'].corr(df['PRES'], method ="pearson"),2)
    correlation_pres = {'parameter': ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"],
                        'values' : [pm25_pres, pm10_pres, SO2_pres, NO2_pres, CO_pres, O3_pres]}
    correlation_pres_df = pd.DataFrame(correlation_pres)
    return correlation_pres_df

korelasi_tekanan = correlation_pres(correlation_df)


# Kolom-kolom yang mengandung data polutan udara
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Mencari nilai yang memiliki jumlah paling tinggi
high_pollutants = {}
for pollutant in pollutants:
    high_pollutant = tian_df[pollutant].mode().values[0]
    high_pollutants[pollutant] = high_pollutant

# Menampilkan polutan memiliki jumlah paling tinggim dalam dataset
print("Polutan Udara Paling Tinggi:")
for pollutant, value in high_pollutants.items():
    print(f"{pollutant}: {value}")
    
# Jumlah polutan per jam
total_polution_hour = (
    tian_df.groupby(['year', 'month', 'day', 'hour'])[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
    .sum()
    .reset_index()
    .sort_values(by=['year', 'month', 'day', 'hour'])
)
total_polution_hour['time'] = total_polution_hour['hour'].astype(str) + ":00"

# Jumlah polutan per hari
total_polution_day = (
    tian_df.groupby(['year', 'month', 'day'])[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
    .sum()
    .reset_index()
    .sort_values(by=['year', 'month', 'day'])
)
total_polution_day['time'] = (
    total_polution_day['year'].astype(str) + "-" +
    total_polution_day['month'].astype(str) + "-" +
    total_polution_day['day'].astype(str)
)

# Jumlah polutan per bulan
total_polution_month = (
    tian_df.groupby(['year', 'month'])[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
    .sum()
    .reset_index()
    .sort_values(by=['year', 'month'])
)
total_polution_month['time'] = (
    total_polution_month['year'].astype(str) + "-" + total_polution_month['month'].astype(str)
)

# Jumlah polutan per tahun
total_polution_year = (
    tian_df.groupby('year')[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
    .sum()
    .reset_index()
    .sort_values(by='year')
)
total_polution_year['time'] = total_polution_year['year'].astype(str)
    
# eksplore data

# visualisasi data

st.set_page_config(layout="wide")

st.markdown('# ☁️🌀 Tiantan City Air Pollution Dashboard')

st.write('---')

# Kolom-kolom yang mengandung data polutan udara
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Mencari frekuensi kemunculan masing-masing polutan
pollutant_counts = tian_df[pollutants].mode().iloc[0]

#Polutan per jam
st.markdown('## Pollutant per Hour Tren')

# Pilih polutan yang ingin divisualisasikan (opsional, bisa dibuat dropdown di Streamlit)
selected_pollutant_hour = st.multiselect(
    "Select Pollutant to Show:",
    ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'],
    key='pollutant per hour',
    placeholder="Select one pollutant:",
)

# Plot line chart
if selected_pollutant_hour!=[]:
    st.line_chart(
        data=total_polution_hour,
        x='time',  # waktu
        y=selected_pollutant_hour,  # kolom polutan
        use_container_width=True
    )
else:
    pass

# Polutan per hari
st.markdown('## Pollutant per Day Tren')

# Pilih polutan yang ingin divisualisasikan (opsional, bisa dibuat dropdown di Streamlit)
selected_pollutant_day = st.multiselect(
    "Select Pollutant to Show:",
    ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'],
    key='pollutant per day',
    placeholder="Select one pollutant:",
)

# Plot line chart
if selected_pollutant_day!=[]:
    st.line_chart(
        data=total_polution_day,
        x='time',  # waktu
        y=selected_pollutant_day,  # kolom polutan
        use_container_width=True
    )
else:
    pass    

# Polutan per bulan
st.markdown('## Pollutant per Month Tren')

# Pilih polutan yang ingin divisualisasikan (opsional, bisa dibuat dropdown di Streamlit)
selected_pollutant_month = st.multiselect(
    "Select Pollutant to Show:",
    ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'],
    key='pollutant per month',
    placeholder="Select one pollutant:",
)

# Plot line chart
if selected_pollutant_month!=[]:
    st.line_chart(
        data=total_polution_month,
        x='time',  # waktu
        y=selected_pollutant_month,  # kolom polutan
        use_container_width=True
    )
else:
    pass

# Polutan per tahun
st.markdown('## Pollutant per Year Tren')

# Pilih polutan yang ingin divisualisasikan (opsional, bisa dibuat dropdown di Streamlit)
selected_pollutant_year = st.multiselect(
    "Select Pollutant to Show:",
    ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'],
    key='pollutant per year',
    placeholder="Select one pollutant:",
)

# Plot line chart
if selected_pollutant_year!=[]:
    st.line_chart(
        data=total_polution_year,
        x='time',  # waktu
        y=selected_pollutant_year,  # kolom polutan
        use_container_width=True
    )
else:
    pass

# Frekuensi polutan terbanyak
st.markdown('## Highest Frequency Pollution')

# Membuat diagram batang untuk polutan yang paling banyak
with st.container():
    fig, ax = plt.subplots(figsize=(7, 2))
    
    ax.bar(pollutant_counts.index, pollutant_counts.values, color='red')
    ax.set_title("Polutan Udara Terbanyak di Stasiun Tiantan", fontsize=8)
    ax.set_xlabel("Jenis Polutan", fontsize=5)
    ax.set_ylabel("Jumlah Kemunculan", fontsize=5)

    ax.tick_params(axis='x', labelrotation=45, labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    st.pyplot(fig)


st.markdown('## Temperature, Pressure and Pollutan Correlation Heatmap')

# heatmap
with st.container():
    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_subplot(111)
    sns.heatmap(data=korelasi, ax=ax, cmap="plasma", vmin=-1, vmax=1, center=0)
    ax.tick_params(axis='both', labelsize=6)
    ax.set_title("Correlation Heatmap", fontsize=8, loc='center')
    st.pyplot(fig)

st.markdown('## Temperature, Pressure and Pollutan Detailed Scatter Plot')

# Tampilan grafik scatter plot dengan menggunakan fungsi corr_scatter_graph(df)
def corr_scatter_graph(df):
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    scatter_params = dict(s=400, alpha=0.5, c="#FACE2D", marker='o', edgecolors="#ed7d53")

    with st.expander("Air Quality VS Temperature"):
        for pol in pollutants:
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.scatter(df['TEMP'], df[pol], **scatter_params)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_xlabel("TEMPERATURE", fontsize=20)
            ax.set_ylabel(pol, fontsize=20)
            st.pyplot(fig)

    with st.expander("Air Quality VS Pressure"):
        for pol in pollutants:
            fig, ax = plt.subplots(figsize=(8, 3))
            ax.scatter(df['PRES'], df[pol], **scatter_params)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_xlabel("PRESSURE", fontsize=20)
            ax.set_ylabel(pol, fontsize=20)
            st.pyplot(fig)
    
corr_scatter_graph(correlation_df)
    

