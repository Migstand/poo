print('Digite uma frase:')
n = input()

n = list(n)
for i in range(len(n)):
    n.append(n[0])
    n.remove(n[0])
    b = ""
    for j in range(len(n)):
        a = n[j]
        b = b + a
    print(b)