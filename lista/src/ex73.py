
tabela = ('Corinthians','Sao Paulo', 'Cruzeiro', 'Flamengo', 'Vasco')

print(tabela[:3])
print(tabela[-3:])
def se(s):
    return s[1]
print(sorted(tabela))

def posicao(time, tabela):
    for pos, t in enumerate(tabela):
        if t == time:
            return pos + 1
    return -1

print(posicao('Cruzeiro', tabela))
