string = "hello, world! are you ready ?"

result = ""
cap_flag = True 

for i in string:
    if cap_flag and 'a' <= i <= 'z':
        result += chr(ord(i) - 32)
    else:
        result += i

    if i in ' .?!':
        cap_flag = True
    else:
        cap_flag = False

print(result)
