'''
    아이스크림 통 만들기
'''
from ex38 import Scoop


class Bowl():
    def __init__(self) -> None:
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)

    def __repr__(self) -> str:
        return '\n'.join(s.flavor for s in self.scoops)


if __name__ == '__main__':
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    print(b)
