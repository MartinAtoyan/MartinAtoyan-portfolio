def apply_twice(f, x):
    res1 = f(x)
    res2 = f(res1)
    return res2

def add_1(x):
    return x + 1

print(apply_twice(add_1, 6))
