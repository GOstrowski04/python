import numpy as np
np.set_printoptions(suppress=True)
Panstwa = np.array(['China', 'Japan', 'Germany', 'USA', 'South Korea', 'India', "Brazil", 'Mexico', 'Spain', 'Russia'])
rok1999 = np.array([0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94])
rok2014 = np.array([19.91, 8.21, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69])

print(f'{np.round(rok2014*100/rok1999-100, 1)}')
print(Panstwa[min(rok1999) == rok1999])
print(Panstwa[rok2014 < rok1999])
