
cont = 1
while True:
    print(cont, '...', end='')
    cont += 1
    break

while True:
    n = int(input('Numero: '))
    if n == 999:
        break
    print(n)

print(f'A soma vale {cont}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos')

salario = 9998.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')