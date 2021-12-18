'''
    우비두비 단어 만들기
    - 모음 (a,e,i,o,u) 앞에 ub를 붙인다.
'''


def ubbi_dubbi(sentense):
    output = []

    for word in sentense:
        if word in 'aeiou':
            output.append(f'ub{word}')
        else:
            output.append(word)

    return ''.join(output)


if __name__ == '__main__':
    sentense = 'octopus'
    print(ubbi_dubbi(sentense))
    sentense = 'elephant'
    print(ubbi_dubbi(sentense))
