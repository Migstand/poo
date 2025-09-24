class Entrada:
    def __init__(self):
        self.dia = ""
        self.hora = 0
    def valor(self):
        dias = ["segunda","terça","quarta","quinta","sexta","sábado","domingo"]
        if self.hora < 17 and self.hora > 0:
            if self.dia == dias[2]:
                return 8.00
            if self.dia in dias[:2] or self.dia == dias[3]:
                return 16.00
            if self.dia in dias[4:]:
                return 20.00
        else:
            if self.dia == dias[2]:
                return 12.00 
            if self.dia in dias[:2] or self.dia == dias[3]:
                return 24.00
            if self.dia in dias[4:]:
                return 30.00

inter = Entrada()
inter.dia = input()
inter.hora = int(input())
valor = inter.valor()
print(valor)