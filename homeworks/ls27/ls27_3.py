def my_zip(*iterables):

    '''

    My_zip function is implementation of built-in zip function. It's combine element's from iterables and return in
    tuple form.

    '''

    min_size = len(iterables[0])

    for i in range(1, len(iterables)):
        if min_size > len(iterables[i]):
            min_size = len(iterables[i])

    ls = []

    for i in range(min_size):
        temp = []
        for j in iterables:
            temp.append(j[i])
        ls.append(tuple(temp))

    return ls

print(my_zip([1, 2], ['a', 'b', 'c']))
