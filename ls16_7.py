n = int(input())
m = int(input())

matrix = []

for i in range(n):
    list = []
    for j in range(m):
        list.append(int(input()))
    matrix.append(list)

max = matrix[0][0]

for i in range(n):
    for j in range(m):
        if matrix[n - 1][m - 1] > max:
            max = matrix[n - 1][m - 1]

print(max)
