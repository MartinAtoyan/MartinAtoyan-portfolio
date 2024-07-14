string = input()

len_str = len(string)
result = ""

while len_str != 0 :
    result += string[len_str - 1]
    len_str -= 1

if result == string:
    print("Yes, it's palindrome")
else: 
    print("No, it's not palindrome")


