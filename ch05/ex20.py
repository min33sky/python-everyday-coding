'''
    글자 수 세기
'''


def make_wc(filename):
    counts = {
        'characters': 0,
        'words': 0,
        'lines': 0
    }
    unique_words = set()

    with open(filename, 'r', encoding='utf8') as f:
        for one_line in f:
            counts['lines'] += 1
            counts['characters'] += len(one_line)
            counts['words'] += len(one_line.split())
            unique_words.update(one_line.split())   # 이터러블을 매개변수로 받을 때 update()

    # 딕셔너리에 추가
    counts['unique words'] = len(unique_words)

    for key, value in counts.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    filename = 'wctest.txt'
    make_wc(filename)
