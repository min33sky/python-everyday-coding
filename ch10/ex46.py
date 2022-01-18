'''
    MyEnumerate 객체 만들기
'''


class MyEnumerate:
    def __init__(self, data) -> None:
        self.data = data

    def __iter__(self):
        # 이터러블과 이터레이터를 분리해서 인덱스 재사용 방지
        return MyEnumerateIterator(self.data)


# 이터레이터 (헬퍼클래스)
class MyEnumerateIterator:
    def __init__(self, data) -> None:
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = (self.index, self.data[self.index])

        self.index += 1

        return value


if __name__ == '__main__':
    e = MyEnumerate('abcd')

    for index, letter in e:
        print(f'{index}: {letter}')

    for index, letter in e:
        print(f'{index}: {letter}')
