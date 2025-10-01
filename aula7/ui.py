import ingresso.py

from ingresso
class UI: #interface com o usuário - não tem instância
    @staticmethod
    def main(): #método estático é um método chamado com a classe
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.ingresso() #ingresso é chamado com o class
            if op == 2: UI.Viagem()
    @staticmethod
    def menu():
        print("1-Ingresso, 2-Viagem, 3- Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def ingresso():
        d = input("Informe o dia [dom, seg, .... sab]: ")
        h = int(input("Informe a hora [0-23]: "))
        x = Ingresso(d, h) # Ingresso.__init__()
        print(x)           # Ingresso.__str__()
        # print(x.__dia) __dia não é visivel fora da classe Ingresso
        # print(x.__dia)__dia #está encapsulado (começa com __)
        
        # x.dia = input("Informe o dia [dom, seg, .... sab]: ")
        # x.hora = int(input("Informe a hora [0-23]: "))

        x.set_dia (input("Informe o dia [dom, seg, .... sab]: "))
        x.set_hora(int(input("Informe a hora [0-23]: ")))
        
        # print(x.dia)
        # print(x.hora)

        print(x.get_dia())
        print(x.get_hora())
        
        # x.inteira() chama o método da classe e self é a instância x
        # inteira() 
        
        print(f"Valor do ingresso R$ {x.inteira():.2f}")
        print(f"Valor do ingresso R$ {x.meia():.2f}")
    @staticmethod
    def viagem():
        pass

UI.main()