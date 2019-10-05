
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


num = 0
soma = 0
while num != 999:
    num = int(input('Digite um valor (999 para parar):'))
    soma += num
print('acabou!')
