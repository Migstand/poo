import 
from models import categoria.py 
class UI:
    
    def menu():
        print()
        print()
        print()
        print()
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Fim")
        return int(input("Informe uma opção: "))
    
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()

    def inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        c = Cliente(id, nome)
        ClienteDAO.inserir(c) #instanciar DAO vai criar várias listas de clientes
        dao.inserir(c)

    def listar():
        for obj in ClienteDAO.listar():
            print(obj)
    def atualizar():
        UI.listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        c = Cliente(id, nome)
        ClienteDAO.atualizar()
    def excluir():
        UI.listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = ""
        c = Cliente(id, nome)
        ClienteDAO.excluir()

UI.main()