termoinicial = int(input('Termo: '))
razao = int(input('Razao: '))

aux = 0
for n in range(1, 11):
    if aux == 0:
        aux = n + razao
        print(aux)
    else:
        aux = aux + razao
        print(aux)