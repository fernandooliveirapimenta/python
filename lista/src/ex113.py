def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
            continue
        else:
            return n


num = leiaInt('val: ')
