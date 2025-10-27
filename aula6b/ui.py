from models.cliente import Cliente, ClienteDAO

from models.venda import Venda, VendaDAO

from models.vendaitem import VendaItem, VendaItemDAO

from models.categoria import Categoria, CategoriaDAO

from models.produto import Produto, ProdutoDAO

class UI:
    
    def menu():
        print("Clientes")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print()
        print("Categoria")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print()
        print("Produtos")
        print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir")
        print()
        print("13-Fim")
        return int(input("Informe uma opção: "))
    
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()

    def cliente_inserir():
        id = 0
        nome = input("Informe o nome: ")
        c = Cliente(id, nome)
        ClienteDAO.inserir(c) #instanciar DAO vai criar várias listas de clientes

    def cliente_listar():
        for obj in ClienteDAO.listar():
            print(obj)

    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        c = Cliente(id, nome)
        ClienteDAO.atualizar(c)
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        nome = ""
        c = Cliente(id, nome)
        ClienteDAO.excluir(c)
    
    def categoria_inserir():
        id = 0
        descricao = input("Infor a descrição dessa categoria: ")
        c = Categoria(id, descricao)
        CategoriaDAO.inserir(c)
    def categoria_listar():
        for obj in CategoriaDAO.listar():
            print(obj)
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição dessa categoria: ")
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        descricao = ""
        c = Categoria(id, descricao)
        CategoriaDAO.excluir(c)
    
    def produto_inserir():
        id = 0
        descricao = input("Informa a descrição desse produto: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque desse produto: "))
        id_Categoria = int(input("Informe a categoria desse produto colocando o id referente: "))
        c = Produto(id, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.inserir(c)

    def produto_listar():
        for obj in ProdutoDAO.listar():
            print(obj)

    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informa a nova descrição desse produto: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o atual estoque desse produto: "))
        id_Categoria = int(input("Informe a categoria atual desse produto colocando o id referente: "))
        c = Produto(id, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.atualizar(c)

    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id a ser excluído: "))
        descricao = ""
        preco = 0
        estoque = 0
        id_Categoria = 0
        c = Produto(id, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.excluir(c)

UI.main()