# 알파벳 순으로 단어 정렬 (소문자 우선)
print(sorted('This is a test string from Andrew'.split(), key=str.lower))

# 복잡한 객체 정렬하기

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

print(sorted(student_tuples, key=lambda student: student[2]))
