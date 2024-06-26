string = "banana"
a = 'a'
x = 'x'
result = ""
for i in range(len(string)):
    if string[i] != a:
        result += string[i]
    else: 
        result += x

print(result)
