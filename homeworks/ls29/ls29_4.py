def compose(f, g):
    def res(x):
        return f(g(x))
    return res

def add_1(x):
    return x + 1

def sub_3(x):
    return x - 3

print(compose(add_1, sub_3)(5))
