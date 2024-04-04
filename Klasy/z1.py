class Car:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok

    def __str__(self):
        return f'{self.marka} {self.rok}'


car1 = Car('Ford', 1999)
car2 = Car('Volkswagen', 2011)
print(car1)
print(car2)
car1 = car2
print(car1)
print(car2)