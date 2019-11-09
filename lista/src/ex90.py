
aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

print(f'Média é igual a {aluno["media"]}')
aluno['situacao'] = 'Aprovado' if aluno['media'] > 6 else 'Reprovado'
print('-=' * 30)
for k,v in aluno.items():
    print(f' - {k} é igual a {v}')