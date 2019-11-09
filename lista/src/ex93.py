jodador = dict()
partidas = list()
jodador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jodador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c+1}?')))
jodador['gols'] = partidas[:]
jodador['total'] = sum(partidas)
print('-=' * 30)
print(jodador)
print('-=' * 30)

for k, v in jodador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jodador["nome"]} jogou {len(jodador["gols"])} partidas.')
for i, v in enumerate(jodador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jodador["total"]} gols.')
