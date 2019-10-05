
lista_numerica = []

while True:
    num = int(input('Numero [negativo para sair]: '))
    if num < 0:
        break
    if num not in lista_numerica:
        lista_numerica.append(num)
lista_numerica.sort()
print(lista_numerica)