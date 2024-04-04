def zamiana_na_rzymskie(x):
    if x >= 4000:
        print("Liczba poza zakresem.")
        return
    s = ''
    liczby = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
              5: 'V', 4: 'IV', 1: 'I'}
    for i in liczby:
        if x / i >= 1.0:
            y = int(x / i)
            for j in range(0, y):
                s += liczby[i]
                x -= i
    return s


def zamiana_na_arabskie(z):
    wartosci = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = z[::-1]
    liczba = 0
    temp1 = 0
    for i in s:
        temp2 = wartosci[i]
        if temp2 < temp1:
            liczba -= temp2
        else:
            liczba += temp2
        temp1 = temp2
    return liczba


class Romanian:
    def __init__(self, rzymska):
        self.rzymska = rzymska

    def dodawanie(self, other):
        x = zamiana_na_arabskie(self.rzymska)
        y = zamiana_na_arabskie(other.rzymska)
        return zamiana_na_rzymskie(x + y)

    def odejmowanie(self, other):
        x = zamiana_na_arabskie(self.rzymska)
        y = zamiana_na_arabskie(other.rzymska)
        return zamiana_na_rzymskie(x - y)

    def mnozenie(self, other):
        x = zamiana_na_arabskie(self.rzymska)
        y = zamiana_na_arabskie(other.rzymska)
        return zamiana_na_rzymskie(x * y)


r1 = Romanian('VII')
r2 = Romanian('CXVII')
print(zamiana_na_rzymskie(1000))
print(r1.dodawanie(r2))
print(r2.odejmowanie(r1))
print(r1.mnozenie(r2))
