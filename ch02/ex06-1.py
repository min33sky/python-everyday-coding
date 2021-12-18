'''
띄어쓰기로 구분되어 있는 문자열 리스트 기반으로 새로운 리스트 만들기
'''


def solution():
    lst = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    output = []

    for i in range(len(lst)):
        for idx, word in enumerate(lst[i].split()):
            if i == 0:
                output.append(word)
            else:
                output[idx] += ' ' + word

    print('output: ', output)


if __name__ == '__main__':
    solution()
