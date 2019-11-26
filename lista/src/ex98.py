# from time import sleep
#
#
# def divisor():
#     print('-=' * 30)
#
#
# def msg(msg):
#     print(msg)
#
#
# def lerint(msg):
#     return int(input(msg))
#
#
# def contador(inicio, fim, passo):
#     for n in range(inicio, fim+1, passo):
#         sleep(0.3)
#         print(f'{n}', end=' ')
#     print()
#
#
# divisor()
# msg('Contagem de 1 até 10 de 1 em 1')
# contador(1, 10, 1)
# divisor()
# msg('Contagem de 10 até 0 de 2 em 2')
# contador(10, 0, -2)
# divisor()
# msg('Agora é sua vez de personalizar a contagem!')
# contador(lerint('Inicio: '), lerint('Fim: '), lerint('Passo: '))
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= 1
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.6)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de ')
contador(5, 50, -2)
