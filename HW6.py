from random import randint

'''dz nomer 1

a=list()
for i in range(3):
  a.append([randint(0, 9) for x in range(3)])
for i in range(3):
  for j in range(3):
    print(a[i][j], end = ' ')
  print()
print('Max of column n.3: ', max([a[i][2] for i in range(3)]))
print('Max of column n.3', max(a[1]))'''

'''dz nomer 2

a=list()
n,m=3,3
for i in range(n):
  a.append([randint(-9, 9) for x in range(m)])
for i in range(n):
  for j in range(m):
    print(a[i][j], end = ' ')
  print()
for i in range(n):
  for j in range(m):
    if a[i][j]<0:
      a[i][j]=0
    else:
      a[i][j]=1
for i in range(n):
  for j in range(m):
    print(a[i][j], end = ' ')
  print()'''

'''dz nomer 3

a=list()
n=3
for i in range(n):
  a.append([randint(0, 9) for x in range(n)])
a=[[2,7,6],[9,5,1],[4,3,8]]
for i in range(n):
  for j in range(n):
    print(a[i][j], end = ' ')
  print()
s=sum(a[i])
status=True
for i in range(n-1):
  if sum(a[i])!=s:
    status=False
for i in range(n-1):
  if sum([a[j][i] for i in range(n)])!=s:
    status=False
if sum([a[i][i] for i in range(n)])!=s:
  status=False
if sum([a[i][n-i-1] for i in range(n)])!=s:
  status=False
print(status)'''

'''dz nomer 4

a=list()
n=3
for i in range(n):
  a.append([randint(0, 9) for x in range(n)])
a=[[1,2,3],[2,1,4],[3,4,1]]
for i in range(n):
  for j in range(n):
    print(a[i][j], end = ' ')
  print()
status=True
for i in range(n):
  for j in range(n):
    if a[n-j-1][i]!=a[i][n-j-1]:
      status=False
print(status)'''

'''dz nomer 5

a=list()
n,m=3,4
for i in range(n):
  a.append([randint(0, 9) for x in range(m)])
for i in range(n):
  for j in range(m):
    print(a[i][j], end = ' ')
  print()
summa=0
for i in range(n):
  if sum([a[i][j] for j in range(m)])>=summa:
    summa=sum([a[i][j] for j in range(m)])
    c=a[i]
print(c,summa)'''

'''dz nomer 6'''

a = list()
n, m = 3, 4
for i in range(n):
    a.append([randint(10, 99) for x in range(m)])
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    if min(a[i]) % 2 == 0:
        a[i][a[i].index(min(a[i]))] = 0
    else:
        a[i][a[i].index(min(a[i]))] = 1
print()
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
