termoinicial = int(input('Termo: '))
razao = int(input('Razao: '))

decimo = termoinicial + (10 - 1) * razao
print(decimo)
for i in range(termoinicial, decimo, razao):
    print('{} '.format(i), end='-> ' )

# aux = 0
# for n in range(1, 11):
#     if aux == 0:
#         aux = n + razao
#         print(aux)
#     else:
#         aux = aux + razao
#         print(aux)