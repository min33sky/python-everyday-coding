from collections import Counter

# Counter는 dict를 상속받아 만들어졌다. 그래서 dict가 할 수 있는 것이 모두 가능하다
print(Counter('abcabcabbbc'))

# 가장 많이 등장하는 글자부터 출력하기
print(Counter('abcabcabbbc').most_common())

# 출력할 튜플 개수 지정
print(Counter('abcabcabbbc').most_common(1))
print(Counter('abcabcabbbc').most_common(2))
