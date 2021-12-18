'''
피그 라틴 문장 만들기
'''


def pl_sentence(sentence):
    output = []

    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(output)


if __name__ == '__main__':
    sentence = 'this is a test translation'
    print(pl_sentence(sentence))
