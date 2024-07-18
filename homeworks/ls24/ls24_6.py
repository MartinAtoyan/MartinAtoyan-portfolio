def length_list(ls):
    if not ls:
        return 0

    return 1 + length_list(ls[1:])

print(length_list([1, 2, 3, 4]))  
