'''
    숫자 더하기
'''


def sum_numbers(numbers):
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())


if __name__ == '__main__':
    input1 = input('문자열을 입력하세요: ')
    print(sum_numbers(input1))
