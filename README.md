# Dashboard Kualitas Udara

Ini adalah aplikasi Streamlit yang menampilkan dashboard untuk analisis kualitas udara menggunakan data pengukuran PM2.5 dan berbagai parameter cuaca dari beberapa stasiun. Dashboard ini menyediakan tren kualitas udara per stasiun, korelasi antar parameter, perbandingan kualitas udara antar stasiun, dan analisis RFM (Recency, Frequency, Monetary) untuk polusi tinggi.

## Fitur
1. **Tren PM2.5**: Menampilkan tren PM2.5 per stasiun dari waktu ke waktu.
2. **Korelasi Parameter**: Matriks korelasi antara berbagai parameter kualitas udara dan cuaca.
3. **Perbandingan Kualitas Udara Antarstasiun**: Boxplot distribusi PM2.5 di setiap stasiun.
4. **Analisis RFM (Recency, Frequency, Monetary)**: Mengidentifikasi stasiun dengan kejadian polusi tinggi berdasarkan analisis RFM.

## Prasyarat

Sebelum menjalankan aplikasi, pastikan kamu sudah menginstal semua dependensi yang diperlukan.

### 1. Setup Virtual Environment
Disarankan untuk menggunakan **virtual environment** untuk mengelola dependensi project.

1. **Buat virtual environment**:
   ```bash
   python -m venv venv
2. **Install Library yang Dibutuhkan**:
   pip install -r requirements.txt
3. **Menjalankan Dashboard**:
   cd dashboard
   streamlit run dashboard.py