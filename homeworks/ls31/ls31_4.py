def gen_squares():
    a = 1
    while a <= 20:
        yield a * a
        a += 1

object = gen_squares()
for _ in range(1, 21):
    print(next(object))