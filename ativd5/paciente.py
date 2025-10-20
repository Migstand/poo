from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def idade(self):
        c = datetime.strptime(self.__nascimento, "%d/%m/%Y")
        d = c.now()
        return (d - c)

    def set_nome(self, nome):
        self.__nome = nome
        #else: raise ValueError("Digite um nome válido")
    def get_nome(self):
        return self.__nome
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
        # if  == str: self.__nome = nome
        # else: raise ValueError("Digite um nome válido")
    def get_cpf(self):
        return self.__cpf
    
    def set_telefone(self, telefone):
        self.__telefone = telefone
        # else: raise ValueError("Digite um nome válido")
    def get_telefone(self):
        return self.__telefone
    
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento
        # else: raise ValueError("Digite um nome válido")
    def get_nascimento(self):
        return self.__nascimento

    def __str__(self):
        return f"{self.__nome}, {self.__cpf}, {self.__telefone}, {self.__nascimento}"
    
class UI:
    def main():
        paci = Paciente(input(), input(), input(), input())
        print(paci.idade())
        print(paci)

UI.main()