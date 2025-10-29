import json
from datetime import datetime, timedelta
class Corrida:
    def __init__(self, id, idpessoa, data, distancia, tempo):
        self.set_id(id)
        self.set_idpessoa(idpessoa)
        self.set_data(data)
        self.set_distância(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_idpessoa(self, idpessoa):
        self.__idpessoa = idpessoa
    def get_idpessoa(self, idpessoa):
        with open("pessoas.json", mode="r") as arquivo:
            list_dic = json.load(arquivo)
            for dic in list_dic:
                for key in dic:
                    if key == "id":
                        if self.__idpessoa == dic[key]:
                            return dic["pessoa"]
        return "Essa pessoa não está listada"
    
    def set_data(self, data):
        hoje = datetime.now()
        if data > hoje: raise ValueError(" Digite uma data existente: ")
        else: self.__data = data
    def get_data(self):
        return self.__data

    def set_distancia(self, distancia):
        self.__distancia = distancia
    def get_distancia(self):
        return self.__distancia
    
    def set_tempo(self, tempo):
        self.__tempo = tempo
    def get_tempo(self, tempo):
        return self.__tempo
    
    def pace(self):
        qui = self.__distancia /1000
        h = self.__tempo.hours/60
        m = self.tempo.minutes
        s = self.__tempo.seconds*60
        minu = h + m + s
        return minu / qui
    
    def __str__(self):
        return f"{self.__id} - {self.__idpessoa} - {self.__data} - {self.__distancia} - {self.__tempo}"

    def to_json(self):
        return { "id" : self.__id, "idpessoa" : self.__idpessoa, "data" : self.__data, "distancia" : self.__distancia, "tempo" : self.__tempo}
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["idpessoa"], dic["data"], dic["distancia"], dic["tempo"])
    
class CorridaDAO:
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
    def atualizar(cls, obj):
        #procurar o objeto que tem o id dado por obj.id
        aux = cls.lista_id(obj.id)
        if aux != None:
            # aux.nome = obj.nome
            # remove o objeto antigo aux e insere novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        aux = cls.lista_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
        
    @classmethod
    def salvar(cls):
        with open("corridas.json", mode="w") as arquivo:
            #json.dump(cls.objetos, arquivo, default = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = Corrida.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("corridas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    # c = Cliente(dic["id"], dic["nome"])
                    c = Corrida.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass