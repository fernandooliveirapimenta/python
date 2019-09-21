
soma = 0
for n in range(1, 501):
    if(n % 2 != 0 and n % 3 == 0):
        print(n, end=' ')
        soma += n
print(soma)
