def contador(i, f, p):
    """

   :param i: inicio
   :param f: fim
   :param p: passo
   :return: none
    """
    print(f'{i}, {f}, {p}')


help(contador)

def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

soma(3,2,5)
soma(8,4)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f += c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f1, f2, f3)
