'''
    동물원 만들기
'''

from ex43 import Parrot, Sheep, Animal, Snake, Wolf
from ex44 import Cage


class Zoo:
    def __init__(self) -> None:
        self.cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def animals_by_color(self, color):
        return [one_animal for one_cage in self.cages for one_animal in one_cage.animals if one_animal.color == color]

    def animals_by_legs(self, legs):
        return [one_animal for one_cage in self.cages for one_animal in one_cage.animals if one_animal.legs == legs]

    def number_of_legs(self):
        return sum(one_animal.legs for one_cage in self.cages for one_animal in one_cage.animals)

    def __repr__(self) -> str:
        return '\n'.join(str(cage) for cage in self.cages)


if __name__ == '__main__':

    sheep = Sheep('white')
    parrot = Parrot('red')
    c1 = Cage(1)
    c1.add_animals(sheep, parrot)

    wolf = Wolf('black')
    snake = Snake('yellow')
    c2 = Cage(2)
    c2.add_animals(wolf, snake)

    z = Zoo()
    z.add_cages(c1, c2)

    print(z)

    print('*'*50)

    print(z.animals_by_color('white'))
    print(z.animals_by_legs(4))
    print(z.number_of_legs())
