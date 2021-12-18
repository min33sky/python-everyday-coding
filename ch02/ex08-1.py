'''
    문자열 정렬하기
'''


def strsort(word):
    print(', '.join(sorted(word.split())))


if __name__ == '__main__':
    word = 'Tom Dick Harry'
    strsort(word)
