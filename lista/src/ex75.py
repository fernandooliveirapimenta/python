
v1 = int(input('Valor: '))
v2 = int(input('Valor: '))
v3 = int(input('Valor: '))
v4 = int(input('Valor: '))

tupla = (v1, v2, v3, v4)

nove = 0
ptres = 0
pares = ()
for p,v in enumerate(tupla):
    if v == 9:
        nove += 1
    if v == 3 and ptres == 0:
        ptres = p + 1
    if v % 2 == 0:
        pares += tuple(str(v))
print(nove)
print(ptres)
print(pares)
