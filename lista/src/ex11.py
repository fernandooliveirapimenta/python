larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m2'.format(larg, alt, area))
print('Para pintar essa parede, você vai precisar de {} litros de tinta'.format(area / 2))