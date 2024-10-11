import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Excel dosyasını oku
file_path = r'C:\Users\it.stajyer\Desktop\Dijital_Olgunluk.xlsx'
df_strateji = pd.read_excel(file_path, sheet_name='1-Strateji')

# X sayımlarını hesapla
KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0

for i in range(3, 13):
    if df_strateji.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df_strateji.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df_strateji.loc[i, 'K'] == 'X':
        K_count += 1
    if df_strateji.loc[i, 'KK'] == 'X':
        KK_count += 1

# Sonuçları DataFrame'e yaz
df_strateji.loc[13, 'KKM'] = KKM_count
df_strateji.loc[13, 'KM'] = KM_count
df_strateji.loc[13, 'K'] = K_count
df_strateji.loc[13, 'KK'] = KK_count

# Streamlit arayüzü
st.title("X Değerleri Sayımı")

# Sonuçları göster
st.write("KKM sütunundaki X sayısı:", KKM_count)
st.write("KM sütunundaki X sayısı:", KM_count)
st.write("K sütunundaki X sayısı:", K_count)
st.write("KK sütunundaki X sayısı:", KK_count)

# Radar grafiği için verileri hazırla
labels = ['KKM', 'KM', 'K', 'KK']
counts = [KKM_count, KM_count, K_count, KK_count]

# Radar grafiği oluştur
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

ax.set_title('Sütunlardaki X Değerlerinin Sayısı')

# Grafiği Streamlit'te göster
st.pyplot(fig)


