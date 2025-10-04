class Conversor:
    def __init__(self, num):
        self.__num = num
    def set_num(self, num):
        if num >= 0 : self.__num = num
        else : raise ValueError("Número negativo não pode ser convertido")
    def get_num(self):
        return self.__num
    def binario(self):
        bina = self.__num
        if bina == 0 : return "0"
        
        conv = ""
        while bina > 0:
            alg = bina % 2
            conv = str(alg) + conv
            bina = bina // 2
        return conv
    def __str__(self):
        return f"Decimal = {self.__num} - Binário = {self.binario()}"

class UI:
    @staticmethod
    def main():
        x = Conversor(0)
        x.set_num(int(input()))
        print (x.binario())
        print (x)

UI.main()