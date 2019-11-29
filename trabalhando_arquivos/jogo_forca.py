import random

def imprime_msg_abert():
    print('*' * 30)
    print('Bem vido')
    print('*' * 30)


def carrega_palavra_secreta():
    with open('palavras.txt', 'r') as arquivo:
        palavras = []
        for l in arquivo:
            palavras.append(l.strip())

        numero = random.randrange(0, len(palavras))
        return palavras[numero].upper()

def jogar():
    imprime_msg_abert()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ['_' for letra in palavra_secreta]
    print(letras_acertadas)


jogar()


