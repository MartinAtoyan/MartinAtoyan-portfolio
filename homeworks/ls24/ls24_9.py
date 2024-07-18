def print_char_of_string(string):
    if len(string) <= 0:
        return string
    
    print(string[0])
    string = string[1:]
    print_char_of_string(string)

print_char_of_string("abcd")