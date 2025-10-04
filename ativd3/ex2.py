class Frete:
    def __init__(self, d, p):
        self.__d = d
        self.__p = p
    def set_distancia(self, d):
        if d >= 0 : self.__d = d
        else : raise ValueError("Distância invalida")
    def set_peso(self, p):
        if p >= 0 : self.__p = p
        else : raise ValueError("Peso invalido")
    def get_distancia(self):
        return self.__d
    def get_peso(self):
        return self.__p
    def calc_frete(self):
        return f"{self.__p/self.__d} centavos"
    def __str__(self):
        return f"Distância = {self.__d} - Pese = {self.__p}"

class UI:
    @staticmethod
    def main():
        x = Frete(0,0)
        x.set_distancia(int(input()))
        x.set_peso(int(input()))
        y = x.calc_frete()
        print(x)
        print(y)

UI.main()