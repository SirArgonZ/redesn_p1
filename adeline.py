import csv
import pandas as pd
import random as nr
def normalizacion():
    print("")

with open("DatosPracticaEnergia1.txt") as f:
    reader = csv.reader(f)
    data1 = [r for r in reader]

# Crea un dataframe con pandas con la información original, con las columnas: counterinfo_id, timestamp y consumption
txtdata = pd.read_csv('DatosPracticaEnergia1.txt', sep=' ')
# print(txtdata.head())
# Selects 1095 rows from the original dataframe
datos = txtdata.loc[:"V438"]
# test data from 2008
test = txtdata.loc["V4381":]
# 766
train = datos.sample(frac=0.7)
# 329
validation = datos.drop(train.index)
print(train.head())
print(validation.head())
print(len(train.index))
print(len(validation.index))



# print(test.head())
# print(test.tail())
min = []
max = []
# Normalization
for column in datos:
    minparcial = train[column].min()
    min.append(minparcial)
    maxparcial = train[column].max()
    max.append(maxparcial)


for column in datos:
    train[column] = (train[column]-train[column].min())/(train[column].max()-train[column].min())

print(train.head())
print(nr.randint(0,10)/10)
