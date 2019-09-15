# tempo = int(input('Quantos anos tem seu carro?'))
# if tempo <= 3:
#     print('novo')
# else:
#     print('velho')
#
# print('carro novo' if tempo <= 3 else 'carro velho')

# nome = 'Fernando'
#
# if(nome == 'Gustavo'):
#     print('nome feio')
#
# n1 = 8
# n2 = 7
# media = n1 + n2 / 2
#
# if media > 6:
#     print('boa')
# else:
#     print('ruim')
#
# from random import choice
# numeros = [0, 1, 2, 3, 4, 5]
# escolhido = choice(numeros)
#
# adivinhar = 100
#
# while(adivinhar != escolhido):
#     adivinhar = int(input('Adivinhe: '))
#
# print(adivinhar)
#
# velocidade = 89.8
# if velocidade > 80:
#     print('Multa: {:.2f}'.format((velocidade - 80) * 7 ) )
# else:
#     print('ok')
#
# num = int(input('Numero: '))
# if num % 2 == 0:
#     print('par')
# else:
#     print('impar')
#
# distancia = float(input('Distancia: '))
#
# if distancia <= 200.0:
#     print(distancia * 0.5)
# else:
#     print(distancia * 0.45)

ano = int(input('Ano: '))
if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('bissexto')
        else:
            print('nao')
    else:
        print('bissexto')
else:
    print('nao')

n1 = 3
n2 = 4
n3 = 1

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

a = 3.2
b = 5.21
c = 6

if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
    print('é um triangulo')
else:
    print('não é')











