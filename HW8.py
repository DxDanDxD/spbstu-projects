import re
from functools import reduce

'''dz nomer 1

s=input()
while s!='':
    if re.fullmatch(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}', s):
        print('Car id number:')
    elif re.fullmatch(r'[А-Я]{2}\d{4,5}', s):
        print('Taxi id number:')
    else:
        print('Not an id number.')
    s=input()'''

'''dz nomer 2

a = open('Занятие_8_Текст.txt', 'r', encoding='utf-8')
s = a.readlines()
b = reduce(lambda x,y:  x[:-1]+' '+y, s).split()
print(b)
print(list(filter(lambda x: re.fullmatch(r'\b[А-Яа-яёЁ]+[-]?[А-Яа-яёЁ]+\b',x) or re.fullmatch(r'\b[A-Za-z]+[-]?[A-Za-z]+\b',x), b)))'''

'''dz nomer 3

s='Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.'
s=s.split()
a=list(filter(lambda x: re.search(r'\b(0[0-9]|1[0-9]|2[0-4])[:](0[0-9]|[0-9]{2})\b',x) ,s))
s= reduce(lambda x,y:  x+' '+y, s)
for i in a:
    s=s.replace(i,'(TBD)',1)
print(s)'''

'''dz nomer 4'''


s='Владимир устроился на работу в одно очень важное место. И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. '
x=re.findall(r'\b[А-ЯЁ][А-ЯЁ ]*[А-ЯЁ]\b',s)
print(x)