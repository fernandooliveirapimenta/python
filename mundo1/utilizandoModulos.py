from math import sqrt,ceil
import math
import emoji
import random
import os

print(sqrt(16))
print(math.ceil(sqrt(16)))
print(random.random())

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)
print(emoji.emojize('Olá, :sunglasses:', use_aliases=True))


#numero real e mostrar somente a parte inteira

nreal = 6.127
print(math.floor(nreal))
print(nreal // 1)

#comprimento do cateto oposto e do cateto adjacente
# de um triangulo
#calcule o mostre o comprimento da hipotenusa
coposto = 8.3
cadjacente = 3.435
print(math.sqrt(math.pow(coposto, 2) + math.pow(cadjacente, 2)))

# leia angulo qualquer, mostre na tela o valor do seno, cosseno e tangente desse angulo

nangulo = 45
print('Seno: {}, Cosseno: {}, Tangente: {}', math.sin(nangulo)
      , math.cos(nangulo), math.tan(nangulo))

# sortear um de quatro alunos
alunos = ["Fernando", "Bruna", "Maria", "Joao"]
for x in range(0, 1):
      print('Aluno sorteado: {}'.format(alunos[random.randint(0, len(alunos)-1)]))

print('\n')

sorteados=set([])

# for x in range(1, 50):
#       print(random.randint(0, 4))

while len(sorteados) < len(alunos):
      sorteados.add(alunos[random.randint(0, len(alunos)-1)])


# for aluno in alunos:



from pygame import mixer
import subprocess
subprocess.call(["afplay", "file.mp3"])




