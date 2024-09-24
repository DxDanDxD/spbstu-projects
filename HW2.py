'''dz nomer 1

x,y = int(input()), int(input())
if y!=0:
    print(x/y)
else:
    print('delenie na nol')'''

'''dz nomer 2

x=int(input())
if x>20:
    print(round(x*0.65 , 2), ' 35%')'''

'''dz nomer 3'''

m=int(input())
month=['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
if 1<=m<=12:
    print('Месяц -',month[m-1],'Время года - ', end='')
    if m==12 or 1<=m<=2:
        print('Зима')
    elif 3<=m<=5:
        print('Весна')
    elif 3<=m<=5:
        print('Лето')
    else:
        print('Осень')
else:
    print('Normalniye chisla vvodi!')