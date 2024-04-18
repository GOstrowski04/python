import numpy as np
"""
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
a[[True, False, True, False]] = 0
print(a)
print(a[a > 3])
a[a > 3] = 100
print(a)
"""

my_array = np.arange(10, 39, 2)
print(my_array)

print(np.shape(my_array))
my_array = np.reshape(my_array, (1, 15))
print(np.shape(my_array))
print(my_array)

my_array += 3
print(my_array)
my_array *= 2

print(my_array)
my_array[my_array % 6 == 2] = 0
print(my_array)


def change(A, x):
    temp = np.copy(A)
    temp[temp == 0] = x
    return temp


change(my_array, 3)
print(my_array)
print(change(my_array, 3))
