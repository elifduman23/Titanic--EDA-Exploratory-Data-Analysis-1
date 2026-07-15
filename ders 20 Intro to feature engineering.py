import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None) # tüm kolonları göstermesi için
#data=pd.read_csv("titanic.csv")
data=sns.load_dataset("titanic") # seaborn kütüphanesinden titanic datasını çağırdık internet üzerinden 
print(data.head())
print(data.isnull().sum()) # boş olan dataların sayısını verir
print(data["deck"].unique()) # Deck kolonundaki unique değerleri verir
print(data.dropna().shape) # boş olan dataları siler ve kaç satır kaldığını gösterir
print(data.dropna(axis=1).shape) # boş olan kolonları siler ve kaç kolon kaldığını gösterir 

#Inputation

#Mean Inputation
sns.histplot(data=data["age"],kde=True) #datasetteki yaş dağılımının histogramını çizer
plt.show()
sns.boxplot(data=data["age"]) # datasetteki yaş dağılımının boxplotunu çizer
plt.show()
data["Age_mean"]=data["age"].fillna(data["age"].mean()) # boş olan dataları ortalama ile doldurur
print(data[["Age_mean","age"]])

#Median Inputation
data["Age_median"]=data["age"].fillna(data["age"].median()) # boş olan dataları medyan ile doldurur
print(data[["Age_median","age"]])

#Mode Inputation
data["Age_mode"]=data["age"].fillna(data["age"].mode()) # boş olan dataları mod ile doldurur
print(data[["Age_mode","age"]])

print(data[data["embarked"].isnull()]) # embarked kolonundakiboş olan dataları yazdırır
print(data["embarked"].unique()) # embarked kolonundaki unique değerleri verir
mode_value=data[data["embarked"].notna()]["embarked"].mode() # embarked kolonundaki boş olmayan dataların modunu verir
data["embarked_mode"]=data["embarked"].fillna(mode_value[0]) # embarked kolonundaki boş olan dataları mod ile doldurur
print(data[["embarked_mode","embarked"]])