print('Informe o número do mês')
mes = int(input())
li=[0,'janeiro','fervereiro','março','abril','maio','junho', 'julho','agosto','setembro','outubro','novembro','dezembro']

if (12-mes) >= 9:
    print("O mês",li[mes],"é do primeiro trimestre do ano")
if (12-mes) < 9 and (12-mes) >= 6:
    print("O mês",li[mes],"é do segundo trimestre do ano")
if (12-mes) < 6 and (12-mes) >= 3:
    print("O mês",li[mes],"é do terceiro trimestre do ano")
if (12-mes) < 3 and (12-mes):
    print("O mês",li[mes],"é do quarto trimestre do ano")