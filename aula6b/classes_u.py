from datetime import datetime

class Cliente:
    def __init__(self, id, email, nome, fone):
        self.set_id(id)
        self.set_email(email)
        self.set_nome(nome)
        self.set_fone(fone)
    
    # def set_id(self, id):
    #     if type(id) == str: raise ValueError("Digite um ip válido")
    #     else: self.ip = ip
    
    # def set_email(self, email):
    #     if type(email) != str: raise ValueError("Digite um email válido")
    #     else: self.email = email
    
    # def set_nome(self, nome):
    #     if type(nome) != str: raise ValueError("Digite um nome válido")
    #     else: self.nome = nome
    
    # def set_fone(self, fone):
    #     if type(fone) != str: raise ValueError("Digite um telefone válido")
    #     else: self.fone = fone
    
    # def get_id(self):
    #     return self.ip
    
    # def get_emai(self):
    #     return self.email
    
    # def get_nome(self):
    #     return self.nome
    
    # def get_fone(self):
    #     return self.fone
    
    def __str__(self):
        return f"{self.id} - {self.email} - {self.nome} - {self.fone}"
    
class Venda:
    def __init__(self, id, data, carrinho, total, Cliente):
        self.set_id(id)
        self.set_data(data)
        self.set_carrinho(carrinho)
        self.set_total(total)
        self.set_idClientes(id_Clientes)
    
    # def set_id(self, id):
    #     if type(id) == str: raise ValueError("Digite um ip válido")
    #     else: self.ip = ip
    
    # def set_data(self, data):
    #     if data
    # def get_data(self):
    #     return self.data

    # def set_carrinho(self, carrinho):
    #     if Venda: carrinho = True
    #     else: carrinho = False
    # def get_carrinho(self):
    #     return carrinho
    
    # def set_total(self, total):
    #     self.total = total
    # def get_total(self):
    #     return self.total

    # def set_idClientes(self, id_Clientes):
    #     self.id_Clientes = id_Clientes
    # def get_idClientes(self):
    #     return set_idClientes
    
class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        set_id(id)
        set_qtd(qtd)
        set_preco(preco)
        set_idVenda(idVenda)
        set_idProduto(idProduto)
    
    # def set_id(self, id):
    #     if type(id) == str: raise ValueError("Digite um ip válido")
    #     else: self.ip = ip
    # def get_id(self):
    #     return self.id
    
    # def set_qtd(self, qtd):
    #     self.qtd = qtd
    # def get_qtd(self):
    #     return self.qtd
    
    # def set_preco(self, preco):
    #     self.preco = preco
    # def get_preco(self):
    #     return self.preco
    
    # def set_idVenda(self, idVenda):
    #     self.idVenda = idVenda
    # def get_idVenda(self):
    #     return self.idVenda
    
    # def set_idProduto(self, idProduto):
    #     self.idProduto = idProduto
    # def get_idProduto(self):
    #     return self.idProduto

class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):

class Categoria:
    def __init__(self, id, descricao):
