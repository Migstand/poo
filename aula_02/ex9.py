print('Digite uma frase:')
n = list(input().split())

for i in range(len(n)):
    n[i] = list(n[i])
    for j in range(len(n[i]) - (len(n[i]) // 2)):
        n[i][j], n[i][(j+1)*(-1)] = n[i][(j+1) * (-1)],n[i][j]
    b = ""
    for q in range(len(n[i])):
        a = n[i][q]
        b = b + a
    print(b)