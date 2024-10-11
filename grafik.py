import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

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

ax.set_title('Sütunlardaki X Değerlerinin Sayısı - Radar Grafiği')

# Grafiği göster
st.pyplot(fig)





