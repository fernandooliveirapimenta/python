

soma = 0
qtd = 0
maior = 0
menor = 0

continuar = 's'

while continuar == 's':
    num = int(input('Numero: '))
    qtd += 1
    soma += num
    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    else:
        if num < menor:
            menor = num
    continuar = str(input('continuar? '))

print(maior)
print(menor)
print(soma/qtd)