'''
    동물원의 동물 만들기
'''


class Animal:
    def __init__(self, color, legs) -> None:
        self.species = self.__class__.__name__
        self.color = color
        self.legs = legs

    def __repr__(self) -> str:
        return f'{self.color} {self.species}, {self.legs} legs'


class Sheep(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 4)


class Wolf(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 2)


if __name__ == '__main__':
    s = Sheep('white')
    p = Parrot('red')
    print(s)
    print(p)
