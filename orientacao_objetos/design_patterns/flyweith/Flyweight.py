import json
from typing import Dict


class Flyweigth:
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")

class FlyweightFactory:
    _flyweights: Dict[str, Flyweigth] = {}

    def __init__(self, initial_flyweight: Dict) -> None:
        for state in initial_flyweight:
            self._flyweights[self.get_key(state)] = Flyweigth(state)

    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweigth:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print('FlyweightFactory: Cant find a flyweight, creation new one.')
            self._flyweights[key] = Flyweigth(shared_state)
        else:
            print('FlyweightFactory: Reusing existing flyweight.')

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f'FlyweightFactory: I have {count} flyweights:')
        print('\n'.join(map(str, self._flyweights.keys())), end="")

def add_car_to_police_database(factory: FlyweightFactory, plates: str,
                               owner: str, brand: str, model: str, color: str) -> None:
    print('\nClient: Adding a car to database.')
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


if __name__ == '__main__':
    factory = FlyweightFactory([
        ['Chevrolet', 'Camaro2018', 'pink'],
        ['Merceder Benz', 'C500' , 'black'],
        ['Merceder Benz', 'C300' , 'black'],
        ['BMW', 'M5', 'red'],
        ['BMW', 'X6', 'white'],
    ])

    factory.list_flyweights()

    add_car_to_police_database(factory, "CL234IR", 'James Doe', 'BMW', "M5", 'red')
    add_car_to_police_database(factory, "CL234IR", 'James Doe', 'BMW', "X1", 'red')

    print()

    factory.list_flyweights()
