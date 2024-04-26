import numpy as np
import pandas as pd

df1 = pd.DataFrame([[2942, 9840, 2794, 8891, 8111, 2933, 8301, 9125],
                    ['Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary',
                     'Zenon', 'Filip', 'Adrian'], [13, 31, 34, 14, 13, 28, 20, 15]]).T
df1.columns = ['ID', 'Name', 'Age']
weight = [65, 80, 64, 69, 74, 61, 66, 61]
height = [179, 179, 151, 177, 170, 157, 151, 153]
glasses = [False, True, False, True, False, True, False, True]
df2 = pd.DataFrame([[2312, 2336, 2942, 9840, 2794, 8891, 8111, 2933],
                    ['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa',
                     'Tomasz', 'Cezary', 'Zenon'], weight, height, glasses]).T
df2.columns = ['ID', 'Name', 'W', 'H', 'GL']

# 1)
df0 = pd.merge(df1, df2, on=['ID', 'Name'], how='inner')
print(df1, df2, df0, sep='\n\n')
df01 = pd.merge(df1, df2, on=['ID', 'Name'], how='outer')
print('\n', df01)

# 2)
df01 = df01.sort_values('Name')
print('\n', df01, '\n')

# 3)
df02 = (df0[df0['GL']])
print(df02, '\n')

# 4)
df03 = (df0[(df0['Age'] >= 20) & (df0['Age'] <= 30)])
print(df03, '\n')

# 5)
df0['bmi'] = (df0['W']*10000/df0['H']**2).astype(int)
print(df0, '\n')

# 6)
print(df0['Age'].mean().round(decimals=2))

# 7)
print(df0.groupby('GL')['bmi'].mean().round(decimals=2))

# 8)
print(df0.groupby('GL')['Age'].mean().astype(float).round(decimals=2))
