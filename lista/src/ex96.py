
def area(largura, comprimento):
    return largura * comprimento

def divisor():
    print('-='*30)

def msg(msg):
    print(msg)

def lerteclado(msg):
    return input(msg)


msg('Controle de Terrenos')
divisor()
largura = float(lerteclado('Largura (m): '))
comprimento = float(lerteclado('Comprimento (m): '))

divisor()
msg(f'A área de um terreno {largura}x{comprimento} é de {area(largura, comprimento)}')
