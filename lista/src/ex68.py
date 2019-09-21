
from random import randint


vitorias = 0
print('Voce é impar maquina é par')
while True:
    escolharcomputador = randint(1,5)
    escolhajogador = int(input('Numero de 1 ate 5: '))
    print(f'Escolha maquna {escolharcomputador}')
    if (escolhajogador + escolharcomputador) % 2 != 0:
        vitorias += 1
    else:
        break
print(f'A quantidade de vitórias foi de: {vitorias}')

