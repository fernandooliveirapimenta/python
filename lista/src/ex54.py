
from datetime import date

maiores = 0
menores = 0

for n in range(1, 8):
    ano = int(input('Ano nascimento: '))
    if(date.today().year - ano > 18):
        maiores += 1
    else:
        menores += 1
print(maiores)
print(menores)
