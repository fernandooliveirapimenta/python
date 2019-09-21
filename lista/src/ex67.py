

def tabuada(num):
    for n in range(0, 11):
        print(f'{n} x {num} = {num * n}')

while True:
    valor = int(input('Tabudado do: '))
    if valor < 0:
        break
    tabuada(valor)
