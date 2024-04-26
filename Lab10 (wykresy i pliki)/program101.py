import numpy as np
import pandas as pd

data = np.genfromtxt('jajka2024.csv', delimiter=";", dtype='U16', encoding='utf8')
print(data, '\n')
df = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
df = df.apply(pd.to_numeric)
print(df, '\n')
print(df.mean().round(decimals=2))
print(list(df.stack().idxmax()))
print(list(df.stack().idxmin()))

