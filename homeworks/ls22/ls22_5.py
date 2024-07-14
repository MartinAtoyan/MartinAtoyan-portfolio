def first_uppercase_letter(string, n):
    for i in range(n):
        if string[i] >= "A" and string[i] < "Z":
            return string[i]

string = "kjhdsFsASdbn"
len_s = len(string)
print(first_uppercase_letter(string, len_s))
