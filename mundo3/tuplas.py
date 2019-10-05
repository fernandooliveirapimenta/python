# lance =  () tupla
# lance =  [] lista
# lance =  {} dicionario
# nao é obrigatorio usar parenteses em tuplas
# tuplas sáo imutaveis
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na pos {pos}')
print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
c = b + a

print(c.count(8))

pessoa = ('Gustavo', 39, 'M', 98.88)
print(pessoa)
def resolvezarc(mesatual, diaatual):
    referencia = mesatual * 3
    pivo3 = referencia
    pivo2 = referencia - 1
    pivo1 = referencia - 2
    print(f'{pivo1}, {pivo2}, {pivo3}')
    if diaatual <= 10:
        return pivo1
    elif diaatual > 10 and diaatual <= 20:
        return pivo2
    else:
        return pivo3

# print(resolvezarc(10, 6))
# print(resolvezarc(10, 13))
# print(resolvezarc(10, 23))
