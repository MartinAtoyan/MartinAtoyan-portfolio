list = ["ab", "abde", "kopggj", "asdqqwe"]
max = len(list[0])
index = 0
for i in range(len(list)):
    if len(list[i]) > max:
        max = len( list[i] )
    index = i

print(index, list[index])
