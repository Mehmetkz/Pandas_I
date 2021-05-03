import pandas as pd
import numpy as np

pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr',False)

tips_df = pd.read_csv("Hafta-03/tips.csv")
tips_df = pd.read_csv("Hafta-03/tips_II.csv",sep=";")

# ilk 100 satır
tips_df100 = pd.read_csv("Hafta-03/tips.csv",nrows=100)

# 100-150 satırları arası
tips_df100_150 = pd.read_csv("Hafta-03/tips.csv",skiprows=100,nrows=50, header=None)\

diabetes = pd.read_csv("Hafta-03/diabetes.csv")
diabetes.isnull().sum()
# 0 olan değerler na olarak tanıtılır.
diabetes = pd.read_csv("Hafta-03/diabetes.csv", na_values={"Glucose": 0,"BloodPressure":0,"SkinThickness":0,"Insulin":0,"BMI":0})
flights = pd.read_csv("Hafta-03/flights.csv")

# değişken türünü değiştirme int64:str
flights.dtypes
flights = pd.read_csv("Hafta-03/flights.csv", dtype={"year":str})

online_retail = pd.read_excel("Hafta-03/online_retail_GER.xlsx")
online_retail = pd.read_excel("Hafta-03/online_retail_GER.xlsx",usecols="B:E,G")

online_retail_2009_2010 = pd.read_excel("Hafta-03/online_retail_GER.xlsx",sheet_name="Year 2009-2010")

online_retail_2010_2011 = pd.read_excel("Hafta-03/online_retail_GER.xlsx",sheet_name="Year 2010-2011")

online_retail_all = pd.concat([online_retail_2009_2010,online_retail_2010_2011])

# iki veri setini de alt alta döndürür.
pd.read_excel("Hafta-03/online_retail_GER.xlsx",sheet_name=None).items()

# Birçok dataframe birleştirmek
for sheet_name, frame in pd.read_excel("Hafta-03/online_retail_GER.xlsx",sheet_name=None).item():
    frame["Year"] = sheet_name
    online_retail_all_new = online_retail_all_new.append(frame)

# Listeden Seri Oluşturma
sayilar = list(np.random.randint(10,20,10))
numpy_dizi = np.random.randint(10,30,10)
pandas_seri = pd.Series(sayilar)
pandas_seri2 = pd.Series(sayilar,index=[2,3,4,5,6,7,8,9,0,1])

# Sözlükten Seri Oluşturma

sozluk = {"5":41,
          "4":11,
          "6":42,
          "7":44,
          "8":65,
          "9":76,
          "12":51,
          "32":71,}
pandas_seri3 = pd.Series(sozluk)

# Veri Setinden Seri Oluşturma
diabetes2 = pd.read_csv("Hafta-03/diabetes.csv",nrows=30)
diabetes2_Glukoz = diabetes2["Glucose"]
diabetes2_BloodPressure = diabetes2["BloodPressure"]
type(diabetes2_Glukoz)

# Seri Özellikleri
diabetes2_BloodPressure.axes # index bilgisi verir.
diabetes2_BloodPressure.dtypes # Sutün veri tipi
diabetes2_BloodPressure.size # Seri boyutu
diabetes2_BloodPressure.shape # Serishape
diabetes2_BloodPressure.ndim # Seri boyutu
diabetes2_BloodPressure.values # Seri değerleri array hali
list(diabetes2_BloodPressure.items())

# Seri Özellikleri Fonksiyon
def seri_kontrol(series:pd.Series):
    print(str(series.name).upper().center(50,"#"))
    print(" - Index Bilgisi - ".center(50,"*"))
    print(series.axes)
    print(" - Tip Bilgisi - ".center(50,"*"))
    print(series.dtype)
    print(" - Toplam Eleman Sayısı - ".center(50, "*"))
    print(series.size)
    print(" - Toplam Boyut - ".center(50, "*"))
    print(series.ndim)
    print(" - Seriye ait index - ".center(50, "*"))
    print(series.keys())
    print(" - Seriye ait değerler - ".center(50, "*"))
    print(series.values)
    print(" - Seriye ait index, değer çifti - ".center(50, "*"))
    print(list(series.items()))
    print(" - İlk 5 Gözlem - ".center(50, "*"))
    print(series.head())
    print(" - Son 5 Gözlem - ".center(50, "*"))
    print(series.tail())


for seri in [diabetes2_BloodPressure,diabetes2_Glukoz]:
    seri_kontrol(seri)

