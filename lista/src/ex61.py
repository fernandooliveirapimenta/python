termoinicial = int(input('Termo: '))
razao = int(input('Razao: '))

decimo = termoinicial + (10 - 1) * razao

qtdtermos = 0


aux = 0
while qtdtermos != 10:
    if aux == 0:
        aux = qtdtermos + razao
        print(aux)
    else:
        aux = aux + razao
        print(aux)

    qtdtermos += 1