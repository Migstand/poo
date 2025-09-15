print('Digite três valores:')
a = int(input())
b = int(input())
c = int(input())
li = [a,b,c]
maior = 0
menor = a

for i in range(3):
    if li[i] > maior:
        maior = li[i]
    if li[i] < menor:
        menor = li[i]

li.remove(maior)
li.remove(menor)

crescente = [menor, li[0], maior]
print(*crescente)