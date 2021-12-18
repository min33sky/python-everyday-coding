'''
'''


def pig_latin():

    word = input('영어 단어를 입력하세요: ')

    # 첫 글자가 대문자라면 변환 뒤에도 형태를 유지시키기
    if word[0].isupper() == True:
        is_upper = True

    if word[0] in 'aeiou' or word[0] in 'AEIOU':
        word += 'way'
    else:
        word = word[1:] + word[0] + 'ay'

    if is_upper:
        word = word[0].upper() + word[1:]

    print(word)


if __name__ == '__main__':
    pig_latin()
