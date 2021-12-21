'''
    마지막 줄 추출하기
'''


def get_final_line():
    with open('README.md', 'r', encoding='utf8') as f:
        for current_line in f:
            print(current_line)


if __name__ == '__main__':
    get_final_line()
