
def solution(num_list, *start):
    if start:
        sum = start[0]
    else:
        sum = 0

    for num in num_list:
        sum += num

    print(sum)


def mysum():
    solution([10, 20, 30])
    solution([10, 20, 30], 4)


if __name__ == '__main__':
    mysum()
