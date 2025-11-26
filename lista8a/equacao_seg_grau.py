class Equacao_2_Grau:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    #Set

    def set_a(self, a): 
        if a == 0: raise ValueError("Equação de primeiro grau!")
        self.__a = a
    def set_b(self, b): self.__b = b
    def set_c(self, c): self.__c = c

    #Get
    def get_a(self, a): return self.__a
    def get_b(self, b): return self.__b
    def get_c(self, c): return self.__c

    def delta(self):
        delta = (self.__b**2)- 4*(self.__a*self.__c)
        return delta
    def y(self, x):
        return ((self.__a)*(x**2)) + (self.__b*x) + self.__c
    def x1(self):
        delta = self.delta()
        if delta < 0:
            return f"{(-self.__b / (2*self.__a))} + {((-delta)**2) / (2 * self.__a)}i"
        x1 = ((self.__b*-1) + (delta**0.5))/(2*(self.__a))
        return x1
    def x2(self):
        delta = self.delta()
        if delta < 0:
            return f"{(-self.__b / (2*self.__a))} - {((-delta)**2) / (2 * self.__a)}i"
        x2 = ((self.__b*-1) - (delta**0.5))/(2*(self.__a))
        return x2
    
    def ponto_inflexao(self):
        return -self.__b/(2*self.__a)

    def __str__(self):
        return f"A = {self.__a}, B = {self.__b}, C = {self.__c}"

f = Equacao_2_Grau(1, -5, 6)
print(f.delta(), f.x1(), f.x2(), f.y(3), f)
print((f.ponto_inflexao()))

p = f.ponto_inflexao()
xmin = p - 10
xmax = p + 10
npontos = 11
dist = (xmax - xmin)/(npontos - 1)

x  = xmin
while x <= xmax:

    y = f.y(x)
    print (x, y)
    x += dist