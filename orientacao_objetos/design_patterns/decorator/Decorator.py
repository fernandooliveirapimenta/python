class Component:
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return 'ConcreteComponent'


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f'ConcreteDecoratorA({self._component.operation()})'


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f'ConcreteDecoratorB({self._component.operation()})'

def client_code(component: Component) -> None:
    print(f'RESULT: {component.operation()}', end='')


if __name__ == '__main__':
    simple = ConcreteComponent()
    print('Client: Ive got a simple component:')
    client_code(simple)
    print()

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print('Client: Now i got a decorator component:')
    client_code(decorator2)
