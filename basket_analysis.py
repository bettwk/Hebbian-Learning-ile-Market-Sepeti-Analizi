import pandas as pd
import numpy as np

print("veri okunuyor bekleyiniz...")

#df = pd.read_excel('Assignment-1_Data.xlsx')
#df.to_csv('Assignment-1_Data.csv', index=False)
df = pd.read_csv('Assignment-1_Data.csv')

urun_sayisi = df['Itemname'].nunique()
print(f"Toplam benzersiz urun sayisi: {urun_sayisi}")

ogrenme_orani = 1.0 

print("Egitim (RAM dostu eslestirme) basliyor...")

ortak_sepet = pd.merge(df, df, on='BillNo')

farkli_urunler = ortak_sepet[ortak_sepet['Itemname_x'] != ortak_sepet['Itemname_y']]

baglar = farkli_urunler.groupby(['Itemname_x', 'Itemname_y']).size().reset_index(name='Agirlik')

baglar['Agirlik'] = baglar['Agirlik'] * ogrenme_orani

print("Egitim tamamlandi!")

print("\n--- En Sik Birlikte Alinan Urunler (En Guclu Sinaptik Baglar) ---")


guclu_baglar = baglar.sort_values(by='Agirlik', ascending=False)

print(guclu_baglar.head(10).to_string(index=False))