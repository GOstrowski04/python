def zamiana_na_rzymskie(x):
    if x >= 4000:
        print("Liczba poza zakresem.")
        return
    s = ''
    liczby = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
              5: 'V', 4: 'IV', 1: 'I'}
    for i in liczby:
        if x % i == 0:
            s += liczby[i]*(x/i)
    return s

class Romanian:
    def __init__(self, rzymska):
        self.rzymska = rzymska

    def zamiana_na_arabskie(self):
        wartosci = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = self.rzymska[::-1]
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

r1 = Romanian('VII')
print(r1.zamiana_na_arabskie())
