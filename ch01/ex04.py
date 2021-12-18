'''
16진수 출력하기
'''


def hex_output():
    decnum = 0

    hexnum = input('변환 할 16진수를 입력하세요 (숫자만 입력):')

    # 진법 계산하기 편하게 하기 위해 reversed()로 뒤집어서 계산
    for idx, num in enumerate(reversed(hexnum)):
        decnum += int(num, 16) * (16 ** idx)

    print('변환 값: ', decnum)


def solution():
    hex_output()


if __name__ == '__main__':
    solution()
