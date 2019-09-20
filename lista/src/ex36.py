casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestacao sera de R${:.2f}'.format(prestacao))
print('COMPRANDO tem que pagar {} e o mínimo é de {}'.format(prestacao, minimo))

if prestacao <= minimo:
    print('Empréstimo pode ser Concedido!')
else:
    print('Emprestimo não pode ser concedido')