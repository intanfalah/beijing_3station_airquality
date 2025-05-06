import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("./cleaned_data.csv")
    df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]])
    df["date"] = df["datetime"].dt.date
    return df

df = load_data()

# Sidebar filter
st.sidebar.header("Filter Data")
stations = df["station"].unique()
selected_stations = st.sidebar.multiselect("Pilih Stasiun", stations, default=stations)
date_range = st.sidebar.date_input("Rentang Waktu", [df["date"].min(), df["date"].max()])

# Filter data
filtered_df = df[(df["station"].isin(selected_stations)) &
                 (df["date"] >= date_range[0]) &
                 (df["date"] <= date_range[1])]

# 1️⃣ Tren PM2.5
st.subheader("📊 Tren Kualitas Udara per Stasiun (PM2.5)")
fig, ax = plt.subplots(figsize=(15, 6))
sns.lineplot(data=filtered_df, x="datetime", y="PM2.5", hue="station", ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Waktu")
plt.ylabel("Konsentrasi PM2.5 (µg/m³)")
plt.title("Tren PM2.5 dari Waktu ke Waktu")
st.pyplot(fig)

# 2️⃣ Korelasi antar parameter
st.subheader("🔍 Korelasi Parameter Kualitas Udara")
cols = ["PM2.5", "PM10", "SO2", "NO2", "O3", "CO", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
corr_matrix = df[cols].corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
plt.title("Matriks Korelasi Antar Parameter")
st.pyplot(fig)

# 3️⃣ Boxplot antar stasiun
st.subheader("📌 Perbandingan Kualitas Udara Antarstasiun")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=filtered_df, x="station", y="PM2.5")
plt.xticks(rotation=45)
plt.xlabel("Stasiun")
plt.ylabel("Konsentrasi PM2.5 (µg/m³)")
plt.title("Distribusi PM2.5 di Setiap Stasiun")
st.pyplot(fig)

# 4️⃣ Analisis RFM untuk PM2.5 Tinggi
st.subheader("📈 Analisis RFM (Recency, Frequency, Monetary) untuk PM2.5 Tinggi")

# Threshold untuk PM2.5 tinggi
threshold = 150
high_pm = df[df['PM2.5'] > threshold]

# RECENCY: Hitung hari sejak PM2.5 tinggi terakhir di tiap stasiun
snapshot_date = df['date'].max()  
recency = high_pm.groupby('station')['date'].max().apply(lambda x: (snapshot_date - x).days)

# FREQUENCY: Hitung berapa kali stasiun mengalami PM2.5 tinggi
frequency = high_pm.groupby('station').size()

# MONETARY: Hitung rata-rata PM2.5 saat tinggi
monetary = high_pm.groupby('station')['PM2.5'].mean()

# Gabungkan semua ke dalam DataFrame RFM
rfm = pd.DataFrame({
    'Recency': recency,
    'Frequency': frequency,
    'Monetary': monetary
}).reset_index()

# Tampilkan RFM
st.write(rfm)

# Korelasi antara metrik RFM
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(rfm[['Recency', 'Frequency', 'Monetary']].corr(), annot=True, cmap="Blues", ax=ax)
plt.title("Korelasi antara Metrik RFM")
st.pyplot(fig)

# 5️⃣ Visualisasi RFM
st.subheader("🔍 Visualisasi Metrik RFM")

# Plot distribusi Recency, Frequency, and Monetary
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
sns.histplot(rfm['Recency'], kde=True, ax=axes[0])
axes[0].set_title('Distribusi Recency')
sns.histplot(rfm['Frequency'], kde=True, ax=axes[1])
axes[1].set_title('Distribusi Frequency')
sns.histplot(rfm['Monetary'], kde=True, ax=axes[2])
axes[2].set_title('Distribusi Monetary')

st.pyplot(fig)