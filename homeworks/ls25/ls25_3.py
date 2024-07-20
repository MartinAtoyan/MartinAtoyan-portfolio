def is_sorted(ls):
    if len(ls) <= 1:
        return True

    return ls[0] < ls[1] and is_sorted(ls[1:])

list_unsorted = [1, 3, 4, 7, 2]
list_sorted = [1, 2, 3, 4, 5]

print(is_sorted(list_unsorted))
print(is_sorted(list_sorted))
