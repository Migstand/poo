class Triangulo:
    def __init__(self):
        self.b = 0                 # atributo ou campo
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2 # método

x = Triangulo()
t = Triangulo()
x.b = float(input("Informe a base do triângulo:"))
x.h = float(input("Informe a altura: "))
print("Área = ", x.calc_area())
# y = 5
# z = int()
# print(type(x))
# print(type(y))
# print(type(z))
# x.b = 10
# x.h = 20
# t.b = 30
# t.h = 40
# print(x.b, x.h)
# print(t.b,t.h)
# print(x.b * x.h / 2)
# print(t.b * t.h / 2)
# print(x.calc_area())
# print(t.calc_area())
