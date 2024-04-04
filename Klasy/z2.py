class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f'Kolor = {self.color}\nWaga = {self.weight}'

    def isfresh(self):
        if self.color in {'czarny', 'brązowy'}: return False
        return True


class Apple(Fruit):
    def __init__(self, weight, color="czerwony"):
        super().__init__(weight, color)
        self.color = color
        self.weight = weight


class Banana(Fruit):
    def __init__(self, weight, color="żółty"):
        super().__init__(weight, color)
        self.color = color
        self.weight = weight


class Orange(Fruit):
    def __init__(self, weight, color="pomarańczowy"):
        super().__init__(weight, color)
        self.color = color
        self.weight = weight


a = Apple(10)
b = Banana(15)
c = Orange(12)
print(a)
print(b)
print(c)

