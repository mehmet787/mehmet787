import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Streamlit uygulamasının başlığı
st.title("Dijital Olgunluk Analizi")

# Excel dosyasını oku
file_path = r'C:\Users\it.stajyer\Desktop\Dijital_Olgunluk.xlsx'
df_strateji = pd.read_excel(file_path, sheet_name='1-Strateji')

def count_X_vectorized(df, start, end, label):
    subset = df.loc[start:end, ['KKM', 'KM', 'K', 'KK']]
    counts = (subset == 'X').sum()

    # Sonuçları belirtilen satıra ekle
    df.loc[label, ['KKM', 'KM', 'K', 'KK']] = counts

# X sayımlarını hesapla
count_X_vectorized(df_strateji, 3, 13, 13)
count_X_vectorized(df_strateji, 15, 24, 25)
count_X_vectorized(df_strateji, 27, 36, 37)
count_X_vectorized(df_strateji, 39, 57, 58)

# Sonuçları al
KKM_count = df_strateji.loc[13, 'KKM']
KM_count = df_strateji.loc[25, 'KM']
K_count = df_strateji.loc[37, 'K']
KK_count = df_strateji.loc[58, 'KK']

# Sonuçları toplama
total_KKM = df_strateji.loc[13, 'KKM'] + df_strateji.loc[25, 'KKM'] + df_strateji.loc[37, 'KKM'] + df_strateji.loc[58, 'KKM']
total_KM = df_strateji.loc[13, 'KM'] + df_strateji.loc[25, 'KM'] + df_strateji.loc[37, 'KM'] + df_strateji.loc[58, 'KM']
total_K = df_strateji.loc[13, 'K'] + df_strateji.loc[25, 'K'] + df_strateji.loc[37, 'K'] + df_strateji.loc[58, 'K']
total_KK = df_strateji.loc[13, 'KK'] + df_strateji.loc[25, 'KK'] + df_strateji.loc[37, 'KK'] + df_strateji.loc[58, 'KK']

# Sonuçları göster
st.write("KKM sütunundaki toplam X sayısı:", total_KKM)
st.write("KM sütunundaki toplam X sayısı:", total_KM)
st.write("K sütunundaki toplam X sayısı:", total_K)
st.write("KK sütunundaki toplam X sayısı:", total_KK)

# Radar grafiği için verileri hazırla
labels = ['KKM', 'KM', 'K', 'KK']
counts = [total_KKM, total_KM, total_K, total_KK]

# Radar grafiği oluşturma
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
counts += counts[:1]  # İlk değeri tekrar ekleyerek grafiği kapat
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, counts, color='orange', alpha=0.25)
ax.plot(angles, counts, color='orange', linewidth=2)

# Etiketleri ayarla
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

ax.set_title('Sütunlardaki X Değerlerinin Toplamı - Radar Grafiği')

# Streamlit'te grafiği göster
st.pyplot(fig)










