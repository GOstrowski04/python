```python
from math import *
# Zadanie 1
# a)
def NWD(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def wzajemniepierwsze(n):
    lista1 = []
    for i in range(1, n):
        if NWD(i, n) == 1:
            lista1.append(i)
    return lista1


# b)
def doskonala(n):
    y = 0
    for i in range(1, n):
        if n % i == 0:
            y += i
    if n == y:
        return True
    return False


# c)
def pierwsza(n):
    if n == 2:
        return True
    for i in range (2, n):
        if n % i == 0:
            return False
    return True


def pierwszepoddzielniki(n):
    lista1 = []
    for i in range(1, n):
        if n % i == 0 and pierwsza(i) == True :
            lista1.append(i)
    return lista1


# d)
def fibonacci(n):
    i = 0
    j = 1
    if n == 1:
        return 0
    while True:
        if (i + j) >= n:
            if i > j:
                return i
            return j
        if i < j:
            i += j
        else:
            j += i


# e)
def sumaKwadratow(n):
    for a in range(0, floor(n**0.5) + 1):
        for b in range(0, floor(n**0.5) + 1):
            for c in range(0, floor(n**0.5) + 1):
                if a*a + b*b + c*c == n:
                    return [a, b, c]
    return False


def wszystkieSumyKwadratow(n):
    lista = []
    for a in range(0, floor(n**0.5) + 1):
        for b in range(0, floor(n**0.5) + 1):
            for c in range(0, floor(n**0.5) + 1):
                if a*a + b*b + c*c == n:
                    lista.append([a, b, c])
    return lista


print(doskonala(6))
print(wzajemniepierwsze(35))
print(pierwszepoddzielniki(15))
print(fibonacci(5000))
print(sumaKwadratow(6))
print(wszystkieSumyKwadratow(6))
```
