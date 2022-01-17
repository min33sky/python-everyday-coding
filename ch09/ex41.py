'''
    더 큰 아이스크림 통 만들기
'''

from ex38 import Scoop


class Bowl():
    max_scoops = 3

    def __init__(self) -> None:
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self) -> str:
        return '\n'.join(s.flavor for s in self.scoops)


class BigBowl(Bowl):
    max_scoops = 5


if __name__ == '__main__':
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    s4 = Scoop('kiwi')
    s5 = Scoop('lemon')

    b = Bowl()
    bb = BigBowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.add_scoops(s4, s5)
    bb.add_scoops(s1, s2)
    bb.add_scoops(s3)
    bb.add_scoops(s4, s5)
    print(b)
    print('**************')
    print(bb)
