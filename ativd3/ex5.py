class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    def set_data(self, data):
        self.__data = data
        self.__dia, self.__mes, self.__ano = map(int,self.__data.split("/"))
        m = self.__mes//8
        d = m + 30
        if self.__mes == 2:
            if (self.__ano%400 == 0) or ((self.__ano%4 == 0) and (self.__ano % 100 != 1)):  d = 29
            else: d = 28
        if self.__dia > d or self.__dia < 1: raise ValueError ("Digite um dia válido")
        if self.__mes < 1 or self.__mes > 12: raise ValueError("Digite um mês válido")
        if self.__ano < 1: raise ValueError("Digite um ano depois de cristo")
    def get_dia(self):
        return self.__dia
    def get_mes(self):
        return self.__mes
    def get_ano(self):
        return self.__ano
    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"

class UI:
    def main():
        data = Data(1, 1, 1)
        data.set_data(input("Informe uma data no formato dd/mm/aaaa"))
        print(data)

UI.main()