from decimal import *


def solution(prime, before, after):
    lst = str(prime).split('.')
    print(f'{lst[0][-before:]}.{lst[1][:after]}')


solution(1234.5678, 2, 3)

# Decimal 클래스 활용해서 부동소수점 계삭 하기
print(0.1 + 0.2)
print(Decimal('0.1') + Decimal('0.2'))
