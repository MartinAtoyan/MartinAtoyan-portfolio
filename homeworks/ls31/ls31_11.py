def custom_reduce(func, iterable, initalizer = None):
    it = iter(iterable)

    if initalizer == None:
        try:
            result = next(it)
        except StopIteration:
            raise TypeError("No value")
    else:
        result = initalizer

    yield result

    for i in it:
        result = func(result, i)
        yield result

ls = [1, 5, 7, 6, 2]
func = lambda x, y: x * y

object = custom_reduce(func, ls, 10)

for i in object:
    print(i)