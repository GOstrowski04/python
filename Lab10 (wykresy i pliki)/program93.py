f = open('tekst1.txt', 'r+', encoding='utf8')
s = f.read()
f.close()
print(s)
print(type(s))

# inny sposób

with open('tekst1.txt', 'r+', encoding='utf8') as f:
    f.write('namb\n')
    f.seek(8)
    f.write(' (dodany tekst) ')
    print(s)

