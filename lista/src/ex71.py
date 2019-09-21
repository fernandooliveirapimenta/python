
def logica(valor, nota, list):
    if valor >= nota:
        qtd(valor, nota, list)
        return valor % nota
    else:
        qtd(valor, 1, list)
        return 1


def qtd(valor, nota, list):
    calc = valor // nota
    for n in range(1, calc + 1):
        list.append(nota)


sedulas = list()
sacado = int(input('Valor a ser sacado: '))
while sum(sedulas) != sacado:
    aux = sacado
    aux = logica(aux, 50, sedulas)
    aux = logica(aux, 20, sedulas)
    aux = logica(aux, 10, sedulas)
    aux = logica(aux, 1, sedulas)

print(sedulas)
print(sum(sedulas))
