import operator

'''
    이름을 알파벳 순서로 정렬하기
'''

PEOPLE = [{
    'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.li'
}, {
    'first': 'Donald', 'last': 'Trump', 'email': 'president@lerner.co.li'
}, {
    'first': 'Vladimir', 'last': 'Putin', 'email': 'president@lerner.co.li'
},
]


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))

if __name__ == '__main__':
    print(alphabetize_names(PEOPLE))
