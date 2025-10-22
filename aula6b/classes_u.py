from datetime import datetime

class Cliente:
    def __init__(self, id, email, nome, fone):
        self.set_id(id)
        self.set_email(email)
        self.set_nome(nome)
        self.set_fone(fone)
    
    def set_id(self, id):
        if type(id) == str: raise ValueError("Digite um ip válido")
        else: self.ip = ip
    
    def set_email(self, email):
        if type(email) != str: raise ValueError("Digite um email válido")
        else: self.email = email
    
    def set_nome(self, nome):
        if type(nome) != str: raise ValueError("Digite um nome válido")
        else: self.nome = nome
    
    def set_fone(self, fone):
        if type(fone) != str: raise ValueError("Digite um telefone válido")
        else: self.fone = fone
    
    def get_id(self):
        return self.ip
    
    def get_emai(self):
        return self.email
    
    def get_nome(self):
        return self.nome
    
    def get_fone(self):
        return self.fone
    
    def __str__(self):
        return f"{self.id} - {self.email} - {self.nome} - {self.fone}"
    
class Venda:
    def __init__(self, id, data, carrinho, total, id_Clientes):
        self.set_id(id)
        self.set_data(data)
        self.set_carrinho(carrinho)
        self.set_total(total)
        self.set_idClientes(id_Clientes)
    
    def set_id(self, id):
        if type(id) == str: raise ValueError("Digite um ip válido")
        else: self.ip = ip
    
    def set_data(self, data):
        if data