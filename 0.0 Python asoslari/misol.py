'''
x = int(input())


def print_number(n=1):
    if n == 1:
        print(n)
    else:
        print(n, end=' ')
        print_number(n-1)

print_number(n)


def f(n):
    if n == -2:
        return 3
    elif n == -3:
        return 4
    elif n % 2 == 0:
        return 3 * f(2*n-2) + 5*f(n/2+1)
    else:
        return f(n+1) - f(n-3)

print(f(x))  


s = input()

raqamlar = (1, 2, 3, 4, 5, 6, 7, 8, 9)
summa = 0

s = s.replace('0', '')

for r in s:
    summa += raqamlar[int(r) - 1] * s.count(r)
    s = s.replace(r, '')

print(summa)
'''

'''
x, y = list(map(float, input().split()))
print(max(x, y), min(x, y))

x, y, z = list(map(float, input().split()))

print(f'{max(x+y+z, x, y, z):.2f}', f'{(min(x+y/2.0, x, y, z) ** 2):.2f}')


from math import *

x, y, a, b= list(map(int, input().split()))

s=0
p=1
sp=0
sp_sub=1

for j in range(1, x +1):
    s += (j ** 2 + 2 * j) /(j ** 3 + j * cos(j) ** 2 +1)
 
for m in range(1, y +1):
    p *= (m ** 2 + 1) / (pow(m, 3/m) + 2)
 
for i in range(1, a+1):

    for k in range(1, b+1):
        sp_sub *= log((pow(k, i) + pow(k, 1/i)) / (pow(k, 3) + pow(i, 1/k)))

    sp += sp_sub
    sp_sub = 1

print(f'{s:.2f}', f'{p:.2f}', f'{sp:.2f}')
'''

a = float(input())

if a <= -1:
    print(f'{(-1 * a - 1):.2f}')
elif a >= -1 and a <= 0:
    print(f'{(a + 1):.2f}')
elif a >= 0 and a <= 1:
    print(f'{(-1 * a + 1):.2f}')
else:
    print(f'{(a - 1):.2f}') 