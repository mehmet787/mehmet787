import pandas as pd

file_path = r'C:\Users\it.stajyer\Desktop\Dijital_Olgunluk.xlsx'
df_strateji = pd.read_excel(file_path, sheet_name='1-Strateji')
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

df_strateji.loc[13, 'KKM'] = KKM_count
df_strateji.loc[13, 'KM'] = KM_count
df_strateji.loc[13, 'K'] = K_count
df_strateji.loc[13, 'KK'] = KK_count

print("KKM sütunundaki X sayısı:", KKM_count)
print("KM sütunundaki X sayısı:", KM_count)
print("K sütunundaki X sayısı:", K_count)
print("KK sütunundaki X sayısı:", KK_count)

KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0



for i in range(15, 25):
    if df_strateji.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df_strateji.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df_strateji.loc[i, 'K'] == 'X':
        K_count += 1
    if df_strateji.loc[i, 'KK'] == 'X':
        KK_count += 1

df_strateji.loc[25, 'KKM'] = KKM_count
df_strateji.loc[25, 'KM'] = KM_count
df_strateji.loc[25, 'K'] = K_count
df_strateji.loc[25, 'KK'] = KK_count

print("KKM sütunundaki X sayısı:", KKM_count)
print("KM sütunundaki X sayısı:", KM_count)
print("K sütunundaki X sayısı:", K_count)
print("KK sütunundaki X sayısı:", KK_count)

KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0

for i in range(27, 37):
    if df_strateji.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df_strateji.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df_strateji.loc[i, 'K'] == 'X':
        K_count += 1
    if df_strateji.loc[i, 'KK'] == 'X':
        KK_count += 1

df_strateji.loc[37, 'KKM'] = KKM_count
df_strateji.loc[37, 'KM'] = KM_count
df_strateji.loc[37, 'K'] = K_count
df_strateji.loc[37, 'KK'] = KK_count

print("KKM sütunundaki X sayısı:", KKM_count)
print("KM sütunundaki X sayısı:", KM_count)
print("K sütunundaki X sayısı:", K_count)
print("KK sütunundaki X sayısı:", KK_count)


KKM_count = 0
KM_count = 0
K_count = 0
KK_count = 0

for i in range(39, 58):
    if df_strateji.loc[i, 'KKM'] == 'X':
        KKM_count += 1
    if df_strateji.loc[i, 'KM'] == 'X':
        KM_count += 1
    if df_strateji.loc[i, 'K'] == 'X':
        K_count += 1
    if df_strateji.loc[i, 'KK'] == 'X':
        KK_count += 1

df_strateji.loc[58, 'KKM'] = KKM_count
df_strateji.loc[58, 'KM'] = KM_count
df_strateji.loc[58, 'K'] = K_count
df_strateji.loc[58, 'KK'] = KK_count

print("KKM sütunundaki X sayısı:", KKM_count)
print("KM sütunundaki X sayısı:", KM_count)
print("K sütunundaki X sayısı:", K_count)
print("KK sütunundaki X sayısı:", KK_count)








