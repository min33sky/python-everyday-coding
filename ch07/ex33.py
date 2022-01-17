'''
    값 변환하기
'''

d = {'a': 1, 'b': 2, 'c': 3}


def transform_values(fn, d):
    return {
        key: fn(value)
        for key, value in d.items()
    }


if __name__ == '__main__':
    print(transform_values(lambda x: x*x, d))
