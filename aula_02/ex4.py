data = input('Digite uma data no formato dd/mm/aaaa: ')

li = [0,'janeiro','fervereiro','março','abril','maio','junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

data = list(map(int,input().split()))
if data[1] == 2:
    if data[0] > 28 and data[0] < 1:
        print("A data informada não é válida")
elif data [1] >