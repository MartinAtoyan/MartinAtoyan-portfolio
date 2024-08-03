def add_maker(n):
    def adder(x):
        return x + n
    return adder

print(add_maker(5)(3))