n = 3
index = 2
list = [1, 2, 4, 5]
    
temp = list[index:]
list[index] = n

for i in range(len(temp)):
    list.append(temp[i])

print(list)


