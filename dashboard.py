import numpy as np
import pandas as pd
import streamlit as st

# Load data
main_data = pd.read_csv("main_data.csv")

# Convert date columns correctly
main_data['dteday'] = pd.to_datetime(main_data['dteday'], errors='coerce')

# Sidebar Navigation
st.sidebar.title("Navigation")
menu_options = ["Home", "Tren Penyewaan Sepeda", "Pengaruh Cuaca", "Penyewaan Hari Libur", "Proporsi Pengguna"]
menu_choice = st.sidebar.radio("Pilih halaman:", menu_options)

# Home Page
if menu_choice == "Home":
    st.title("Dashboard Analisis Penyewaan Sepeda 🚴‍♂️")
    st.write("""
    Selamat datang di Dashboard Analisis Penyewaan Sepeda! 
    Pada dashboard ini, Anda dapat menjelajahi beberapa visualisasi yang memberikan insight dari data penyewaan sepeda berdasarkan beberapa aspek:

    1. **Tren Penyewaan Sepeda**: Melihat bagaimana tren penyewaan sepeda sepanjang tahun.
    2. **Pengaruh Cuaca**: Mengetahui jenis cuaca yang paling mempengaruhi jumlah penyewaan sepeda.
    3. **Penyewaan Hari Libur**: Menganalisis jumlah penyewaan sepeda pada hari libur dibandingkan hari biasa.
    4. **Proporsi Pengguna**: Menampilkan proporsi penyewaan yang dilakukan oleh pengguna terdaftar dan pengguna kasual.
    
    Pilih salah satu menu di sidebar untuk melihat visualisasi lebih lanjut.
    """)

# Page 1: Tren Penyewaan Sepeda
elif menu_choice == "Tren Penyewaan Sepeda":
    st.header("Tren Penyewaan Sepeda Sepanjang Tahun")
    monthly_rentals = main_data.groupby(main_data['dteday'].dt.month)['cnt'].sum()
    monthly_rentals.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    st.line_chart(monthly_rentals)

# Page 2: Pengaruh Cuaca
elif menu_choice == "Pengaruh Cuaca":
    st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    weather_counts = main_data.groupby('weathersit')['cnt'].sum()
    weather_labels = ['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Berat']
    st.bar_chart(weather_counts.rename(weather_labels))

# Page 3: Penyewaan Hari Libur
elif menu_choice == "Penyewaan Hari Libur":
    st.header("Perbandingan Penyewaan pada Hari Libur vs Hari Biasa")
    holiday_counts = main_data.groupby('holiday')['cnt'].sum()
    holiday_labels = ['Biasa', 'Libur']
    st.bar_chart(holiday_counts.rename(holiday_labels))

# Page 4: Proporsi Pengguna
elif menu_choice == "Proporsi Pengguna":
    st.header("Proporsi Penyewaan oleh Pengguna Terdaftar dan Kasual")
    user_counts = main_data[['casual', 'registered']].sum()
    st.bar_chart(user_counts)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Dashboard dibuat menggunakan Streamlit. Pilih menu di sidebar untuk menampilkan visualisasi.")
