

soma = 0
quantos = 0

n = 0
while n != 999:
    n = int(input('Numero: '))
    if n != 999:
        soma += n
        quantos += 1
print(quantos)
print(soma)
