import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id          # atributo de instância
        self.nome = nome      # cada cliente (instância) tem id e nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

class ClienteDAO:             # classe estática -> não tem instância
    objetos = []              # atributo da classe
    @classmethod              # classe DAO não vai ter instância
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1    
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            #aux.nome = obj.nome
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("cliente.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("cliente.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente(dic["id"], dic["nome"])
                    cls.objetos.append(c)
        except:
            pass      