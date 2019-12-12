from design_patterns.builder.Builder import JeepBuilder, Director
if __name__ == '__main__':
    jeepBuilder = JeepBuilder()
    director = Director()

    print('Jeep')

    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()
    print('')
