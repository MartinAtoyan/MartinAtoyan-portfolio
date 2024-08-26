def custom_map(func, iterable):
    for item in iterable:
        yield func(item)


numbers = [1, 2, 3, 4, 5]
square = lambda x: x ** 2
object = custom_map(square, numbers)
for result in object:
    print(result)
