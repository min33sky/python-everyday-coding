'''
피그 라틴 단어 만들기
    - a,e,i,o,u로 끝나면 끝에 'way' 추가
    - 그 외단어로 시작하면 첫 글자를 마지막으로 이동, 끝에 'ay'추가
'''


def pig_latin():

    word = input('영어 단어를 입력하세요: ')

    if word[0] in 'aeiou':
        word += 'way'
    else:
        word = word[1:] + word[0] + 'ay'

    print(word)


if __name__ == '__main__':
    pig_latin()
