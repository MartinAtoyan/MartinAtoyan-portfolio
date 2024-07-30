def apply_function(iterable, function):
    result = []
    for item in iterable:
        result.append(function(item))
    return result

def square(n):
    return n ** n

print(apply_function([1, 2, 3], square))

