import pathlib

p = pathlib.Path('/home/typemean/python-everyday-coding/text')

for one_filename in p.iterdir():
    print(one_filename)

print('*'*100)

for one_filename in p.glob('pg*.txt'):
    print(one_filename)
