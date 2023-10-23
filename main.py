from string import *
from random import *
from time import *
from tkinter import *
# Wypisz sumę pierwszych dziesięciu liczb naturalnych
suma = 0
for i in range(1, 11):
    suma += i
print(suma)
# Suma kwadratów liczb od 1 do 100 (włącznie)
suma = 0
for i in range(1, 101):
    suma += pow(i, 2)
print(suma)


class App(Tk):

   def __init__(self):
      super().__init__()
      self.geometry("600x600")


app = App()
app.mainloop()
"""
for i in range(0,10) :
    sleep(1)
    print(i)
"""
"""
a1 = []
plik1 = open("test.txt")
for i in plik1:
    a1.append(int(i))
plik1.close()
a1.reverse()
plik1 = open("test2.txt", "w+")
for i in a1:
    plik1.write(str(i))
    plik1.write('\n')
for i in range(1, 106):
    plik1.write(choice(ascii_letters))
    if i % 15 == 0: plik1.write('\n')
"""