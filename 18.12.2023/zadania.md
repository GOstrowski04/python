# Zadanie 3
```python
f = open("plik.txt", 'r')
tekst = f.readlines()
for i in range(len(tekst)):
    tekst[i] = tekst[i].strip()
print(tekst)
d = {}
for i in tekst:
    for j in i:
        if j.isalpha():
            if j not in d:
                d[j] = 0
            d[j] += 1
print(d)
```
# Zadanie 4
```python
f = open("plik.txt", 'r')
x = {}
for line in f:
    words = line.split()
    for word in words:
        if word.isnumeric():
            if word not in x:
                x[word] = 0
            x[word] += 1
print(x)
```
# Weryfikacja hasła
```python
def weryfikacja(haslo):
    duzalitera = False
    cyfra = False
    for i in haslo:
        if i.isupper():
            duzalitera = True
        if i.isnumeric():
            cyfra = True
    if duzalitera and cyfra:
        print("Hasło jest poprawne.")
        return True
    print("Hasło nie jest poprawne.")
    return False


password = "Abcdefg1"
weryfikacja(password)
```
# Choinka
```python
def choinka (h):
    if h <= 2:
        return False
    for i in range(0, h):
        print(' ' * (h - i), '*' + '*'*i*2)
    print(' ' * h, '*')


h = 10
choinka(h)
```
# Pusty trójkąt
```python
def pustytrojkat(h):
    for i in range(h):
        print(' ' * (h - i), end="")
        lista = []
        for x in range(1+2*i):
            lista.append(x)
        for j in lista:
            if i == h-1 or j == lista[0] or j == lista[len(lista)-1]:
                print('*', end="")
            else:
                print(' ', end="")
        print('\n', end="")


pustytrojkat(10)
```
