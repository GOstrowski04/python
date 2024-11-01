import numpy as np

A = np.array([[1, 1, 2], [2, 1, 0], [4, 1, 2]])
B = np.array([[2, 5, 7], [2, 8, 0], [4, 3, 1]])
print(A, '\n')
print(B, '\n\n')
print(A + B, '\n')
print(A @ B, '\n')
print(A * B, '\n\n')
print(A.T, '\n')
print(np.flip(A), '\n')
print(np.power(A, 5), '\n')
print(np.linalg.matrix_power(A, 5), '\n')
print(np.linalg.det(B))
print(np.linalg.matrix_power(B, -3), '\n')

print('#'*60, '\n')

C = np.array([[1, 2, 4]]).reshape(3, 1)
print(C, '\n')
D = np.array([[2, 5, 7]])
print(D, '\n')
print(C @ D, '\n')
print(D @ C, '\n')
print(C * D, '\n')
print(C + D, '\n')

print('#'*60, '\n')

E = np.array([[1, 5], [2, 1]])
F = np.array([[2, 1], [2, 8]])
print(E, '\n')
print(F, '\n')
print(E / F, '\n')
print(E // F, '\n')
print(E % F, '\n')
