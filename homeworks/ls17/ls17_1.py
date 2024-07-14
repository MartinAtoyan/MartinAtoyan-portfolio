
matrix = [[1, 2, 3]       
         ,[4, 5, 6]
         ,[7, 8, 9]]

m = len(matrix[0])
n = len(matrix)


res = [[None for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        res[i][j] = matrix[j][i]


for i in range(n):
    for j in range(m):
        print(res[i][j], end=" ")
    print()

