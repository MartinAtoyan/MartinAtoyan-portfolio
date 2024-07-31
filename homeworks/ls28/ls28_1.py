def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

make_multiplier_of3 = make_multiplier_of(3)
print(make_multiplier_of3(7))

make_multiplier_of4 = make_multiplier_of(4)
print(make_multiplier_of4(5))
