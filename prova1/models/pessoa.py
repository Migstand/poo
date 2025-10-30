import json
from datetime import datetime, timedelta
class Pessoa:
    def __init__(self, id, nome, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_nascimento(nascimento)
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    
    def set_nascimento(self, nascimento):
        hoje = datetime.now()
        # a , m, d = map(int, hoje.split("-"))
        # h, e, y = map(int, nascimento("/"))
        # if y> a: raise ValueError(" Digite uma data existente: ")
        # if e> m: raise ValueError(" Digite uma data existente: ")
        # if h> d: raise ValueError(" Digite uma data existente: ")
        if nascimento > hoje: raise ValueError("Digite uma data existente: ")
        self.__nascimento = nascimento
    def get_nascimento(self, nascimento):
        return self.__nascimento
    

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__nascimento}"

    def to_json(self):
        return { "id" : self.__id, "nome" : self.__nome, "nascimento" : self.__nascimento}
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["nome"], dic["nascimento"])
    
class PessoaDAO:
    objetos = []                           
    @classmethod
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
    def lista_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None

    @classmethod
    def salvar(cls):
        with open("pessoas.json", mode="w") as arquivo:
            #json.dump(cls.objetos, arquivo, default = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = Pessoa.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("pessoas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    # c = Cliente(dic["id"], dic["nome"])
                    c = Pessoa.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass