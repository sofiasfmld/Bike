# Bike Sharing Dashboard 🚴‍♂️✨

Dashboard ini dibangun menggunakan **Streamlit** untuk menampilkan visualisasi dan analisis data penyewaan sepeda. Dashboard ini menggunakan dataset `main_data.csv` yang merupakan hasil penggabungan dari `day.csv` dan `hour.csv`.

## Fitur Dashboard
- Visualisasi jumlah penyewaan sepeda berdasarkan jam, hari, dan cuaca.
- Grafik interaktif untuk mengeksplorasi tren penyewaan.
- Analisis RFM (Recency, Frequency, Monetary) untuk mengidentifikasi pelanggan terbaik.
- Analisis dan prediksi jumlah penyewaan sepeda.

## Prasyarat
Pastikan Anda memiliki beberapa hal berikut sebelum memulai:

1. **Python** versi 3.7 atau lebih baru.
2. **Anaconda** (opsional) jika Anda ingin menggunakan environment terisolasi.
3. File `main_data.csv` yang merupakan hasil gabungan dari dataset `day.csv` dan `hour.csv`.

## Setup Environment dengan Anaconda
Jika Anda menggunakan Anaconda, ikuti langkah-langkah berikut untuk menyiapkan environment:

```bash
conda create --name bike-sharing-dashboard python=3.9
conda activate bike-sharing-dashboard
pip install -r requirements.txt

Jika tidak menggunakan Anaconda, Anda dapat menyiapkan environment menggunakan pipenv atau venv:

# Buat direktori proyek
mkdir proyek_bike_sharing
cd proyek_bike_sharing

# Install pipenv jika belum ada
pip install pipenv

# Buat environment dengan pipenv dan aktifkan
pipenv install
pipenv shell

# Install dependencies dari berkas requirements.txt
pip install -r requirements.txt
