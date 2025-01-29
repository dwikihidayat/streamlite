import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

days_df = pd.read_csv("../../data/raw/day.csv")
hours_df = pd.read_csv("../../data/raw/hour.csv")

# Menghapus kolom yang tidak diperlukan
days_df.drop(columns=["instant", "dteday"], inplace=True)
hours_df.drop(columns=["instant", "dteday"], inplace=True)

# Mengisi nilai yang hilang dengan nilai rata-rata kolom
days_df.fillna(days_df.mean(), inplace=True)
hours_df.fillna(hours_df.mean(), inplace=True)

# Mengubah tipe data kolom yang sesuai
days_df["season"] = days_df["season"].astype("category")
hours_df["season"] = hours_df["season"].astype("category")

# Menampilkan beberapa baris pertama dari data yang telah diproses

# Membuat visualisasi distribusi jumlah penyewaan sepeda berdasarkan musim
st.write("Distribusi jumlah penyewaan sepeda berdasarkan musim (Days):")
fig, ax = plt.subplots()
sns.countplot(data=days_df, x="season", ax=ax)
st.pyplot(fig)

st.write("Distribusi jumlah penyewaan sepeda berdasarkan musim (Hours):")
fig, ax = plt.subplots()
sns.countplot(data=hours_df, x="season", ax=ax)
st.pyplot(fig)

# Membuat visualisasi hubungan antara suhu dan jumlah penyewaan sepeda
st.write("Hubungan antara suhu dan jumlah penyewaan sepeda (Days):")
fig, ax = plt.subplots()
sns.scatterplot(data=days_df, x="temp", y="cnt", ax=ax)
st.pyplot(fig)

st.write("Hubungan antara suhu dan jumlah penyewaan sepeda (Hours):")
fig, ax = plt.subplots()
sns.scatterplot(data=hours_df, x="temp", y="cnt", ax=ax)
st.pyplot(fig)

# Membuat visualisasi boxplot jumlah penyewaan sepeda berdasarkan hari dalam seminggu
st.write("Boxplot jumlah penyewaan sepeda berdasarkan hari dalam seminggu (Days):")
fig, ax = plt.subplots()
sns.boxplot(data=days_df, x="weekday", y="cnt", ax=ax)
st.pyplot(fig)

st.write("Boxplot jumlah penyewaan sepeda berdasarkan hari dalam seminggu (Hours):")
fig, ax = plt.subplots()
sns.boxplot(data=hours_df, x="weekday", y="cnt", ax=ax)
st.pyplot(fig)
if __name__ == "__main__":
    st.title("Proyek Analisis Data Penyewaan Sepeda")
    st.write(
        "Aplikasi ini menampilkan analisis data penyewaan sepeda berdasarkan dataset yang tersedia."
    )
