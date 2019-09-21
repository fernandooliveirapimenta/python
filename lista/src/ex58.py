from random import randint
from time import sleep

print('pensando ....')
computador = randint(0, 10)
sleep(1)

while(int(input('Adivinhe: ')) != computador):
    print('Errou')

print('Acertou')



