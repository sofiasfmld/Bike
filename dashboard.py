import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly_rentals.index, monthly_rentals.values, marker='o', linestyle='-', color='blue')
    ax.set_title('Jumlah Penyewaan Sepeda per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticks(monthly_rentals.index)
    ax.grid()
    st.pyplot(fig)

# Page 2: Pengaruh Cuaca
elif menu_choice == "Pengaruh Cuaca":
    st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    weather_counts = main_data.groupby('weathersit')['cnt'].sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    weather_counts.plot(kind='bar', color='lightblue', ax=ax)
    ax.set_title('Pengaruh Jenis Cuaca terhadap Jumlah Penyewaan Sepeda')
    ax.set_xlabel('Jenis Cuaca')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticklabels(['Clear', 'Mist', 'Light Rain', 'Heavy Rain'], rotation=0)
    st.pyplot(fig)

# Page 3: Penyewaan Hari Libur
elif menu_choice == "Penyewaan Hari Libur":
    st.header("Perbandingan Penyewaan pada Hari Libur vs Hari Biasa")
    holiday_counts = main_data.groupby('holiday')['cnt'].sum()

    fig, ax = plt.subplots(figsize=(8, 5))
    holiday_counts.plot(kind='bar', color='orange', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda pada Hari Libur vs Hari Biasa')
    ax.set_xlabel('Hari Libur')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticklabels(['Biasa', 'Libur'], rotation=0)
    st.pyplot(fig)

# Page 4: Proporsi Pengguna
elif menu_choice == "Proporsi Pengguna":
    st.header("Proporsi Penyewaan oleh Pengguna Terdaftar dan Kasual")
    user_counts = main_data[['casual', 'registered']].sum()

    fig, ax = plt.subplots(figsize=(8, 6))
    user_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen'], ax=ax)
    ax.set_title('Proporsi Penyewaan oleh Pengguna Terdaftar dan Kasual')
    ax.set_ylabel('')  # Menghapus label y
    st.pyplot(fig)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Dashboard dibuat menggunakan Streamlit. Pilih menu di sidebar untuk menampilkan visualisasi.")
