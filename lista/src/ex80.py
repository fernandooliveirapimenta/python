

def ordena(col):
    for i in range(0, len(col)):
        for j in range(0, len(col)):
            print(f'{i} {j}')
            if col[i] < col[j]:
                aux = col[i]
                col[i] = col[j]
                col[j] = aux

col = [3,1,5,2,7,1]
print(len(col))
ordena(col)
print(col)
# for v in range(1, 6):
#     v1 = int(input('Valor: '))
    # ordena(col, v1)

# print(col)
print(range(5, 0, -1))