# Eleman İşlemleri
sayi = list(np.random.randint(10,60,10))
pandas_seri4 = pd.Series(sayi,index=[1,2,3,4,5,6,7,8,9,0])

# Seri içinde eleman sorgulama
1 in pandas_seri4

# Seri içinde eleman çağırma
pandas_seri4.loc[4:8]

# Fancy index
pandas_seri4[[3,4,8]]

# index değerlerine koşul atama
pandas_seri4 > 30 # True - False
pandas_seri4[(pandas_seri4 > 30)] # True olan değerler

# DataFrame - Yapılandırılmış Veri Formu
# Listeden DataFrame Oluşturma
liste = [12,32,43,54,65,77,23,12,13,41]
list_df = pd.DataFrame(liste, columns=["Değişken"])

# Numpy Array ile Oluşturma
matris = np.random.randint(10,40,9).reshape(3,3)
matris_df = pd.DataFrame(matris,columns=["1","2","3"])

# Sözlükten dataframe Oluşturma
değişken_ismi = ["var1","var2","var3"]
deger = [np.random.randint(10,size = 5) for i in range(3)]
sozluk = dict(zip(değişken_ismi,deger))
dict_df = pd.DataFrame(sozluk)

# Seriden dataframe oluşturma
seri = pd.Series(liste)
seri_df = pd.DataFrame(seri,columns=["seri"])

# DataFrame Özellikleri Fonksiyon
def dataframe_kontrol(dataframe:pd.DataFrame):
    print(" - Satır Bilgisi - ".center(50,"*"))
    print(dataframe.index)
    print(" - Sutun Bilgisi - ".center(50,"*"))
    print(dataframe.columns)
    print(" - Tip Bilgisi - ".center(50, "*"))
    print(dataframe.dtypes)
    print(" - Satır ve Sutun Sayısı - ".center(50, "*"))
    print(dataframe.shape)
    print(" - Toplam Eleman Sayısı - ".center(50, "*"))
    print(dataframe.size)
    print(" - Toplam Boyut - ".center(50, "*"))
    print(dataframe.ndim)
    print(" - İlk 5 Gözlem - ".center(50, "*"))
    print(dataframe.head())
    print(" - Son 5 Gözlem - ".center(50, "*"))
    print(dataframe.tail())
    print(" - Metadata - ".center(50, "*"))
    print(dataframe.info())
    print(" - Boş Gözleme Ait Değişkenler - ".center(50, "*"))
    print(dataframe.isnull().sum())

diabetes = pd.read_csv("Hafta-03/diabetes.csv")
dataframe_kontrol(diabetes)

# Veri setinde eleman işlemleri
df = tips_df

# 10 ile 30. satırlar arası ekrana yazdırmak
df[10:30]

# day ve time değişkenlerini getirmek
df[["smoker","time"]]

# 10. satırdan 30.satıra kadar tip değişkeni
df[10:30]["tip"]

# 12.satırdan 22. satıra kadar tip,time ve day değişkenleri
df[12:22][["tip","time","day"]]

# üstteki senaryoyu loc ifadesi ile gösterimi
# df.loc[satır,sutun]
df.loc[12:22,["tip","time","day"]] # 22.satır yok

# üstteki senaryonun iloc ile gösterimi
# sutun değerleri sayısal olarak gösterilir.
# Satır ifadesi son satırı dahil etmez
df.iloc[12:23,[1,4,5]]

# Enumerate
df.columns
for col in enumerate(df.columns):
    print(col)

# Time değeri dinner olan satırlar
df[df["time"] == "Dinner"]

# time değeri Lunch ve day değeri sat olan ifadeler
(df["time"] == "Lunch") & (df["day"] == "Sat")
# yukarıdaki ifade true ve false döndürür. Tekrar df içine alırsak true değerleri ekrana gelir.
df[(df["time"] == "Lunch") & (df["day"] == "Sat")]

# day değeri Fri olan smoker ve tip ifadeleri
df.loc[df["day"] == "Fri", ["smoker","tip"]]

# Smoker değeri yes ve size değeri 4 den büyük olan
df[(df["smoker"] == "Yes") & (df["size"] > 4)]

# Smoker değeri no ve size değeri 4 den küçük olan tip ve tootal_bill sutunları
df.loc[(df["smoker"] == "No") & (df["size"] > 4),["tip","total_bill"]]

try_df = df.loc[(df["smoker"] == "No") & (df["size"] > 4),["tip","total_bill"]]
try_df["tip"].unique()
df["size"].unique()

