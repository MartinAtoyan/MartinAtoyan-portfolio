def power_factory(n):
    def arg(x):
        return x ** n
    return arg

print(power_factory(3)(2))