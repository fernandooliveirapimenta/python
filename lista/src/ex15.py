km = float(input('Quantos km rodados? '))
dias = int(input('Quantos dias alugados? '))
preco = 60.0 * dias + (0.15 * km)
print('Preço final: {:.2f}'.format(preco))
