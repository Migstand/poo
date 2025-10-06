class Conversor:
    def __init__(self, num):
        self.__num = num
    def set_num(self, num):
        if num >= 0 : self.__num = num
        else : raise ValueError("Número negativo não pode ser convertido")
    def get_num(self):
        return self.__num
    def binario(self):
        restos = []
        n = self.__num
        while n > 0:
            restos.append(n % 2)
            n = n // 2
        bin = ""
        while len(restos) > 0:
            bin = bin + str(restos.pop())
        return bin
    
    def binario2(self):
        bin = ""
        n = self.__num
        while n > 0:
            bin = str(n % 2) + bin
            n = n//2
        return bin

class UI:
    @staticmethod
    def main():
        x = Conversor(0)
        x.set_num(int(input()))
        print (x.binario())
        print (x.binario2())
        print (x)

UI.main()