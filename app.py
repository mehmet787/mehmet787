import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Excel dosyasını oku
file_path = r'C:\Users\it.stajyer\Desktop\Dijital_Olgunluk yeni.xlsx'
sheet_name = '1-Strateji'
df = pd.read_excel(file_path, sheet_name=sheet_name)  # DataFrame'i burada tanımlayın

KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0

for i in range(3, 13):
    if df.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df.loc[i, 'K'] == 'X':
        K_count += 1
    if df.loc[i, 'KK'] == 'X':
        KK_count += 1

df.loc[13, 'KKM'] = KKM_count
df.loc[13, 'KM'] = KM_count
df.loc[13, 'K'] = K_count
df.loc[13, 'KK'] = KK_count


KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0

for i in range(15, 25):
    if df.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df.loc[i, 'K'] == 'X':
        K_count += 1
    if df.loc[i, 'KK'] == 'X':
        KK_count += 1

df.loc[25, 'KKM'] = KKM_count
df.loc[25, 'KM'] = KM_count
df.loc[25, 'K'] = K_count
df.loc[25, 'KK'] = KK_count


KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0

for i in range(27, 37):
    if df.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df.loc[i, 'K'] == 'X':
        K_count += 1
    if df.loc[i, 'KK'] == 'X':
        KK_count += 1

df.loc[37, 'KKM'] = KKM_count
df.loc[37, 'KM'] = KM_count
df.loc[37, 'K'] = K_count
df.loc[37, 'KK'] = KK_count

KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0

for i in range(39, 58):
    if df.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df.loc[i, 'K'] == 'X':
        K_count += 1
    if df.loc[i, 'KK'] == 'X':
        KK_count += 1

df.loc[58, 'KKM'] = KKM_count
df.loc[58, 'KM'] = KM_count
df.loc[58, 'K'] = K_count
df.loc[58, 'KK'] = KK_count



df.loc[59, 'KKM'] = df.loc[13, 'KKM'] + df.loc[25, 'KKM'] + df.loc[37, 'KKM']+ df.loc[58, 'KKM']
df.loc[59, 'KM'] = df.loc[13, 'KM'] + df.loc[25, 'KM'] + df.loc[37, 'KM']+ df.loc[58, 'KKM']
df.loc[59, 'K'] = df.loc[13, 'K'] + df.loc[25, 'K'] + df.loc[37, 'K']+ df.loc[58, 'KKM']
df.loc[59, 'KK'] = df.loc[13, 'KK'] + df.loc[25, 'KK'] + df.loc[37, 'KK']+ df.loc[58, 'KKM']


# Radar grafiği için verileri hazırlama
labels = ['KKM', 'KM', 'K', 'KK']
values = [df.loc[13, 'KKM'], df.loc[13, 'KM'], df.loc[13, 'K'], df.loc[13, 'KK']]
values2 = [df.loc[25, 'KKM'], df.loc[25, 'KM'], df.loc[25, 'K'], df.loc[25, 'KK']]
values3 = [df.loc[37, 'KKM'], df.loc[37, 'KM'], df.loc[37, 'K'], df.loc[37, 'KK']]
values4 = [df.loc[58, 'KKM'], df.loc[58, 'KM'], df.loc[58, 'K'], df.loc[58, 'KK']]

values += values[:1]
values2 += values2[:1]
values3 += values3[:1]
values4 += values3[:1]



angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]  # Kapamak için ilk açıyı tekrar ekle


fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))


ax.fill(angles, values, color='b', alpha=0.25, label='Satır 12')
ax.fill(angles, values2, color='r', alpha=0.25, label='Satır 19')
ax.fill(angles, values3, color='g', alpha=0.25, label='Satır 26')
ax.fill(angles, [df.loc[27, 'KKM'], df.loc[27, 'KM'], df.loc[27, 'K'], df.loc[27, 'KK']] + [df.loc[27, 'KKM']], color='m', alpha=0.25, label='Toplam (Satır 27)')

ax.plot(angles, values, color='b', linewidth=2)
ax.plot(angles, values2, color='r', linewidth=2)
ax.plot(angles, values3, color='g', linewidth=2)
ax.plot(angles, [df.loc[27, 'KKM'], df.loc[27, 'KM'], df.loc[27, 'K'], df.loc[27, 'KK']] + [df.loc[27, 'KKM']], color='m', linewidth=2)

# Kategorileri ekleme
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Başlık ve legend
ax.set_title('KKM, KM, K, KK Radar Grafiği', size=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Grafiği gösterme
plt.show()







































