def dig_one_to_five(x):
    if x < 1:
        return None
    dig_one_to_five(x - 1)
    print(x)

print(dig_one_to_five(5))
