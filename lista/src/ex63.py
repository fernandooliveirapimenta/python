
n = int(input('Numero: '))

t1 = 0
t2 = 1
print('{} {}'.format(t1, t2), end=' ')

qtd = 3
while qtd < n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    qtd += 1
# qtd = 0
#
# def fibo(num):
#    if num == 0:
#       return 0
#    elif num == 1:
#       return 1
#    else:
#       return fibo(num - 1) + fibo(num - 2)
#
# while qtd < n:
#    print(fibo(qtd), end=' ')
#    qtd += 1
