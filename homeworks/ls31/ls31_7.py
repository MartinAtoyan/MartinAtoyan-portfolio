def custom_range(start, end, step):
    a = start
    while a <= end:
        yield a
        a += step


object = custom_range(0, 5, 0.5)
for _ in range(50):
    print(next(object))