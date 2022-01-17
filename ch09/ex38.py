'''
    아이스크림 스쿱 만들기
'''


class Scoop():
    def __init__(self, flavor) -> None:
        self.flavor = flavor


def create_scoop():
    scoops = [Scoop('chocolet'), Scoop('vanilla'), Scoop('persimmon')]

    for scoop in scoops:
        print(scoop.flavor)


if __name__ == '__main__':
    create_scoop()
