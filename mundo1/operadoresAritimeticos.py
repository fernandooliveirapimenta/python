# + adicao - subtracao * multiplicacao / divisao
# ** potencia
# // divisao inteira
# % resto

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)

# ordem precedencia
# primeiro parenteses ()
# segundo potencia **
# terceiro * / // % multiplicacao divisao divisao inteira resto divisao
# quarto + -

print('ordem')
print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)
print('{:=^20} !'.format('fefe' ))
n1 = 4
n2 = 3
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n produto é {}, divisao é {:.3f} '.format(s, m, d))
print('divisao inteira {} e potencia {}'.format(di, e))
