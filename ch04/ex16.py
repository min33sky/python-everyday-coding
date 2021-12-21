'''
    두 딕셔너리의 차이 찾기
'''


def dictdiff(dict1, dict2):
    diff = {}

    all_keys = dict1.keys() | dict2.keys()

    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            diff[key] = [dict1.get(key), dict2.get(key)]

    return diff


if __name__ == '__main__':
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    print(dictdiff(d1, d2))

    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}
    print(dictdiff(d3, d4))

    d5 = {'a': 1, 'b': 2, 'd': 4}
    print(dictdiff(d1, d5))
