import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('jajka2024.csv', sep=';', index_col=0, encoding='UTF-8')
data = data.apply(pd.to_numeric)
print(data)
plot1 = data.plot(kind='box')
plt.xticks(rotation=60)
plot2 = data.T.plot(kind='box')
plt.xticks(rotation=60)
plt.show()
