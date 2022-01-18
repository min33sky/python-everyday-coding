'''
    동물 우리 만들기
'''


from ex43 import Parrot, Sheep


class Cage:

    def __init__(self, id_number) -> None:
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self) -> str:
        output = f'Cage {self.id_number}\n'
        output += '\n'.join(
            '\t' + str(animal) for animal in self.animals
        )
        return output


if __name__ == '__main__':
    sheep = Sheep('white')
    parrot = Parrot('red')
    c1 = Cage(1)
    c1.add_animals(sheep, parrot)

    print(c1)
