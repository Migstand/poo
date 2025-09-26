class Ingresso: #Entidade
    def __init__(self):
        self.__dia = "domingo"
        self.__hora = 17
    
    def get_dia(self):
        return self.__dia
    
    def get_hora(self):
        return self.__hora
    
    def set_dia(self, dia):
        if dia in ["domigo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]:
            self.__dia = dia
        else: raise ValueError("Dia inválido")

    def set_hora(self, hora):
        if self.__hora >= 0 and self.hora <=23: self.__hora = hora
        else: raise ValueError("Hora inválido")
    
    def inteira(self): #método de instância
        if self.__dia == "quarta": return 8
        if self.__dia in ["segunda", "terça", "quinta"]: valor = 16
        else: valor = 20
        if self.__hora >= 17 or self.__hora == 0: valor = valor * 1.5
        return valor
    
    def meia(self):
        if self.__dia == "quarta": return 8
        return self.inteira()/2