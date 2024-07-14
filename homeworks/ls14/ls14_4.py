string = "reverse me"
len_string = len(string)
result = ""
while len_string != 0 :
    result += string[len_string - 1]
    len_string -= 1
print(result)
