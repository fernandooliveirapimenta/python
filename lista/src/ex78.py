
# v1 = int(input('Valor: '))
# v2 = int(input('Valor: '))
# v3 = int(input('Valor: '))
# v4 = int(input('Valor: '))
# v5 = int(input('Valor: '))
#
# col = [v1, v2, v3, v4, v5]
# print(f' Maior {max(col)} pos {col.index(max(col)) + 1}')
# print(f' Menor {min(col)} pos {col.index(min(col)) + 1}')


listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} na posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...',end='')
print()
