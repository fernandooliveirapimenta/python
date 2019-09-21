

for pessoa in range(1,6):
    peso = float(input('Peso: '))
    if(pessoa == 1):
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(maior)
print(menor)
