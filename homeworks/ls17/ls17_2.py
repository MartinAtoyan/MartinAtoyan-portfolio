n = int(input())

matrix = []

for i in range(n):
    list = []
    for j in range(n):
        list.append(int(input()))
    matrix.append(list)

res = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        res[i][j] = matrix[n - i - 1][n - j - 1]

for i in range(n):
    for j in range(n):
        print(res[i][j], end=" ")
    print()



