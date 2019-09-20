preco = float(input('Preco: '))
tipo = int(input('Tipo: '))

if tipo == 1:
    print('A vista: {:.2f}'.format(preco - ((preco * 1.10) - preco) ))
elif tipo == 2:
    print('A vista no cartao: {:.2f}'.format(preco - ((preco * 1.05) - preco) ))
elif tipo == 3:
    print('2x cartao: {:.2f}'.format(preco))
else:
    print('3x ou mais: {:.2f}'.format(preco + ((preco * 1.20) - preco)))

