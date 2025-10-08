class Cliente:
    def __init__(self, nome, limite):
        self.set_nome(nome)
        self.set_limite(limite)
        self.__socio = None
    
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
   
    def set_limite(self, limite):
        self.__limite = limite
    def get_limite(self):
        return self.__limite
    def get_limite_sociedade(self):
        if self.__socio == None:
            return self.__limite
        else:
            return self.__limite + self.__socio.__limite

    def set_socio(self, socio):
        c1 = self
        c2 = self.__socio
        c3 = socio
        c4 = socio.__socio
        
        if c2 != None: c2.__socio = None
        if c4 != None: c4.__socio = None
        
        # self.__socio = socio
        # socio.__socio = self
        c1.__socio = c3
        c3.__socio = c1

    def get_socio(self):
        return self.__socio
    
    def __str__(self):
        if self.__socio == None:
            return f"{self.__nome} {self.__limite} {self.get_limite_sociedade()}"
        else :
            return f"{self.__nome} {self.__limite} {self.__socio.__nome} {self.get_limite_sociedade()}"


class UI:
    @staticmethod
    def main():
        a = Cliente("Alex", 1000)
        b = Cliente("Marília", 1500)
        c = Cliente("Eduardo", 2000)
        d = Cliente("Silvia", 2500)
        
        a.set_socio(b)
        d.set_socio(c)

        print(a)
        print(b)
        print(c)
        print(d)

        a.set_socio(c)
        
        print("")
        print(a)
        print(b)
        print(c)
        print(d)
        
UI.main()