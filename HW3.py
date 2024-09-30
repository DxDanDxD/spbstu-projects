'''DZ1'''

n = int(input())
s=0
if n<=100:
    for i in range(n+1):
        s+=i**3
print(s)

'''DZ2'''

l=''
for i in range(1,10):
    for j in range(1,10):
        if i*j<10:
            l+=' '
        l+=(str(i*j)+' ')
    print(l)
    l=''


'''DZ3'''

l=''
for i in range(9,0,-1):
    for j in range(1,10):
        if i*j<10:
            l+=' '
        l+=(str(i*j)+' ')
    print(l)
    l=''