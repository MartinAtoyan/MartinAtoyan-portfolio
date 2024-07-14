string = "capitalize"
first_letter = string[0]
uppercase_first_letter = chr(ord(first_letter) - 32)
new_string = uppercase_first_letter + string[1:]
print(new_string)