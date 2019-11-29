NOME = 'palavras.txt'
arquivo = open(NOME, 'r')
print(arquivo.read())
# for l in arquivo.readlines():
#     print(l)

arquivo_linhas = open(NOME)

for l in arquivo_linhas:
    print(l.strip())