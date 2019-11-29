NOME = 'palavras.txt'
arquivo = open(NOME, 'w')

arquivo.write('banana \n')
arquivo.write('melancia \n')
arquivo.write('fernando \n')

arquivo.close()

# r read, w write, a append, b binary
arquivo_aberto = open(NOME, 'a')
arquivo_aberto.write('fefe \n')
arquivo_aberto.close()


