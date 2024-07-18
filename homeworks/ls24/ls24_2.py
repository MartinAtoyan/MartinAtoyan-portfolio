def dig_five_to_one(x):
    if x < 1:
        return None
    print(x)
    dig_five_to_one(x - 1)

print(dig_five_to_one(5))