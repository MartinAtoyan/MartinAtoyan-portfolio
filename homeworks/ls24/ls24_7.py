def reserve_string(string):
    if len(string) <= 0:
        return string
    
    return string[-1] + reserve_string(string[:-1])

print(reserve_string("abcd"))