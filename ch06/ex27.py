'''
    비밀번호 생성기
'''
import random


def create_password_generator(s):

    def create_password(length):
        result = []

        for _ in range(length):
            result.append(random.choice(s))

        return ''.join(result)

    return create_password


if __name__ == '__main__':
    alpha_password = create_password_generator('abcdef')
    symbol_password = create_password_generator('!@#$%')

    print(alpha_password(5))
    print(alpha_password(10))

    print(symbol_password(5))
    print(symbol_password(10))
