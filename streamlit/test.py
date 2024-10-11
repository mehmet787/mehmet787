import pandas as pd

file_path = r'C:\Users\it.stajyer\Desktop\Dijital_Olgunluk.xlsx'
df_strateji = pd.read_excel(file_path, sheet_name='1-Strateji')


def count_X_vectorized(df, start, end, label):
    subset = df.loc[start:end, ['KKM', 'KM', 'K', 'KK']]
    counts = (subset == 'X').sum()

    # Sonuçları belirtilen satıra ekle
    df.loc[label, ['KKM', 'KM', 'K', 'KK']] = counts


count_X_vectorized(df_strateji, 3, 13, 13)
count_X_vectorized(df_strateji, 15, 24, 25)
count_X_vectorized(df_strateji, 27, 36, 37)
count_X_vectorized(df_strateji, 39, 57, 58)

pd.set_option('display.max_columns', None)

print(df_strateji)















































