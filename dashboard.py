# import library
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import library

# pembuatan data frame
tian_df = pd.read_csv("tiantan.csv")
tian_df.head()
# pembuatan data frame

# tingkat polusi udara per jam pada tanggal 2013-03-01
air_polution_hour = tian_df.groupby(by = ['year', 'month', 'day','hour'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month', 'day','hour'], ascending = True)
air_polution_hour = air_polution_hour.reset_index()
air_polution_hour['time'] = air_polution_hour["hour"].astype(str) + ":00"
air_polution_hour.head(24)

# Tingkat polusi selama 10 hari pada tanggal 2013-03-01 sampai 2013-03-10 (10 data pertama)
air_polution_day = tian_df.groupby(by = ['year', 'month', 'day'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month', 'day'], ascending = True)
air_polution_day = air_polution_day.reset_index()
air_polution_day['time'] = air_polution_day["year"].astype(str) + "-" + air_polution_day["month"].astype(str) + "-" + air_polution_day["day"].astype(str)
air_polution_day.head(10)

# Tingkat polusi selama 10 bulan pada tanggal 2013-03 sampai 2013-10 (10 data pertama)
air_polution_month = tian_df.groupby(by = ['year', 'month'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month'], ascending = True)
air_polution_month = air_polution_month.reset_index()
air_polution_month['time'] = air_polution_month["year"].astype(str) + "-" + air_polution_month["month"].astype(str)
air_polution_month.head(10)

# polusi selama 5 tahun
air_polution_year = tian_df.groupby(by = ['year'] ).agg({
            "PM2.5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year'], ascending = True)
air_polution_year = air_polution_year.reset_index()
air_polution_year['time'] = air_polution_year["year"].astype(str)
air_polution_year.head(10)

# suhu dan tekanan selama 24 jam pada 2013-03-01
air_parameters_hour = tian_df.groupby(by = ['year', 'month', 'day','hour'] ).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year', 'month', 'day','hour'], ascending = True)
air_parameters_hour = air_parameters_hour.reset_index()
air_parameters_hour['time'] = air_parameters_hour["hour"].astype(str) + ":00"
air_parameters_hour.head(24)

# Suhu dan tekanan udara selama 10 hari tanggal 2013-03-01 sampai 2013-03-10
air_parameters_day = tian_df.groupby(by = ['year', 'month', 'day'] ).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year', 'month', 'day'], ascending = True)
air_parameters_day = air_parameters_day.reset_index()
air_parameters_day['time'] = air_parameters_day["year"].astype(str) + "-" + air_parameters_day["month"].astype(str) + "-" + air_parameters_day["day"].astype(str)
air_parameters_day.head(10)

# Suhu dan tekanan udara selama 10 bulan tanggal 2013-03 sampai 2013-10
air_parameters_month = tian_df.groupby(by = ['year', 'month']).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year', 'month'], ascending = True)
air_parameters_month = air_parameters_month.reset_index()
air_parameters_month['time'] = air_parameters_month["year"].astype(str) + "-" + air_parameters_month["month"].astype(str)
air_parameters_month.head(10)

# Suhu dan tekanan udara selama 5 tahun tanggal 2013 sampai 2017
air_parameters_year = tian_df.groupby(by = ['year'] ).agg({
            "TEMP" : "mean",
            "PRES" : "mean"}).sort_values(by = ['year'], ascending = True)
air_parameters_year = air_parameters_year.reset_index()
air_parameters_year['time'] = air_parameters_year["year"].astype(str)
air_parameters_year.head(5)

# korelasi suhu dan tekanan dengan polusi udara
correlation_df = tian_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES']].copy()


korelasi = correlation_df.corr(method = "pearson")


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
    
# eksplore data

# visualisasi data

st.set_page_config(layout="wide")

st.markdown('# ☁️🌀 Tiantan city air pollution dashboard')

st.write('---')

st.markdown('## Highest Frequency Pollution')

# Kolom-kolom yang mengandung data polutan udara
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Mencari frekuensi kemunculan masing-masing polutan
pollutant_counts = tian_df[pollutants].mode().iloc[0]

# Membuat diagram batang untuk polutan yang paling umum
with st.container():
    fig = plt.figure(figsize=(4, 4))
    pollutant_counts.plot(kind='bar', color='skyblue')
    plt.title('Polutan Udara dengan Jumlah Tertinggi Di Stasiun Tiantan')
    plt.xlabel('Polutan Udara')
    plt.ylabel('Frekuensi Kemunculan')
    plt.xticks(rotation=45)
    st.pyplot(fig) 


st.markdown('## Temperature, Pressure and Pollutan Correlation Heatmap')

# heatmap
with st.container():
    fig, ax = plt.subplots(figsize=(6,3))
    sns.heatmap(korelasi, vmax = 1, vmin = -1, center = 0, cmap = "plasma")
    ax.tick_params(labelsize = 5)
    ax.set_title("Korelasi heatmap", loc="center", fontsize=5)
    st.pyplot(fig)     


st.markdown('## Temperature, Pressure and Pollutan Detailed Scatter Plot')

# Tampilan grafik scatter plot dengan menggunakan fungsi corr_scatter_graph(df)
def corr_scatter_graph(df):
    with st.expander("Air Quality VS Temperature"):
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        ax1.scatter(df['TEMP'], df['PM2.5'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax1.set_xlabel("TEMPERATURE", fontsize = 20)
        ax1.set_ylabel("PM2.5", fontsize = 20)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.scatter(df['TEMP'], df['PM10'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        ax2.set_xlabel("TEMPERATURE", fontsize = 20)
        ax2.set_ylabel("PM10", fontsize = 20)
        st.pyplot(fig2)

        fig3, ax3 = plt.subplots(figsize=(8, 4))
        ax3.scatter(df['TEMP'], df['SO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax3.set_xticklabels([])
        ax3.set_yticklabels([])
        ax3.set_xlabel("TEMPERATURE", fontsize = 20)
        ax3.set_ylabel("SO2", fontsize = 20)
        st.pyplot(fig3)

        fig4, ax4 = plt.subplots(figsize=(8, 4))
        ax4.scatter(df['TEMP'], df['NO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax4.set_xticklabels([])
        ax4.set_yticklabels([])
        ax4.set_xlabel("TEMPERATURE", fontsize = 20)
        ax4.set_ylabel("NO2", fontsize = 20)
        st.pyplot(fig4)

        fig5, ax5 = plt.subplots(figsize=(8, 4))
        ax5.scatter(df['TEMP'], df['CO'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax5.set_xticklabels([])
        ax5.set_yticklabels([])
        ax5.set_xlabel("TEMPERATURE", fontsize = 20)
        ax5.set_ylabel("CO", fontsize = 20)
        st.pyplot(fig5)

        fig6, ax6 = plt.subplots(figsize=(8, 4))
        ax6.scatter(df['TEMP'], df['O3'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax6.set_xticklabels([])
        ax6.set_yticklabels([])
        ax6.set_xlabel("TEMPERATURE", fontsize = 20)
        ax6.set_ylabel("O3", fontsize = 20)
        st.pyplot(fig6)

    with st.expander("Air Quality VS Pressure"):
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        ax1.scatter(df['PRES'], df['PM2.5'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax1.set_xlabel("PRESSURE", fontsize = 20)
        ax1.set_ylabel("PM2.5", fontsize = 20)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.scatter(df['PRES'], df['PM10'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])
        ax2.set_xlabel("PRESSURE", fontsize = 20)
        ax2.set_ylabel("PM10", fontsize = 20)
        st.pyplot(fig2)

        fig3, ax3 = plt.subplots(figsize=(8, 4))
        ax3.scatter(df['PRES'], df['SO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax3.set_xticklabels([])
        ax3.set_yticklabels([])
        ax3.set_xlabel("PRESSURE", fontsize = 20)
        ax3.set_ylabel("SO2", fontsize = 20)
        st.pyplot(fig3)

        fig4, ax4 = plt.subplots(figsize=(8, 4))
        ax4.scatter(df['PRES'], df['NO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax4.set_xticklabels([])
        ax4.set_yticklabels([])
        ax4.set_xlabel("PRESSURE", fontsize = 20)
        ax4.set_ylabel("NO2", fontsize = 20)
        st.pyplot(fig4)

        fig5, ax5 = plt.subplots(figsize=(8, 4))
        ax5.scatter(df['PRES'], df['CO'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax5.set_xticklabels([])
        ax5.set_yticklabels([])
        ax5.set_xlabel("PRESSURE", fontsize = 20)
        ax5.set_ylabel("CO", fontsize = 20)
        st.pyplot(fig5)

        fig6, ax6 = plt.subplots(figsize=(8, 4))
        ax6.scatter(df['PRES'], df['O3'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolor= "#ed7d53")
        ax6.set_xticklabels([])
        ax6.set_yticklabels([])
        ax6.set_xlabel("PRESSURE", fontsize = 20)
        ax6.set_ylabel("O3", fontsize = 20)
        st.pyplot(fig6)
    
corr_scatter_graph(correlation_df)
    

