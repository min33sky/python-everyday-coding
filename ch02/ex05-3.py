'''
    구두점 처리하기
'''


def pig_latin():

    word = input('영어 단어를 입력하세요: ')
    endpoint = False

    if word[-1] == '.':
        endpoint = True

    if word[0] in 'aeiou':
        if endpoint:
            word = word[:-1] + 'way' + '.'
        else:
            word = word[:-1] + 'way'

    else:
        if endpoint:
            word = word[1:-1] + word[0] + 'ay' + '.'
        else:
            word = word[1:-1] + word[0] + 'ay'

    print(word)


if __name__ == '__main__':
    pig_latin()
