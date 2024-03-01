
s = ("W Roku Pańskim 1345, władca Henryk 12, na rzecz "
     "swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków.")

suma = 0
n = 0
for i in s:
    if i.isdigit():
        n *= 10
        n += int(i)
    else:
        suma += n
        n = 0

print(suma)
