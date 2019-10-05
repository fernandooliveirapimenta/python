
valores = []
while True:
    v = int(input('Valor: '))
    if v < 0:
        break
    valores.append(v)

print(len(valores))
valores.sort(reverse=True)
print(valores)

if 5 in valores:
    print('5 foi digitado')