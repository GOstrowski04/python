import numpy as np
import pandas as pd

#serie
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

# obliczenia na seriach
print(sr4)
print(sr1 + sr4)
print(sr1 - sr4)
print(sr1 * sr4)
print(sr1 / sr4)

sr5 = pd.Series(np.random.randint(-10, 10, 10))
print(sr5)
sr6 = sr5[sr5 < 0]
print(sr6, '\n')

# ramki danych
my_list = [1, 32, -37, 91, 12, 11, -5]
my_dict = {'a': [1, 3, 2], 'b': [2, 5, 7], 'c': [3, 4, 8], 'd': [4, 10, 12]}
my_array = np.array([[1, 2, 5], [-2, 3, 3], [5, 2, 6]])
my_series = pd.Series([1, 32, -37, 91, 12, 11, -5], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
df1 = pd.DataFrame(my_list, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'], columns=['liczby'])
df2 = pd.DataFrame(my_dict, index=[1, 2, 3])
df3 = pd.DataFrame(my_array, index=[1, 2, 3], columns=['a', 'b', 'c'])
df4 = pd.DataFrame(my_series)
print(df1, df2, df3, df4, sep='\n\n')

my_list2 = df1.values.tolist()
my_dict2 = df2.to_dict()
my_array2 = df3.to_numpy()
my_series2 = df4.squeeze()
print(my_list2, my_dict2, my_array2, my_series2, sep='\n\n')

df5 = pd.DataFrame({'a': [1, -3, 2], 'b': [2, 8, -5], 'c': [4, 0.5, 7], 'd': [5, 10, 3]}, index=['l1', 'l2', 'l3'])
print(df5, '\n')

# wyciąganie elementów
print(df5.iloc[0:2], '\n')
print(df5.iloc[:, [0, 2]], '\n')
print(df5.iat[1, 0])

# sortowanie kolumną
df5 = df5.sort_values('a')
print(df5)
