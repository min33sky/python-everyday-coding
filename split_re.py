import re

s = 'abc   def  ghi '

print(s.split(' '))
# 매개변수를 전달하지 않으면 None을 전달 한 것과 같다. (공백 개수와 상관없이 공백으로 자른다)
print(s.split())

print(re.split(r'\W+', 'Words, words, words.'))
print(re.split(r'(\W+)', 'Words, words, words.'))
print(re.split(r'\W+', 'Words, words, words.', 1))
print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
