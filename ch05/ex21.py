import os

'''
    파일에서 가장 긴 단어 찾기
'''


def find_all_longest_words(dirname):
    return {
        filename: find_longest_word(os.path.join(dirname, filename)) for filename in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, filename))
    }


def find_longest_word(filename):
    longest_word = ''
    with open(filename, 'r', encoding='utf8') as f:
        for one_line in f:
            for one_word in one_line.split():
                if len(one_word) > len(longest_word):
                    longest_word = one_word
    return longest_word


if __name__ == '__main__':
    dirname = '/home/typemean/python-everyday-coding/text'
    print(find_all_longest_words(dirname))
