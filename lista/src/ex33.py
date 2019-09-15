
a = 3
b = 1
c = 4

menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(menor)
print(maior)
