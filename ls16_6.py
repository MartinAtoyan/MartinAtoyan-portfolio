n = int(input())
matrix = []
sum = 0
for i in range(0, n):
    list = []
    for j in range(0, n):
        list.append(int(input()))
    matrix.append(list)

for i in range(n):
    sum += matrix[n - i - 1][n - i - 1]
   
print(sum)


