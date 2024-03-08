import math

lista = [1, 2, 3]
print(lista)
lista.append(4)
print(lista)
lista.extend([5, 6, 3, 7, 9])
print(lista)
lista.insert(0, 0)
print(lista)
lista.remove(9)
print(lista)
lista.pop(7)
print(lista)
temp = lista.copy()
print(lista)
temp.clear()
print(lista.index(5))
print(lista.count(2))