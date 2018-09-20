import csv
import pandas as pd
import numpy as np
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


train['weight'] = np.random.randint(0, 1000000, size=len(train))/1000000
# print(nr.randint(0, 1000000)/1000000))
umbral = nr.randint(0, 1000000)/1000000
print(train.head())
print(umbral)
i =0
print(train.tail())
for index in train.index:
    print(index)
    for col in train:
        print(train[col].loc[index])