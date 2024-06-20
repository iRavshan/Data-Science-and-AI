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
'''
