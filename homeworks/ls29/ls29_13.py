def bar(n):
    def mul(x):
        return x * n
    ls = []
    for i in range(n):
        ls.append(mul(i))
    return ls

funcs = bar(8)
