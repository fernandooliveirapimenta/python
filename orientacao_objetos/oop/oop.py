class MyClass(object):
    def setAge(self, num):
        self.age = num

    def getAge(self):
        return self.age

class MyClass2(object):
    def __init__(self, age):
        self.age = age

    def get_age(self):
       return self.age

zarc = MyClass()
zarc.setAge(54)
print(zarc.getAge())

tt = MyClass2(33)
print(tt.get_age())

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(9)
b = InstanceCounter(18)
c = InstanceCounter(27)

for obj in (a,b,c):
    print(f'val of obj {obj} = {obj.get_val()}')
    print(f'count: {obj.get_count()}')

class myClass:
    class_attribute = 99

    def class_method(self):
        self.instance_attribute = 'I am instance attribute'


print(myClass.__dict__)


a = myClass()
a.class_method()
print(a.__dict__)


print()
print()
print()

normal_list = [2, 4, 5, 7, 9]


class CustomSequence():
    def __len__(self):
        return 5

    def __getitem__(self, item):
        return f'x{item}'


class funkyback():
    def __reversed__(self):
        return 'backwards!'


for seq in normal_list, CustomSequence(), funkyback():
    print(f'\n{seq.__class__.__name__}: ', end='')
    for item in reversed(seq):
        print(item, end=', ')

