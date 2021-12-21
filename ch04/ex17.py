'''
    서로 다른 숫자의 개수 찾기
'''


def how_many_diffrent_numbers(arr):
    # 가장 쉬운 방법: set(arr)

    records = set()

    for item in arr:
        records.add(item)


    return len(records)


if __name__ == '__main__':
    numbers = [1, 2, 3, 1, 2, 3, 4, 1]
    print(how_many_diffrent_numbers(numbers))
