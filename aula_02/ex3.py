print('Digite quatro valores inteiros')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
li = [a,b,c,d]
maior = 0
menor = a
meios = 0

for i in range(4):
    if li[i] > maior:
        maior = li[i]
    if li[i] < menor:
        menor = li[i]

li.remove(maior)
li.remove(menor)

meios = li[0] + li[1]

print("Maior valor =", maior)
print("Menor valor =", menor)
print("A soma do segundo maior valor com o segundo menor =",meios)