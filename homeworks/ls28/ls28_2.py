def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter_1 = make_counter()

print(counter_1())
print(counter_1())
print(counter_1())
print(counter_1())
