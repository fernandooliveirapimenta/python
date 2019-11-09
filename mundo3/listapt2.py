dados = list()
dados.append('Pedro')
dados.append(25)

pessoas = list()
pessoas.append(dados)

print(pessoas)
print(pessoas[0][0])

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = []
# [:] realiza copia
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

sensoriamento = [['Fernando', 24], ['Alexandre', 26], ['Izaac', 28]]
print(sensoriamento[1][0],sensoriamento[2][1])

for id in sensoriamento:
    print(id[0])

listpessoa = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    listpessoa.append(dado[:])
    dado.clear()
print(listpessoa)

for p in listpessoa:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')
