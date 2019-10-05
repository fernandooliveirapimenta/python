


def par(v):
    return True if v % 2 == 0 else False

valores = []
pares = []
impar = []
while True:
    v = int(input('Valor: '))
    if v < 0:
        break
    valores.append(v)
    if par(v) == True:
        pares.append(v)
    else:
        impar.append(v)

print(valores)
print(pares)
print(impar)
