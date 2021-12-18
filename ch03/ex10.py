'''
    아무것이나 더하기
'''


def mysum(*items):
    if not items:
        return items

    # ? 첫 번째 요소로 초기화하면 자료형도 같이 따라간다.
    output = items[0]

    for item in items[1:]:
        output += item

    return output


if __name__ == '__main__':
    print(mysum())
    print(mysum('abc', 'def'))
    print(mysum([1, 2, 3], [4, 5, 6], [70, 80]))
