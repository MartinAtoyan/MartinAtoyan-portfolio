def sorting(ls):
    return sorted(ls)

def reversing(ls):
    return reversed(ls)

def filtering(ls, func):
    return filter(func, ls)

def mapping(ls, func):
    return map(ls, func)

def transform_list(lst, operation):

    dict = {
        "sorting": sorting,
        "reversing": reversing,
        "filtering": filtering,
        "mapping": mapping
    }

    if operation in dict.keys():
        return dict[operation](lst)

