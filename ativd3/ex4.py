class Eq_2_grau:
    def __init__ (self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def set_a(self, a):
        self.__a = a
    def set_b(self, b):
        self.__b = b
    def set_c(self, c):
        self.__c = c
    
    def get_a(self, a):
        return self.__a
    def get_b(self, b):
        return self.__b
    def get_c(self, c):
        return self.__c
    
    def delta(self):
        return ((self.__b**2) - ((self.__a*self.__c)*4))
    def raiz1(self):
        soma = (((self.__b)*(-1)) + ((self.delta())**0.5))/(2*self.__a)
        return f"{soma:.2f}"
    def raiz2(self):
        sub =(((self.__b)*(-1)) - ((self.delta())**0.5))/(2*self.__a)
        return f"{sub:.2f}"
    
    def __str__(self):
        return f"A = {self.__a} - B = {self.__b} - C = {self.__c}"

class UI:
    def main():
        x = Eq_2_grau(1,1,1)
        x.set_a(int(input()))
        x.set_b(int(input()))
        x.set_c(int(input()))
        y = x.delta()
        z = x.raiz1()
        w = x.raiz2()
        print (x)
        print (y)
        print (z)
        print (w)

UI.main()