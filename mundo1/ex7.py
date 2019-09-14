# imprima antecessor e sucessor

num = 10
print('Sucessor = {} e Antecessor = {}' .format(num + 1, num - 1))

#leia um num mostre seu dobro seu triplo e raiz quadrada

#entrada = int(input('Numero: '))
entrada = 9
print('Dobro: {}, Triplo: {}, Raiz Quadrada: {}'.format(entrada * 2, entrada * 3, entrada ** (1/2)))


#leia duas notas e calcule media
#nota1 = float(input('Nota 1:'))
#nota2 = float(input('Nota 2: '))
nota1 = 6.5
nota2 = 8.2
soma = nota1 + nota2
media = (nota1+nota2)/2
print('Media: {}'.format(media))

#leia em metros e exiba em centimetros e milimetros

nmetros = float(1.72)
ncentimetros= nmetros * 100
nmilimetros = nmetros * 1000
print('Centimetros: {}, Milimetros: {}'.format(ncentimetros, nmilimetros))

#leia um inteiro e mostre sua tabuada

for x in range(0, 11):
    print('9 * {} = {}'.format(x, 9*x))

#leia qtd reais em dolares de uma carteira

vdolar = 4.09
qtdreais = float(20.85)
print('Em dolar: {}'.format(qtdreais * vdolar))

#leia largura de uma parede em metros, calcule sua area,
# e a quantidade de tinta necessária para pintala sabendo que
# cada litro de tinta pinta 2m

larguraparedemetros = 2
alturaparedemetros = 4
area = larguraparedemetros * alturaparedemetros
litrosTinta = area / 2
print('Qtd tinta = {}'.format(litrosTinta))

#preco com 5% de desconto

npreco = 10
nporcentagem = npreco - (npreco * (5/100))
print('O {} com 5% de desconto = {:.1f}'.format(npreco, nporcentagem))

















#salario com 15% de aumento
nsalario = 8000
nsalarioaumento = nsalario + (nsalario * (15/100))
print('Salario com 15% de aumento = {}'.format(nsalarioaumento))


