a = int(input())
b = int(input())
c = int(input())
d = int(input())

li=[a,b,c,d]
impar=0
par=0

for i in range(4):
    if li[i]%2==0:
        par = par + li[i]
    else:
        impar = impar +li[i]
print(par)
print(impar)