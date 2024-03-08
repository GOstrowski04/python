########################################################################

def print_phone_numbers(slownik):
    for i in slownik:
        print(i, "ma numer", slownik[i])


numery = {"Adam": 431642950, "John": 975280155, "Bob": 729563195}
print_phone_numbers(numery)


########################################################################
def c41(dni):
    days = {"Poniedziałek": "Monday", "Wtorek": "Tuesday", "Środa": "Wednesday", "Czwartek": "Thursday",
            "Piątek": "Friday", "Sobota": "Saturday", "Niedziela": "Sunday"}
    listax = [days[x] for x in dni]
    return listax


########################################################################
def c42(dni):
    days = {"Poniedziałek": "Monday", "Wtorek": "Tuesday", "Środa": "Wednesday", "Czwartek": "Thursday",
            "Piątek": "Friday", "Sobota": "Saturday", "Niedziela": "Sunday"}
    listax = []
    for i in days:
        for j in dni:
            if j == days[i]:
                listax.append(i)
    return listax


dnitygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
print(c41(dnitygodnia))
print(c42(["Monday", "Tuesday"]))


########################################################################
def c43(miesiac):
    miesiace = {1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec",
                7: "Lipiec", 8: "Sierpień", 9: "Wrzesień", 10: "Październik", 11: "Listopad", 12: "Grudzień"}
    listax = []
    for i in miesiace:
        for j in miesiac:
            if miesiace[i] == j:
                listax.append(j)
    return listax


print(c43(["Sierpień", "Marzec", "Styczeń"]))


########################################################################


def rzymskie_na_arabskie(liczba):
    rzymskie = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    arabska = 0
    while i in range(0, len(liczba)):
        if i != len(liczba)-1 and rzymskie[liczba[i]] < rzymskie[liczba[i+1]]:
            arabska += rzymskie[liczba[i+1]] - rzymskie[liczba[i]]
            i += 1
        else:
            arabska += rzymskie[liczba[i]]
        i += 1
    return arabska


def arabskie_na_rzymskie(liczba):
    arabskie = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 'I': 1}
    rzymska = ''
    for i in arabskie:
        if liczba // i > 0:
            rzymska += (liczba // i)*arabskie[i]
        liczba = liczba % i
    return rzymska


print(rzymskie_na_arabskie('MMXXIV'))
print(arabskie_na_rzymskie(2024))

