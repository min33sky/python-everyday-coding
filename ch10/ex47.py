'''
    순환하는 이터레이터 만들기
'''


class Circle:
    def __init__(self, data, max_times) -> None:
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        n = len(self.data)
        return (self.data[x % n] for x in range(self.max_times))


if __name__ == '__main__':
    c = Circle('abc', 5)
    print(list(c))
