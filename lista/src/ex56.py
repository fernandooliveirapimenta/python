

qtd = 0
soma = 0
media = 0
nomehomemmaisvelho = ''
qtdmulhermenos20 = 0
maioridade = 0

for pessoa in range(1,5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))

    if(pessoa == 1 and sexo == 'H'):
        maioridade = idade
        nomehomemmaisvelho = nome

    if(idade > maioridade and sexo == 'H'):
        maioridade = idade
        nomehomemmaisvelho = nome

    if(sexo == 'M' and idade < 20):
        qtdmulhermenos20 += 1

    soma += idade
    qtd += 1

print('Media idade {}'.format(soma/qtd))
print('Homem mais velho {}'.format(nomehomemmaisvelho))
print('Qtd mulher menos 20 {}'.format(qtdmulhermenos20))
