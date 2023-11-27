import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
from pathlib import Path
st.header('Pengembangan Dasboard menggunakan Python:👋:')
st.subheader("Selamat Datang di dashboard Rendy Ilyasa")

def create_Musim_df(df):
    byMusim_df = df.groupby(by="Musim").instant.nunique().reset_index()
    byMusim_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byMusim_df

def create_yr_df(df):
    byyr_df = df.groupby(by="yr").instant.nunique().reset_index()
    byyr_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byyr_df

def create_holiday_df(df):
    byholiday_df = df.groupby(by="holiday").instant.nunique().reset_index()
    byholiday_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    
    return byholiday_df

def create_workingday_df(df):
    byworkingday_df = df.groupby(by="workingday").instant.nunique().reset_index()
    byworkingday_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    
    return byworkingday_df

def create_weathersit_df(df):
    byweathersit_df = df.groupby(by="weathersit").instant.nunique().reset_index()
    byweathersit_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byweathersit_df

def sidebar(df):
    df["dteday"] = pd.to_datetime(df["dteday"])
    min_date = df["dteday"].min()
    max_date = df["dteday"].max()

    with st.sidebar:
        st.title("Minetod Store")
        st.image("https://raw.githubusercontent.com/mrscriptword/Dicoding/main/Logo%20Baru.png")
        def on_change():
            st.session_state.date = date

        date = st.date_input(
            label="Rentang Waktu", 
            min_value=min_date, 
            max_value=max_date,
            value=[min_date, max_date],
            on_change=on_change
        )

    return date

def Musim(df):
    st.subheader("Musim")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="Musim",
        y="sum",
        data=df.sort_values(by="Musim", ascending=False),
        ax=ax
    )
    ax.set_title("Rental Sepeda Berdasarkan Musim", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def year(df):
    st.subheader("Tahun")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="yr",
        y="sum",
        data=df.sort_values(by="yr", ascending=False),
        ax=ax
    )
    ax.set_title("Rental Sepeda Berdasarkan Tahun", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def month(df):
    st.subheader("Bulan")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="mnth",
        y="cnt",
        data=df.sort_values(by="mnth", ascending=False),
        ax=ax
    )
    ax.set_title("Rental Sepeda Berdasarkan Bulan", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def holiday(df):
    st.subheader("Hari Libur")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="holiday",
        y="sum",
        data=df.sort_values(by="holiday", ascending=False),
        ax=ax
    )
    ax.set_title("Rental Sepeda Berdasarkan Hari Libur", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def workingday(df):
    st.subheader("Hari Kerja")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="workingday",
        y="sum",
        data=df.sort_values(by="workingday", ascending=False),
        ax=ax
    )
    ax.set_title("Rental Sepeda Berdasarkan Hari Kerja", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def weathersit(df):
    st.subheader("Cuaca")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="weathersit",
        y="sum",
        data=df.sort_values(by="weathersit", ascending=False),
        ax=ax
    )
    ax.set_title("Rental Sepeda Berdasarkan Cuaca", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

if __name__ == "__main__":
    sns.set(style="white")

    st.header("Rental Sepeda :bike:")

    day_df_csv = Path(__file__).parents[1] / 'Modul Pembelajaran Data Science Dicoding/data_day_bersih.csv'

    day_df = pd.read_csv(day_df_csv)

    date = sidebar(day_df)
    if len(date) == 2:
        main_df = day_df[(day_df["dteday"] >= str(date[0])) & (day_df["dteday"] <= str(date[1]))]
    else:
        main_df = day_df[(day_df["dteday"] >= str(st.session_state.date[0])) & (day_df["dteday"] <= str(st.session_state.date[1]))]

    Musim_df = create_Musim_df(main_df)
    Musim(Musim_df)
    year_df = create_yr_df(main_df)
    year(year_df)
    month(main_df)
    holiday_df = create_holiday_df(main_df)
    holiday(holiday_df)
    workingday_df = create_workingday_df(main_df)
    workingday(workingday_df)
    weathersit_df = create_weathersit_df(main_df)
    weathersit(weathersit_df)
    copyright = "Copyright 20234 @ Minetod Store | By Rendy Ilyasa"
    st.caption(copyright)
