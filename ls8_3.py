list = [1, 2, 3.14, "asd", 'a', True]
list_reserve = [] 
size = len(list)
for i in range(size):
    list_reserve.append(list[size - 1 - i])

print(list_reserve)
