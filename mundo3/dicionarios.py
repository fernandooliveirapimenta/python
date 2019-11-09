fernando = {'nome': 'ff'}
dados = dict()
dados = {'nome':'Pedro','idade':25}

print(dados)

print(dados['nome'])
print(dados['idade'])

dados['sexo']='M'
del dados['idade']

print(dados)

filme = {
    'titule':'Star Wars',
    'ano': 1977,
    'diretor': 'George Luccas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

locadora = list()
locadora.append(filme)
print(locadora)

pessoa = {'nome': 'Fernando', 'sexo': 'M', 'idade': 24}
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos')

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)