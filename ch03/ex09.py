'''
    처음과 마지막 요소 찾기

'''


def firstlast(arg):
    return arg[:1] + arg[-1:]


if __name__ == '__main__':
    print(firstlast('abc'))
    print(firstlast([1, 2, 3, 4]))
    print(firstlast((1, 2, 3, 'a')))
