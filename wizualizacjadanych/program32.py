import math

##########################################################################


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list3 = [list1[x] + list2[x] for x in range(len(list1))]
print(list3)


##########################################################################


def numermiesiaca(miesiac):
    miesiace = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
                "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    return miesiace.index(miesiac)


list4 = ["Luty", "Styczeń", "Grudzień", "Kwiecień", "Listopad", "Wrzesień", "Lipiec", "Sierpień", "Czerwiec",
         "Październik", "Maj", "Marzec"]

list4.sort(key=numermiesiaca)
print(list4)


##########################################################################


def c3(lista, litera):
    listax = [x for x in lista if x[0].lower() > litera.lower()]
    return listax


nazwiska = ["Kowalski", "Adamczyk", "Nowak", "Fedorczyk"]
print(c3(nazwiska, 'f'))


###########################################################################


def c4(lista):
    listax = [x for x in lista if len(x) > 6]
    return listax


print(c4(nazwiska))


###########################################################################


def c5(lista):
    listax = lista.copy()
    listax.sort(reverse=True)
    if lista == listax:
        return True
    return False


print(c5([5, 7, 3, 5, 1, 4, 7]))
print(c5([9, 6, 4, 2, 1]))


###########################################################################


def c6(lista):
    listax = [x**3 for x in lista]
    return listax


print(c6([1, 2, 3, 4, 5]))


###########################################################################


def func(lista, n1, n2):
    listax = [x if x != n1 else n2 for x in lista]
    return listax


print(func([2.5, 1.7, 3.8, 1.7], 1.7, 3.4))


###########################################################################


def func2(lista, n1, n2):
    listax = [x if not math.isclose(x, n1, abs_tol=0.01) else n2 for x in lista]
    return listax


print(func2([2.5, 1.7, 3.8, 1.7], 1.702, 3.4))
