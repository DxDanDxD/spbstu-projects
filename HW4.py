''' dz nomer

s = input(str())
c,m=0,0
for i in range(len(s)):
    if s[i]=='н':
        c+=1
    else:
        m=max(m,c)
        c=0
s=s.replace('н','!')
print(m, s)'''

'''dz nomer 2

s = input(str())
for i in '[{':
  s=s.replace(i,'(')
for i in '}]':
  s=s.replace(i,')')
for i in range(len(s)):
    if s[i]=='(':
        a=i
    elif s[i]==')':
        b=i
print(s[a+1:b])'''

'''dz nomer 3'''
s = input('Введите строку: ')
s=s.split()
a=''
for i in s:
    if (i[0].lower()=='а') and (i[-1]=='я'):
        a=a+i+' '
print(a)
