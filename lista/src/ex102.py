
def fatorial(n=1, show=False):
    """
    Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: resultado
    """
    fat = 1
    fmt = ''
    for i in range(n, 0, -1):
        fmt += f'{i} {"x" if i > 1 else "="} '
        fat *= i

    print(f'{fmt}{fat}') if show \
        else print(fat)

    return fat

fatorial(5, True)
fatorial(5)

help(fatorial)
