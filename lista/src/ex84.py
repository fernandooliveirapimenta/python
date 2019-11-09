pessoas = list()
nomepeso = []

for i in range(0, 3):
    nomepeso.append(str(input('Nome: ')))
    nomepeso.append(float(input('Peso: ')))
    pessoas.append(nomepeso[:])
    nomepeso.clear()

pp = []
pl = []
for v, i in enumerate(pessoas):
    if v == 0:
        pp.clear()
        pp.append(i[:])
        pl.clear()
        pl.append(i[:])
    if i[1] < pl[0][1]:
        pl.clear()
        pl.append(i[:])
    if i[1] > pl[0][1]:
        pp.clear()
        pp.append(i[:])

print(len(pessoas))
print(pp)
print(pl)
