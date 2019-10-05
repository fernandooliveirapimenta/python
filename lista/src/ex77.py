
palavras = ('Lapis', 'Celular', 'Fernando', 'Teclado', 'Futebol', 'Amor')

def vogal(p):
    return str(p).upper() in 'aeiou'.upper()

for p in palavras:
    vogais = ()
    for v in p:
        if vogal(v):
            vogais += tuple(v.lower())
    print(f'{p} = {vogais}')
