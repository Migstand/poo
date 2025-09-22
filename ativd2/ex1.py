class Circulo:
    def __init__(self):
        self.raio = 0
    def calc_area(self):
        return self.raio*self.raio * 3.14
    def calc_circum(self):
        return 3.14*2 * self.raio

pizza = Circulo()

pizza.raio = int(input())
a = pizza.calc_area()
print(a)