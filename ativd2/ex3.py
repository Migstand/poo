class Conta:
    def __init__(self):
        self.titular = ""
        self.numero = ""
        self.saldo = 0
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor


x = Conta() #uma instância
print(x.titular, x.numero, x.saldo)
x.titular = "Raquel"
x.numero = "123-x"
x.saldo = 1000
print(x.titular, x.numero, x.saldo)
x.depositar(500)
print(x.titular, x.numero, x.saldo)

y = Conta() #outra instância
y.titular = "Thiago"
y.numero = ""
y.saldo = 2000
print(y.titular, y.numero, y.saldo)
y.depositar(300)
print(y.titular, y.numero, y.saldo)