
num = int(input('Numero: '))

fat = num
while num != 1:
    fat = fat * (num - 1)
    num -= 1

print(fat)

aux = 1
i = 2
while i <= num:
    aux = aux * i
    i += 1
print(aux)