import pandas as pd
import streamlit as st
from babel.numbers import format_currency
from datetime import datetime
##Import Data
day_df = pd.read_csv("https://raw.githubusercontent.com/mrscriptword/Dicoding/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/mrscriptword/Dicoding/main/hour.csv")
#Bagian Atas dari dashboard
st.header('Pengembangan Dasboard menggunakan Python:🎉:')
st.subheader("Selamat Datang di dashboard Rendy Ilyasa")

#Bagian Sidebar
with st.sidebar:
    st.title("Daftar Data Rental Sepeda Berdasarkan :")
    selected_data = st.radio("Pilih Data", ["Hari", "Jam"])

#Konten
if selected_data == "Berdasarkan Hari":
        st.header("Hari")
        st.table(day_df)
else:
        st.header("Berdasarkan Jam")
        st.table(hour_df)
