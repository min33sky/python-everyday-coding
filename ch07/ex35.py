'''
    제마트리아(1)
'''


import string


def gematria_dict():

    return {
        char: index for index, char in enumerate(string.ascii_lowercase, 1)
    }


if __name__ == '__main__':
    print(gematria_dict())
