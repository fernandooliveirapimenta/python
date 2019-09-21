

operacao = 0

while operacao != 5:
    v1 = int(input('Valor1: '))
    v2 = int(input('Valor2: '))
    operacao = int(input('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos numeros
        [ 5 ] sair
        
    '''))
    if operacao == 1:
        print(v1 + v2)
    elif operacao == 2:
        print(v1 * v2)
    elif operacao == 3:
        print(v1 if v1 > v2 else v2)