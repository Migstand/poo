class Mamifero:
    def emitir_som(self):
        return None

class Gato(Mamifero):
    def emitir_som(self):
        return "Miau"
class Cachorro(Mamifero):
    def emitir_som(self):
        return "Auau"

x = Gato()
print(type(x))
print("Type")
print(type(x) == Gato)
print(type(x) == Mamifero)
print("Instance")
print(isinstance(x, Gato))
print(isinstance(x, Mamifero))
print(isinstance(x, object))
print(x.emitir_som())
y = Cachorro()
print(y.emitir_som())