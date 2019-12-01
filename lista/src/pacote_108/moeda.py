def aumentar(num):
    return num + 1


def diminuir(num):
    return num - 1


def dobro(num):
    return num * 2


def metade(num):
    return num / 2


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
