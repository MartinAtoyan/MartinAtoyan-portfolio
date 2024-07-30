def my_map(func, iterable):
    """ My_map function has two parameters. First parameters is function
    that return one value, second parameter is an iterable. Every value of iterable
    my_map put in first parameter and returned all values in list. """

    length_of_iterable = len(iterable)
    result = []
    for i in range(length_of_iterable):
        res = iterable[i]
        result.append(func(res))
    return result

def square(x):
    return x * x

ls = [10, 52, 1, 2, 3, 4]

print(my_map(square, ls))