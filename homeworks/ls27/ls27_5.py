def get_nth_element(iterable, n):

    iterator = iter(iterable)
    for _ in range(n):
        try:
            next(iterator)
        except StopIteration:
            print("finish")
    try:
        return next(iterator)
    except StopIteration:
        print("finish 2")

ls = [1, 2, 3, 4, 5]
print(get_nth_element(ls, 2))
