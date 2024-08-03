def make_accumulator(start=0):
    def add_arg(n):
        return start + n
    return add_arg


print(make_accumulator(5)(2))
print(make_accumulator(4)(6))
