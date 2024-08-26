def fib(n):
    a_1 = 0
    a_2 = 1
    for i in range(n):
        yield a_2
        a_1, a_2 = a_2, a_1 + a_2


object = fib(5)
print(next(object))
print(next(object))
print(next(object))
print(next(object))
print(next(object))
print(next(object))


