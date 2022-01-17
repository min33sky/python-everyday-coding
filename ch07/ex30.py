'''
    리스트 평탄화하기
'''


def flatten(lst):

    result = [num for elem in lst for num in elem]
    return result


if __name__ == '__main__':
    print(flatten([[1, 2], [3, 4]]))
