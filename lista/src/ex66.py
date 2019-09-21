
qtd = 0
soma = 0
while True:
    num = int(input('Numero: '))
    if num == 999:
        break
    qtd += 1
    soma += num

print(f'Quantidade: {qtd}')
print(f'Soma: {soma}')