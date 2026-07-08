import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("titanic.csv")
print(data.head())
age=pd.DataFrame(data["Age"]) #Age kolonundaki verileri age değişkenine atadık ve dataframe yaptık
print(age)
name =pd.DataFrame(data["Name"])
print(name)
print(data.shape) # verinin kaç satır olduğuna bakarız.
plt.hist(age) #yolcuların yaş dağılımını histogram ile gösterir
plt.show()
plt.hist(data["Fare"]) # yolcuların ödedikleri ücretin dağılımını histogram ile gösterir
plt.show()
print(data.columns) # kolonların isimlerini verir
plt.boxplot(data["Fare"].dropna()) # ücretin dağılımını boxplot ile gösterir
plt.show()
plt.boxplot(data["Age"].dropna()) # yaşın dağılımını boxplot ile gösterir
plt.show()