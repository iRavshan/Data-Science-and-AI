#131 - masala
'''
n, m = list(map(int, input().split()))

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    print(sum(matrix[i]), end=' ')

max = matrix[0][0]
min = max

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
        if matrix[i][j] < min:
            min = matrix[i][j]

print()
print(max, min)

#133 - masala

n = int(input())

matrix = []

for i in range(2*n):
    row = list(map(int, input().split()))
    matrix.append(row)


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    for j in range(n):
        print(matrix[i+1][j], end=' ')
    print()
'''   

#137 - masala
n = int(input())

matrix = []
vector = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

m = int(input())

for i in range(n):
    for j in range(n):
        if matrix[i][j] % m == 0:
            vector.append(matrix[i][j])

ortacha = sum(vector) / len(vector)

print(f'{ortacha:.2f}')



