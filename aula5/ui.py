import ingresso.py

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
        x = Ingresso()
        x.dia = input("Informe o dia [dom, seg, .... sab]: ")
        x.hora = int(input("Informe a hora [0-23]: "))
        print(x.dia)
        print(x.hora)
        # x.inteira() chama o método da classe e self é a instância x
        # inteira() 
        print(f"Valor do ingresso R$ {x.inteira():.2f}")
        print(f"Valor do ingresso R$ {x.meia():.2f}")
    @staticmethod
    def viagem():
        pass