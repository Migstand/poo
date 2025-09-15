print('Digite uma frase:')
n = list(input().split())
print(*n)

for i in range(len(n)):
    n.remove(n[0])
    print(*n)