'''
    마지막 줄 추출하기
'''


def get_final_line(filename):
    final_line = ''

    with open(filename, 'r', encoding='utf8') as f:
        for current_line in f:
            final_line = current_line

    print(final_line, end='')


if __name__ == '__main__':
    # filename = 'README.md'
    filename = '/etc/passwd'
    get_final_line(filename)
