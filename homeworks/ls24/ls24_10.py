def is_polindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return is_polindrome(string[1:-1])
    else:
        return False    

print(is_polindrome("abcdedcba"))    