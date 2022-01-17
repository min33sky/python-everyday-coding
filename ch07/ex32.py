'''
    딕셔너리 반전하기
'''

d = {'a': 1, 'b': 2, 'c': 3}


def flipped_dict(d):
    return {
        val: key for key, val in d.items()
    }


if __name__ == '__main__':
    print(flipped_dict(d))
