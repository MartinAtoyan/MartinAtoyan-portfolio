def print_elem_list(ls):
    if len(ls) == 0:
        return None
    print(ls[0])
    print_elem_list(ls[1:])

print_elem_list([1, 2, 3, 4, 5])