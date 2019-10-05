
num = [2, 5, 9, 1]

num[2] =3

num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.pop() #final
num.pop(2)
num.remove(2) #comeco

if 7 in num:
    print('na lista')

print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v} ... ', end='')
for p,v in enumerate(valores):
    print(f'{p}:{v} ... ', end='')


a = [2, 3, 4, 7]
b = a #recebe instancia na memoria
b = a[:] #copia um arrey em outro
b[2] = 338
print()
print(f'Lista A: {a}')
print(f'Lista B: {b}')
