import math


def silnia(n):
    x = 1
    for i in range(2, n+1):
        x *= i
    return x


def c6a(n):
    if not (0 < n < 100):
        print("n is too large.")
        return 0
    for i in range(0, n+1):
        for j in range(0, n+1):
            print(i, ' x ', j, ' = ', i*j)


def c6b(a, b):
    if math.gcd(a, b) == 0:
        return 0
    p = a//math.gcd(a, b)
    q = b//math.gcd(a, b)
    print(p, ', ', q)


def c6c(n):
    if n == 0:
        return 0
    e1 = (1 + 1/n)**n
    e2 = 0
    for k in range(0, n+1):
        e2 += (1/silnia(k))
    print(e1, ' ', e2)
    print('e1 - math.e = ', e1 - math.e)
    print('e2 - math.e = ', e2 - math.e)
    print('|e1 - math.e| = ', abs(e1 - math.e))
    print('|e2 - math.e| = ', abs(e2 - math.e))


def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


c6a(5)
c6b(2, 10)
c6c(1)
c6c(5)
c6c(10)
print(nwd(60, 24))
