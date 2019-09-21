
maior18 = 0
homens = 0
mulheresmenor20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))

    if idade > 18:
        maior18 += 1
    elif sexo in 'Mm':
        homens += 1
    else:
        mulheresmenor20 += 1

    if 0 > int(input('Continuar: ')):
        break
print(f'Maiores de 18: {maior18}')
print(f'Quantidade de homens: {homens}')
print(f'Mulheres menor de 20: {mulheresmenor20}')

