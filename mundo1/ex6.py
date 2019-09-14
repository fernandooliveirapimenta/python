
valor = input('Digite algo: ')
print(type(valor))
print('So tem espacos',valor.isspace())
print('é um numero', valor.isnumeric())
print(valor.isalnum())
print(valor.isalpha())
print(valor.isdigit())
print('capitalizada: ', valor.istitle())


