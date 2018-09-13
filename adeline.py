
import csv
import pandas as pd


with open("DatosPracticaEnergia1.txt") as f:
    reader = csv.reader(f)
    data1 = [r for r in reader]

# Crea un dataframe con pandas con la información original, con las columnas: counterinfo_id, timestamp y consumption
txtdata = pd.read_csv('DatosPracticaEnergia1.txt', sep=' ')
print(txtdata.head())
# 767
datos = txtdata.loc[:"V4052"]

print(datos.tail())
validacion = txtdata.loc["V4053":"V4380"]
print(validacion.head())
print(validacion.tail())
test = txtdata.loc["V4381":]
print(test.head())
print(test.tail())

# print(datos.tail())
# print(validacion.head())
# print(validacion.tail())
# print(test.head())
