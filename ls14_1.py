string = "find the letter z"
z = "z"
index = 0

for i in range(len(string)):
    if string[i] != z:
        index += 1
    else:
        break

if string[index] == z:
    print(index)
else:
    print("Character not found")



        

