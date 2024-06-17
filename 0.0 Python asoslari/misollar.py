#3-masala: Uchburchak 
'''
s, h = list(map(int, input().split()))
print(f'{(s / h * 2):.2f}')
'''

#4-masala: Shar
'''
import math

r = int(input())

print(f'{(4 * math.pi * r ** 2):.2f}')
'''

#5-masala: Perimetr
'''
a, b, c = list(map(int, input().split()))
print(f'{((a + b + c) / 2):.2f}')
'''

#7-masala: Konus
'''
import math
h, r = list(map(int, input().split()))
v = 1/3 * h * r **2 * math.pi
print(f'{v:.2f}')
'''

#8-masala: Vaqt
'''
v, s = list(map(int, input().split()))
t = s / v
print(f'{t:.2f}')
'''

#9-masala: Erkin tushish
'''
import math
h = int(input())
t = math.sqrt(2 * h / 9.8)
print(f'{t:.2f}')
'''

#10-masala: Arifmetika
'''
x = int(input())
l = (x * 365 * 24 * 60 * 60) / 1000
print(int(l))
'''

#11-masala: Summa
'''
n = int(input())
print(int(n * (n+1) / 2))
'''

#12-masala: 
'''
from math import *

#foydalanuvchi bir nechta ma'lumotlar kirita olishi uchun
x, y = list(map(float, input().split())) 

x, y = [5.49, 6.51]

A = x + y
B = y ** 2 + abs((y * y + 2) / (x + x **3 + 5))
C = exp(y + 2)

c1 = A / B + C

print(f'{c1:.2f}')
'''

'''
from math import *

x, y = list(map(int, input().split())) 

A = pow((x + y), 2) + sqrt(abs(y) + 2) - (x - (x * y) / ((x * x) / 2 - 5))
B = pow(cos(x + y), 2) / pow((x + y), 1/3)

z = log(abs(A)) + B

print(f'{z:.2f}')
'''
