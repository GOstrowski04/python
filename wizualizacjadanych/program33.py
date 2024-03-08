def c11(tuple1, e):
    x = (e,)
    tuple1 += x
    return tuple1


def c12(tuple2, e):
    x = list(tuple2)
    x.append(e)
    tuple2 = tuple(x)
    return tuple2


def c13(tuple3, e):
    x = list(tuple3)
    x.remove(e)
    tuple3 = tuple(x)
    return tuple3


tup1 = 1, 3, 'tekst'
tup2 = 1, 3, 'abc'
print(c11(tup1, 'abc'))
print(c12(tup1, 'abc'))
print(c13(tup2, 'abc'))

##################################################################


def c21(lista):
    return list(set(lista))


def c22(lista):
    return tuple(set(lista))


lista1 = [1, 2, 4, 6, 2, 1, 7, 3]
print(c21(lista1))
print(c22(lista1))
