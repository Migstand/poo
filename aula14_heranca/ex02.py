class Funcionario:
    def __init__(self, nome, salario_base):
        self._salariobase = salario_base        #PRIVATE
        self.__nome = nome                      #PRIVATE
    def get_nome(self):
        return self.__nome
    def get_salario(self):
        return self._salariobase
    def __str__(self):
        return f"{self.__nome} recebe {self.get_salario()} reais"

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, gratificacao):
        super().__init__(nome, salario_base)
        self.__gratificacao = gratificacao
    def get_salario(self):
        return self._salariobase + self.__gratificacao

x = Funcionario("Eduardo", 1000)
print(x)
print(x.get_nome(), x.get_salario())

y = Gerente("Alessandro", 1000, 500)
print(y)
print(y.get_nome(), x.get_salario())