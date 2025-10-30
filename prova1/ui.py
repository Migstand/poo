import json
from models.corrida import Corrida, CorridaDAO
from models.pessoa import Pessoa, PessoaDAO
from datetime import datetime, timedelta
class UI:
    
    def menu():
        print("Pessoas")
        print("1-Inserir, 2-Listar, 3-Pesquisar")
        print()
        print("Corridas")
        print("4-Inserir, 5-Listar, 6-PacePara")
        print()
        print("7-Encerrar")
        return int(input("Informe uma opção: "))
        
    def main():
        op = 0
        while op != 7:
            op = UI.menu()
            if op == 1: UI.pessoa_inserir()
            if op == 2: UI.pessoa_listar()
            if op == 3: UI.pessoa_pesquisar()
            if op == 4: UI.corrida_inserir()
            if op == 5: UI.corrida_listar()
            if op == 6: UI.corrida_pacepar()
       
    
    def pessoa_inserir():
        id = 0
        nome  = input("Digite o seu nome completo: ")
        nascimento = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
        c = Pessoa(id, nome, nascimento)
        PessoaDAO.inserir(c)
    def pessoa_listar():
        for obj in PessoaDAO.listar():
            print(obj)
    def pessoa_pesquisar():
        UI.pessoa_listar()
        pessoa = input("Digite o nome de alguem: ")
        with open("pessoas.json", mode="r") as arquivo:
            list_dic = json.load(arquivo)
            for dic in list_dic:
                for key in dic:
                    if key == "nome":
                        if pessoa == dic[key]:
                            return dic["nome"]
        return "Essa pessoa não está listada"

    
    def corrida_inserir():
        id  = 0
        idpessoa = int(input("Informe o id pessoa que irá correr: "))
        data = datetime.strptime(input("Informe a data em que a corrida acontece: "), "%d/%m/%Y")
        distancia = int(input("Informe a distância da corrida em metros: "))
        tempo = timedelta(hours = int(input("Duração em horas")), minutes=int(input("Duração em minutos"), seconds = int(input("Duração em segundos"))))
        c = Corrida(id, idpessoa, data, distancia, tempo)
        CorridaDAO.inserir(c)
    def corrida_listar():
        for obj in CorridaDAO.listar():
            print(obj)
    def corrida_pacepar():
        listas = []
        with open("corridas.json", mode="r") as arquivo:
            list_dic = json.load(arquivo)
            for dic in list_dic:
                c = Corrida.pace(dic[key])
                listas.append(c)
        print(min(listas))

    
UI.main()