import operator

'''
    튜플 레코드 출력하기
'''

PEOPLE = [('Donald', 'Trupm', 7.85), ('Vladimir',
                                      'Putin', 3.626), ('Jinping', 'xi', 10.603)]


def format_sort_records(list_of_tuples):
    output = []

    for person in sorted(list_of_tuples, key=operator.itemgetter(1, 0)):
        output.append(f'{person[1]:10} {person[0]:10} {person[2]:5.2f}')

    return '\n'.join(output)


if __name__ == '__main__':
    print(format_sort_records(PEOPLE))
