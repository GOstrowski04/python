import math
# Ćw 1 b)
lista1 = [x**5 for x in range(0, 15)]
print(lista1)

lista2 = [math.factorial(x) for x in range(0, 20)]
print(lista2)

lista3 = [math.e**x for x in range(0, 20)]
print(lista3)

lista41 = ['kowalski', 'nowak', 'pawelczyk', 'adamczyk']
lista42 = [len(x) for x in lista41]
print(lista42)