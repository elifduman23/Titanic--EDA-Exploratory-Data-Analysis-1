import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("titanic.csv")
print(data.head())
age=pd.DataFrame(data["Age"])
print(age)
name =pd.DataFrame(data["Name"])
print(name)
print(data.shape) # verinin kaç satır olduğuna bakarız.
