# cargar un archivo csv en una estructura de datos
import pandas as pd



# cargar un archivo csv en una matriz

data=pd.read_csv("ejemplocsv.csv",header=None)

list=data.values.tolist()

print(list)


# cargar un archivo csv en un diccionario

df = pd.read_csv("ejemplocsv.csv", sep=";")

print(df)




