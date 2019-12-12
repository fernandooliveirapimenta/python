import copy


class Prototype:
    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

    def __str__(self):
        return f'{self.getType()} {self.getValue()}'


class Type1(Prototype):
    def __init__(self, number):
        self._type = 'Type1'
        self._value = number

    def clone(self):
        return copy.copy(self)


class Type2(Prototype):
    def __init__(self, number):
        self._type = 'Type2'
        self._value = number

    def clone(self):
        return copy.copy(self)


class ObjectFactory:
    fernando = 'lindo'
    __type1Value1 = Type1(1)
    __type1Value2 = Type1(2)
    __type2Value1 = Type2(1)
    __type2Value2 = Type2(2)

    @staticmethod
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def getType1Value2():
        return ObjectFactory.__type1Value2.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()

    @staticmethod
    def getType2Value2():
        return ObjectFactory.__type2Value2.clone()
