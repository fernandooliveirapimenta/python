from random import randint
from time import sleep
intens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
''')

jogador = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VENCEU')
    elif jogador == 2:
        print('PERDEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VENCEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('VENCEU')
    elif jogador == 1:
        print('PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
print('-=' * 11)
