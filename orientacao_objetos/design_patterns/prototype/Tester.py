from design_patterns.prototype.Prototype import ObjectFactory

if __name__ == '__main__':

    instance = ObjectFactory.getType1Value1()
    print(instance)

    instance = ObjectFactory.getType1Value2()
    print(instance)

    instance = ObjectFactory.getType2Value1()
    print(instance)

    instance = ObjectFactory.getType2Value2()
    print(instance)
