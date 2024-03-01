

def parzyste(s):
    return s[0::2]


def ostatnieznaki(s, n):
    n *= -1
    return s[n:]


def odwrocenie(s):
    return s[::-1]


def palindrom(s):
    if s == s[::-1]:
        return True
    return False


def porownanie(s1, s2):
    if s1 > s2:
        return 1
    elif s1 < s2:
        return 2
    else:
        return "Są równe."


def imieidata(imie, data):
    s = 'My name is {0}. My date of birth is {1}.'.format(imie, data)
    return s


print(parzyste("abcdefg"))
print(ostatnieznaki("abcdefg", 3))
print(odwrocenie("abcdefg"))
print(palindrom("abcdcba"))
print(porownanie("abcd", "abc"))
print(imieidata("ABCDEFG", "19.11.2004"))
