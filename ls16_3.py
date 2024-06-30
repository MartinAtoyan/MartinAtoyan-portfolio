n = int(input())
matrix = []

for i in range(0, n):
    list = []
    for j in range(0, n):
        list.append(int(input()))
    matrix.append(list)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print()



