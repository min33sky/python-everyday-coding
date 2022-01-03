'''
    전위 표기법 계산기 만들기
'''

import operator


def calc(op_str):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod
    }

    op, first, second = op_str.split()
    first = int(first)
    second = int(second)

    return operations[op](first, second)


print(calc('+ 2 3'))
