def my_filter(function, iterable):
    '''

    my_filter function similar filter built-in function.
    Function has two parameters.
    1: function
    2: iterable
    If iterable's item in function is true, this item added to other list. Function does this with all items and
    in the end return's list of iterable's items that requires function.

    '''

    result = []
    for i in range(len(iterable)):
        if function(iterable[i]):
            result.append(iterable[i])
    return result

print(my_filter(lambda x: x > 0, [1, -2, 3, 0, -1, 2]))

