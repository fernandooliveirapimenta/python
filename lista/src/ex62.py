
termoinicial = 5

while termoinicial != 0:
    termoinicial = int(input('Termo: '))

    if termoinicial != 0:

        razao = int(input('Razao: '))
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