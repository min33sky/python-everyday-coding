import random


def guessing_game():

    answer = random.randint(0, 100)

    print('정답: ', answer)

    while True:
        number = input('1~100 숫자를 입력하세요: ')

        # ? 숫자로 변환 가능한 문자열인지 체크
        if not str.isdigit(number):
            print('숫자를 입력해주세요!!')
            continue
        else:
            number = int(number)

        if answer == number:
            print('Just right')
            break
        elif answer > number:
            print('Too low')
        elif answer < number:
            print('Too high')


if __name__ == '__main__':
    guessing_game()
