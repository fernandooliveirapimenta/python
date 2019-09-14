real = float(input('Quanto dinheiro voce tem na carteira? '))
dolar = real / 3.27
print('Com R${} voce pode comprar US${:.2f}'.format(real, dolar))