
from datetime import date
ano = int(input('Ano 0 para atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('bisesto')
else:
    print('não')