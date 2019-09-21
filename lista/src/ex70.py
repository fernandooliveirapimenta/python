
totalgasto = 0
qtdmaiormil = 0
produtomaisbarato = 0
maisbarado = 0
nomemaisbarato = ''

while True:
    nome = str(input('Nome produto: '))
    preco = float(input('Preço: '))

    totalgasto += preco
    if preco > 1000.0:
        qtdmaiormil += 1
    if maisbarado == 0:
        maisbarado = preco
        nomemaisbarato = nome
    elif preco < maisbarado:
        maisbarado = preco
        nomemaisbarato = nome

    continuar = str(input('S/N'))
    if continuar in 'Nn':
        break
print(f'Total gasto: {totalgasto}')
print(f'Maior que R$1000: {qtdmaiormil}')
print(f'Mais barato {nomemaisbarato}')