
n = int(input('Numero: '))

esperado = {1, n}
primos = set()
for num in range(1, n+1):
    if(n % num == 0):
        primos.add(num)
print(primos)
if esperado == primos:
    print('ok')
