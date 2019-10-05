
v1 = int(input('Valor: '))
v2 = int(input('Valor: '))
v3 = int(input('Valor: '))
v4 = int(input('Valor: '))
v5 = int(input('Valor: '))

col = [v1, v2, v3, v4, v5]
print(f' Maior {max(col)} pos {col.index(max(col)) + 1}')
print(f' Menor {min(col)} pos {col.index(min(col)) + 1}')
