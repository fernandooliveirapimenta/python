from random import randint


def sorteio(n):
    sorteios = []
    for f in range(0, n):
        sorteios.append(randint(0, 100))

    return sorteios


def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    return soma


numeros = sorteio(10)
somaPares = somaPar(numeros)
print(f'Sorteados: {numeros}')
print(f'Soma pares: {somaPares}')
