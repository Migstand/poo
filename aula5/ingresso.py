class Ingresso: #Entidade
    def __init__(self):
        self.__dia = ""
        self.__hora = 0
    def inteira(self): #método de instância
        if self.__dia == "quarta": return 8
        if self.__dia in ["segunda", "terça", "quinta"]: valor = 16
        else: valor = 20
        if self.__hora >= 17 or self.__hora == 0: valor = valor * 1.5
        return valor
    def meia(self):
        if self.__dia == "quarta": return 8
        return self.inteira()/2