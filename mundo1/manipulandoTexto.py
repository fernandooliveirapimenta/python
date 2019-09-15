frase = 'curso em video python'

print(frase[9])
#do caractere 9 ate 13 range
print(frase[9:13])
#pulando 2
print(frase[9:21:2])

# do inicio ate 5
print(frase[:5])

# do 15 ate fim
print(frase[15:])

# do 9 pulando de 3 em 3
print(frase[9::3])

print(len(frase))

print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('curso' in frase)
print(frase.replace('python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '  Aprenda Python  '
print(frase.strip())

frase = 'curso em video python'
lista = frase.split()
print(lista)
print('-'.join(lista))


garrafa = 'garrafa da perto do talco'
print(garrafa[3:10:2])

print( """skgjskdgjkdsgj sldkjgksdjg jklsdjgkl sjdg
lsdkjgldsjglds lsdjk jksdj ksjgk jskj kjskjgsjg
lsdkjgksdgk slj sjgk""")

cuso = 'Curso de python    '
print(len(cuso.strip()))

print('Fernado pimenta'.split()[1][3])


# desafio 22
nomecompleto = 'Fernando Oliveira Pimenta da Silva'
print(nomecompleto.upper())
print(nomecompleto.lower())
print(len(nomecompleto.replace(' ', '')))
print(len(nomecompleto.split()[0]))

# desafio 23
numero = '1834'
print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))

# deasio 24
cidade = 'Santo das artes'
print(cidade.lower().startswith('santo'))

# desafio 25
nome = 'Fernando Oliveira Pimenta da Silva'
print(nome.lower().find("silva"))
print('silva' in nome.lower())

# desafio 26
frased = 'Meu macbook é muito bonito e rapido eu adoro'

print(frased.count('a'))
print(frased.find('a'))
posicoes = []
for x in range(0, len(frased)):
    if frased[x] == 'a':
        posicoes.append(x)


print(posicoes[len(posicoes)-1])

# desafio 27

nomePessoa = 'Fernando oliveira pimenta'
nomes = nomePessoa.split()
print('{} {}'.format(nomes[0], nomes[len(nomes) - 1]))
