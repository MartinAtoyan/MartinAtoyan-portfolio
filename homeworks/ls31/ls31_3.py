def infinity():
    a = 1
    while True:
        yield a
        a += 1

object = infinity()
for _ in range(10):
    print(next(object))