Na spoj wejść i zrobić zadania 2
# Zadanie 1
### a) napisać funkcję która pobiera jako argument łańcuch znaków i zwraca jako wynik słownik ze znakami jako kluczem z przypisaną ilością wystąpień
```python
def znaki(slowo):
    d = {}
    for z in slowo:
        if z not in d:
            d[z] = 0
        d[z] += 1
    return d
```
### b) Słownik zawierający informację ile razy każda litera (nie wszystkie znaki!) występuje w łańcuchu podanym jako argument o ile w nim występuje chociaż raz
```python
def litery(slowo):
    d = {}
    for z in slowo:
        if z in s.ascii_letters:
            if z not in d:
                d[z] = 0
            d[z] += 1
    return d
```
### c) tak jak wyżej ale bez rozróżniania na małe i duże
```python
def literywszystkie(slowo):
    d = {}
    slowo = slowo.lower()
    for z in slowo:
        if z in s.ascii_letters:
            if z not in d:
                d[z] = 0
            d[z] += 1
    return d
```
