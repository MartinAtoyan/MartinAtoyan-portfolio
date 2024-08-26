def exception_propagator(iterable):
    for item in iterable:
        if item == "error":
            raise ValueError("An error occurred!")
        yield item

ls = ["asdsad", 12, 43, "error"]
object = exception_propagator(ls)

try:
    for item in object:
        print(item)
except ValueError as e:
    print(e)