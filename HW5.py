import math

'''dz nomer 1'''


def f(x, y):
    return math.degrees(math.atan(x / y))


x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())
z1, z2 = map(float, input().split())
print(f(x1, x2))
print(f(y1, y2))
print(f(z1, z2))

'''dz nomer 2'''


def F1(n):
    a = bin(n)[2:]
    a1 = a[:(len(a)) // 2]
    a2 = a[(len(a) - 1) // 2 + 1:]
    return a1[::-1] == a2


def F2(n):
    a = n
    b = 2
    if n == 1:
        return False
    else:
        while b <= n // 2:
            if n % b == 0:
                a = 0
            b += 1
        if a == 0:
            return False
        else:
            return F1(a)


n = int(input())
m = []
for i in range(0, n + 1):
    if f(i) == True:
        m.append(i)
print(m)
