def flatten_list(ls):
    nes_ls = []
    for i in ls:
        if isinstance(i, list):
            nes_ls.extend(flatten_list(i))
        else:
            nes_ls.append(i)

    return nes_ls

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flattened = flatten_list(nested_list)
print(flattened)
