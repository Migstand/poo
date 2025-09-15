data = input('Digite uma data no formato dd/mm/aaaa: ')
li = [0,'janeiro','fervereiro','março','abril','maio','junho', 'julho','agosto','setembro','outubro','novembro','dezembro']
lista = data.split("/")
print(*lista)