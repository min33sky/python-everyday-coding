# f-string

name = 'world'
first = 'Reuven'
last = 'Lerner'

print(f'Hello, {first:#<10} {last:#>10}')

# 이터러블을 매개변수로 전개하기


def spread(*arg):
    print(arg)


spread(*[1, 2, 3])  # 배열이 전개되서 인자로 전달
spread([1, 2, 3])   # 리스트 자체가 전달

# 문자열과 유니코드 숫자 변환
print(ord('a'))
print(chr(97))
