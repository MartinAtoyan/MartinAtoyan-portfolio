def sum_elem_list(ls):
    res = 0
    for i in ls:
        if isinstance(i, list):
            res += sum_elem_list(i)
        else:
            res += i

    return res

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
res = sum_elem_list(nested_list)
print(res)
