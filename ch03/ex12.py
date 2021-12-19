from collections import Counter

'''
    특정 글자를 가장 많이 가진 단어 찾기
'''


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)


if __name__ == '__main__':
    words = ['this', 'is', 'an', 'elementary', 'test', 'example']
    print(most_repeating_word(words))
