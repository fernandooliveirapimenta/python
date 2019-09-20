
nome = 'Fernando'

if nome == 'Gustavo':
    print('nome bonito')
elif nome == 'Fernando' or nome == 'Pedro':
    print('nome popular')
    if 2 > 1:
        print('dentro')

elif nome in 'Ana Claudia Juliana':
    print('nome feminino')
else:
   print('nome normal')

print('Tenha bom dia')


valorcasa = 28000.00
salario = 8000
anos = 30
prestacao = valorcasa / anos
trintaporcento = salario * 30 / 100

if prestacao > trintaporcento:
    print('não pode')
elif prestacao <= trintaporcento:
    print('uhulll valor prestacao: {}'.format(prestacao))


numero = 332

print(bin(numero))
escolhar = 'o'

if escolhar == 'b':
    print('binario {0:b}'.format(numero))
elif escolhar == 'o':
    print('octal {}'.format(oct(numero)))
else:
    print('haxadecimal {}'.format(hex(numero)))

n1 = 83
n2 = 83

if n1 > n2:
    print('primerio')
elif n2 > n1:
    print('segundo')
else:
    print('iguais')

import datetime

now = datetime.datetime.now()
nascimento = 2000
idade = now.year - nascimento
print(idade)

if idade <= 18:
    print('ainda vai')
elif idade == 18:
    print('hora de ir')
else:
    print(idade - 18)


n1 = 8
n2 = 2

media = (n1 + n2) / 2

print(media)

if media < 5:
    print('reprovado')
elif media >= 5 and media <= 6.9:
    print('recuperacao')
else:
    print('aprovado')


anoatleta = 2005
idade = datetime.datetime.now().year - anoatleta

if idade <= 9:
    print('mirim')
elif idade > 9 and idade <= 14:
    print('infantio')
elif idade > 14 and idade <= 19:
    print('junior')
elif idade <= 20:
    print('senior')
else:
    print('master')

l1 = 3
l2 = 9
l3 = 9

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('triangulo')
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Equilátero')
    elif (l1 == l2 and l2 != l3) \
            or (l2 == l3 and l1 != l2)\
            or (l1 == l3 and l2 != l3):
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('nao')


