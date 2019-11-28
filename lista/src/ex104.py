def leiaInt(msg):
    n = input(msg)
    # n.isnumeric()
    try:
       inteiro = int(n)
       print(f'Você acabou de digitar o número {inteiro}')
    except:
       print('ERRO! Digite um número inteiro válido')


leiaInt('Digite um número: ')
