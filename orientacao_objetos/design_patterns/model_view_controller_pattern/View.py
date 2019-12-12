
def showAllView(list):
    print(f'In our db have {len(list)}')
    for item in list:
        print(item.name())


def startView():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db? [y/n]')


def endView():
    print('Goodbye!')
