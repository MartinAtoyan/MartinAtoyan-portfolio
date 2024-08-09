def add(a, b):
    return a + b

def decorator(func):
    def wrapper(a, b):
        if a < 0 and b < 0:
             print("error")

        return func(a, b)

    return wrapper

add = decorator(add)

