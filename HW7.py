from functools import reduce

'''dz nomer 1'''
def read_last(lines, file):
    a = open('article.txt', 'r', encoding='utf-8')
    for i in range(lines):
        print(a.readline(), end='')

a = int(input())
f = open('article.txt', 'r', encoding='utf-8')
n = len(f.readlines())
if a>0 and a<n:
    read_last(a, f)

'''dz nomer 2'''

def print_docs(directory):
    a = os.walk(directory)
    for catalog in a:
        print(f'{catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)
print_docs('C:/Users/User/Downloads/2')

'''dz nomer 3'''

def longest_words(file):
    a = file.readlines()
    b = reduce(lambda x, y: x[:-1] + ' ' + y, a).split()
    c = max(map(len, b))
    return list(filter(lambda x: len(x) == c, b))
a = open('article.txt', 'r', encoding='utf-8')
print(longest_words(a))

'''dz nomer 4'''

a = input() + '.txt'
file = open(a, "w")
s = input() + '\n'
while len(s) > 1:
    file.write(s)
    s = input() + '\n'
print('Finished.')
