class Retangulo:
    def __init__(self, b, h):
        self.__b = b
        self.__h = h
    def set_base(self, b):
        if b >= 0: self.__b = b
        else : raise ValueError()
    def set_altura(self, h):
        if h >= 0: self.__h = h
        else : raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h
    def calc_diagonal(self):
        d = ((self.__b*self.__b) + (self.__h*self.__h))**0.5
        return d
    def __str__ (self):
        return f"Base = {self.__b} - Altura = {self.__h}"

class UI:
    @staticmethod
    def main():
        x = Retangulo(3,4)
        x.set_base(int(input()))
        x.set_altura (int(input()))
        y = x.calc_area()
        z = x.calc_diagonal()
        print(x)
        print(y)
        print(z)        

UI.main()