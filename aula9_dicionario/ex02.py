class Aluno:
    def __init__(self, nome, matricula, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade

a = Aluno("Raquel", "20251014040000", 20)
b = Aluno("Miguel", "20251014040001", 18)

print(a.__dict__) #__dict__ é o atributo que mostra as variáveis 
print(vars(b)) #vars é uma função que mostra as variáveis

x = vars(b)
for item in x.items():
    print(item, type(item))