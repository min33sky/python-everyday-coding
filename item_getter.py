import operator

s = 'abcdef'
t = (10, 20, 30, 40, 50, 60)

# ? itemgetter(): 해당 인덱스의 값을 튜플로 반환하는 함수를 리턴한다
get_2_and_4 = operator.itemgetter(2, 4)
print(get_2_and_4(s))
print(get_2_and_4(t))
