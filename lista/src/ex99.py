from time import sleep


def maior(* vals):
    print('Analisando os valores passados...')
    sleep(1)
    ord = sorted(vals, reverse=True)
    print(f'Foram informados {len(vals)} ao todo. ')
    print(f'O maior valor informado for {ord[0]}.')


maior(3, 2, 33, 2, 1, 33, 4, 344, 32)
