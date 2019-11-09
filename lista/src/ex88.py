
import random

# qtd = int(input('Qtd: '))

jogos = []
for i in range(0, 3):
    jogo = []
    for j in range(0, 6):
        continuar = True
        while continuar:
            sorteio = random.randint(1, 60)
            if(sorteio not in jogo):
                continuar = False
                jogo.append(sorteio)

    jogos.append(jogo)

for j in jogos:
    print(j)