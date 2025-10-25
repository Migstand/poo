class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque} - {self.idCategoria}"
    def to_json(self):
        return { "id" : self.id, "descricao" : self.descricao, "preco" : self.preco, "estoque" : self.estoque, "idCategoria" : self.idCategoria}
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"])
    
class ProdutoDAO:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1
        obj.id = max (cls.objetos, key = lambda x : x.id).id + 1
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def lista_id(cls, id):
        for obj in cls.objetos:
            if obj.id == id return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, produto):
        aux = cls.lista_id(obj.id)
        if aux != None:
            cls.objetos.remove(obj)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, deafault = Produto.to_json, indent = 4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode = "r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Produto.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass
               


