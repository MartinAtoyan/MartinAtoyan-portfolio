def repeat_element(element, times):
    for _ in range(times):
        yield element

item = "Hello world"
object = repeat_element(item, 5)
print(next(object))
print(next(object))
print(next(object))
print(next(object))
print(next(object))
print(next(object))
