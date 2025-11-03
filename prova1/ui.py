from models.corrida import Corrida, CorridaDAO
from models.pessoa import Pessoa, PessoaDAO
from datetime import datetime, timedelta
class UI:
    
    def menu():
        print("Pessoas")
        print("1-Inserir, 2-Listar, 3-Pesquisar")
        print()
        print("Corridas")
        print("4-Inserir, 5-Listar, 6-MenorPace")
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
            if op == 6: UI.corrida_menor_pace()
       
    
    def pessoa_inserir():
        id = 0
        nome  = input("Digite o seu nome completo: ")
        nascimento = datetime.strptime(input("Informe a data de nascimento: "))
        c = Pessoa(id, nome, datetime(nascimento, "%d/%m/%Y"))
        PessoaDAO.inserir(c)

    def pessoa_listar():
        for obj in PessoaDAO.listar():
            print(obj)

    def pessoa_pesquisar():
        nome = input("Digite o nome de alguem: ")
        pessoa = UI.pessoa_listar()
        for obj in pessoas:
            if obj.get_nome().startswith(nome): print(obj)

    def corrida_inserir():
        id  = 0
        UI.pessoa_listar()
        idpessoa = int(input("Informe o id pessoa que irá correr: "))
        data = datetime.strptime(input("Informe a data em que a corrida acontece: "), "%d/%m/%Y")
        distancia = int(input("Informe a distância da corrida em metros: "))
        tempo = input("Informe o tempo em hh:mm:ss: ")
        h, m, s = map(int, input().split(":"))
        c = Corrida(id, idpessoa, datetime.strftime(data, "%d/%m/%Y"), \
            distancia, timedelta(hours = h, minutes = m, seconds = s))
        CorridaDAO.inserir(c)

    def corrida_listar():
        for obj in CorridaDAO.listar():
            print(obj)

    def corrida_menor_pace():
        corridas = CorridaDAO.listar()
        m = corridas[0]
        for obj in CorridaDAO.listar():
            if obj.pace() < m.pace(): m = obj
        print(m)

UI.main()