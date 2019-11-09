from random import randint
from time import sleep
from operator import itemgetter

jogo2 = {
    'jogador1': randint(1,6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking2 = dict()
print('Valores sorteados: ')
for k, v in jogo2.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking2 = sorted(jogo2.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING ==')
for i, v in enumerate(ranking2):
    print(f'  {i+1}o lugar: {v[0]} com {v[1]}.')
    sleep(1)

jogadas = {}

for jogador in range(1, 5):
    sleep(0.5)
    dado = randint(1, 8)
    jo = f'jogador{jogador}'
    jogadas[jo] = dado
    print(f'O  {jo} tirou {jogadas[jo]}')

rank = []
for v, i in enumerate(jogadas.items()):
    rank.append(i)
print(rank)


for i in range(0, len(rank)):
    for j in range(0, len(rank)):
        if(rank[i][1] > rank[j][1]):
            aux = rank[i]
            rank[i] = rank[j]
            rank[j] = aux

# print(rank)
print('Ranking dos jogadores: ')
for i, v in enumerate(rank):
    print(f'{i+1}o. lugar: {v[0]} com {v[1]}')

def ordena(col):
    for i in range(0, len(col)):
        for j in range(0, len(col)):
            if col[i] < col[j]:
                aux = col[i]
                col[i] = col[j]
                col[j] = aux

arr = [3, 2 , 5, 10, 1, 3, 0.2]

ordena(arr)

# print(arr)

