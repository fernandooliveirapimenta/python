class BaseClass:
    pass


class DevivedClass(BaseClass):
    pass


class Date(object):
    def get_date(self):
        return '2019-12-1'


class Time(Date):
    def get_time(self):
        return '09:00:00'


dt = Date()
print(f'Date: {dt.get_date()}')

tm = Time()
print(f'Time: {tm.get_time()}')
print(f'Time Date: {tm.get_date()}')


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} is eating {self.name}. ')



class Dog(Animal):

    def fetch(self, thing):
        print(f'{self.name} goes after the {thing}! ')

    def show_affection(self):
        print(f'{self.name} wags tail')


class Cat(Animal):

    def swatstring(self):
        print(f'{self.name} shreds the string! ')

    def show_affection(self):
        print(f'{self.name} purrs')

d = Dog('Ranger')
c = Cat('MeOw')

d.fetch('ball')
c.swatstring()
d.eat('Dog food')
c.eat('Cat food')
# d.swatstring()


print()
for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')): a.show_affection()