import math
n = int(input())
List = []

for i in range(n):
    elem = int(input())
    List.append(elem)

max = List[0]
min = List[0]
index_max = 0
index_min = 0

for i in range(n):
    if List[i] > max:
        max = List[i]
for i in range(n):
    if List[i] < min:
        min = List[i]

for i in range(n):
    if List[i] != max:
        index_max += 1
    else:
        break

for i in range(n):
    if List[i] != min:
        index_min += 1
    else:
        break

result = abs(index_min - index_max)
print(result)


