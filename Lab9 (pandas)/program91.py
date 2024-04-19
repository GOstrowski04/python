import numpy as np
import pandas as pd

sr1 = pd.Series({'A': 1, 'B': 2, 'C': 3})
print(sr1)

sr2 = pd.Series({1: 'abc', 2: 'baab', 3: 'vns'}, index=[1, 2, 3])
print(sr2)

lista1 = [1, 4, 5, 2, 6]
sr3 = pd.Series(lista1)
print(sr3)

lista2 = sr1.values.tolist()
print(lista2)

listanp = np.array([1, 2, 3])
print(listanp)
sr4 = pd.Series(listanp, index=['A', 'B', 'C'])
print(sr4)
print(sr1 + sr4)
print(sr1 - sr4)
print(sr1 * sr4)
print(sr1 / sr4)
sr5 = pd.Series(np.random.randint(-10, 10, 10))
print(sr5)
