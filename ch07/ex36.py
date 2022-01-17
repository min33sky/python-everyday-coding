'''
    제마트리아(2)
'''

import string


def gematria_dict():

    return {
        char: index for index, char in enumerate(string.ascii_lowercase, 1)
    }


GEMATRIA = gematria_dict()


def gematria_for(word):
    return sum(GEMATRIA.get(one_char, 0) for one_char in word)


def gematria_equal_words(input_word):
    out_score = gematria_for(input_word.lower())
    return [word.strip() for word in open('words.txt') if gematria_for(word.lower()) == out_score]


if __name__ == '__main__':
    word = input('문자열을 입력하세요: ')
    print(gematria_equal_words(word))
