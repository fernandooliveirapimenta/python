from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['cpts'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['cpts'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + \
                             ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
