'''
    모든 모음을 포함하는 단어 찾기
'''


vowels = {'a', 'e', 'i', 'o', 'u'}


def get_sv(file_name):

    with open(file_name, 'r') as f:
        return {word.strip() for word in f if vowels < set(word)}


if __name__ == '__main__':
    print(get_sv('words.txt'))
