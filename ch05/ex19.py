'''
    /etc/passwd를 딕셔너리로 바꾸기
'''


def passwd_to_dict(filename):
    records = {}

    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith(('#', '\n')):
                tmp = line.split(':')
                records[tmp[0]] = tmp[2]

    return records


if __name__ == '__main__':
    filename = '/etc/passwd'
    print(passwd_to_dict(filename))
