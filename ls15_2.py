list = [1, 2, 10, 3, 4, 5]
elem = 10
index = 0

for i in list:
    if elem != i:
        index += 1
    else:
        break

for i in list:
    if elem != i:
        print("error")


temp = list[ : index ]
temp1 = list[index + 1:]

for i in temp1:
    temp.append(i)

list = temp

print(list)
