def voto(ano=1995):
    from datetime import datetime
    idade = datetime.now().year - ano
    print(f'Idade: {idade}')
    if 18 <= idade <= 60:
        return 'OBRIGATÓRIO'
    elif idade <= 18:
        return 'NEGADO'
    else:
        return 'OPCIONAL'



print(voto(2010))
print(voto(1970))
print(voto(1950))
print(voto(1930))
print(voto(1900))