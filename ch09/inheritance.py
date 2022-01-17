from unicodedata import name


class Person():
    def __init__(self, name) -> None:
        self.name = name

    def greet(self):
        return f'Hello, {self.name}'


class Employee(Person):
    def __init__(self, name, id_number) -> None:
        super().__init__(name)
        self.id_number = id_number
