try:
    a = 50
    b = 0
    r = a/b
except ZeroDivisionError as e:
    print(f'zero division {e.__cause__}')
except (ValueError, TypeError):
    print('erro')
except Exception as err:
    print(f'oi {err}')
else:
    print('sucesso')
finally:
    print('executado sempre')