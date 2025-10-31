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
        return self.__idpessoa

    
    def set_data(self, data):
        hoje = datetime.now()
        if data >= hoje: raise ValueError("Data inexistente")
        else: self.__data = data
    def get_data(self):
        return self.__data

    def set_distancia(self, distancia):
        self.__distancia = distancia
    def get_distancia(self):
        return self.__distancia
    
    def set_tempo(self, tempo):
        if tempo < timedelta(): raise ValueError("Tempo inválido")
        self.__tempo = tempo
    def get_tempo(self, tempo):
        return self.__tempo
    
    def pace(self):
        return (self.__tempo.seconds/60)/(self.__distancia/1000)
    
    def __str__(self):
        return f"{self.__id} - {self.__data.datetime.strftime("%d/%m/%Y")} - distância: {self.__distancia}m - tempo: {self.__tempo} - pace: {self.pace():.2f}"

    def to_json(self):
        return { "id" : self.__id, "idpessoa" : self.__idpessoa, 
        "data" : self.__data.strftime("%d/%m/%Y"), 
        "distancia" : self.__distancia, 
        "tempo" : self.__tempo.seconds}
    @staticmethod
    def from_json(dic):
        return Corrida(dic["id"], dic["idpessoa"], \
        datetime.strftime(dic["data"], "%d/%m/%Y"), \
         dic["distancia"], timedelta(seconds=dic["tempo"]))
    
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