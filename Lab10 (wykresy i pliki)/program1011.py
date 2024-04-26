import pandas as pd
data = pd.read_csv('jajka2024.csv', sep=';', index_col=0, encoding='UTF-8')
data2 = data.stack()
data2 = data2.apply(pd.to_numeric)
print(data2)
srednia = data2.mean()
minCena = data2.min()
maxCena = data2.max()
print(data2[data2 == minCena])
print(data2[data2 == maxCena])