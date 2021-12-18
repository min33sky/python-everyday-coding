
def solution(*args):
    sum = 0
    for item in args:
        sum += int(item)
    print(sum)


def mysum():
    solution(10, 20, 30)


if __name__ == '__main__':
    mysum()
