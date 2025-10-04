class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    def set_dia(self, dia):
        if self.__mes == 2:
            if self.__ano == 