import math
# math
# a)


def reszta(x, y):
    if isinstance(x, float) or isinstance(y, float):
        return math.fmod(x, y)
    elif isinstance(x, int) and isinstance(y, int):
        return x % y


def logarytm(a, n):
    for k in range(2, n+1):
        print(math.log(a, k), end='|')


def c1a4(a):
    lista = [math.exp(a), math.e**a, math.pow(math.e, a)]
    return lista

# b)


print(12 ** 50)
print(math.pow(12, 50))

print(3 % 4)
print(math.remainder(3, 4))

print(math.cosh(5))
print((math.pow(math.e, 5) + math.pow(math.e, -5))/2)

print(math.sinh(5))
print((math.pow(math.e, 5) - math.pow(math.e, -5))/2)

# string
s = "qwertyuiopasdfghjklzxcvbnm"
print(s[12])
print(s*2)
print(s+'qwe')
print(len(s))
