class Equacao_2_Grau:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    #Set

    def set_a(self, a): self.__a = a
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
        x1 = ((self.__b*-1) + (delta**0.5))/2
        return x1
    def x2(self):
        delta = self.delta()
        x2 = ((self.__b*-1) - (delta**0.5))/2
        return x2

    def __str__(self):
        return f"A = {self.__a}, B = {self.__b}, C = {self.__c}"