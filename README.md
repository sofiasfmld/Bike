# Dashboard Proyek Analisis Data

## Deskripsi Proyek

Proyek ini merupakan sebuah dashboard interaktif yang dibangun menggunakan Python dan Streamlit. Dashboard ini memungkinkan pengguna untuk mengeksplorasi data, menampilkan visualisasi, dan memberikan insight utama dari data secara dinamis. Data diolah dan divisualisasikan dalam dashboard yang sudah terintegrasi untuk memudahkan pengguna dalam memahami hasil analisis.

## Struktur Proyek

Struktur folder dan file utama dalam proyek ini adalah sebagai berikut:

- `dashboard.py`: Skrip utama yang digunakan untuk menjalankan dashboard berbasis Streamlit.
- `data/`: Folder ini berisi dataset tambahan berupa dua file, `day.csv` dan `hour.csv`, yang digunakan untuk analisis lebih lanjut.
- `notebook.ipynb`: Notebook Jupyter yang digunakan untuk eksplorasi dan analisis data awal sebelum diimplementasikan dalam dashboard.
- `README.md`: Berkas ini berisi dokumentasi proyek, termasuk cara instalasi dan penggunaan.
- `requirements.txt`: Daftar pustaka Python yang diperlukan agar proyek ini dapat berjalan dengan baik.
- `url.txt`: Berkas yang memuat URL untuk mengakses dashboard yang sudah dideploy.

## Panduan Instalasi dari File ZIP

Jika Anda menggunakan file ZIP, ikuti langkah-langkah berikut:

1. Ekstrak file ZIP melalui link https://github.com/sofiasfmld/Bike.
2. Buka terminal dan arahkan ke direktori tempat file ZIP diekstrak.
3. Instal dependensi dari `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Menjalankan Dashboard dari File ZIP

   Jalankan dashboard dengan perintah:

   ```bash
   streamlit run dashboard.py
   ```

Anda juga dapat mengakses versi dashboard yang telah dideploy melalui tautan berikut:

[Dashboard yang sudah dideploy](https://app-dashboard-mtuc8jpwft8exmrrvvdhz8.streamlit.app/)


## Analisis di Jupyter Notebook

File `notebook.ipynb` berisi analisis data awal dan eksplorasi yang dilakukan sebelum data diterapkan pada dashboard. Anda dapat membukanya dengan Jupyter Notebook atau JupyterLab untuk melihat detail analisis yang telah dilakukan.

## Dependensi

Proyek ini menggunakan pustaka Python berikut:

- `matplotlib`
- `pandas`
- `numpy`
- `seaborn`
- `streamlit`
