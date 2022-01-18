from itertools import chain

for one_item in chain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
    print(one_item)
