ls = [1, 2, 3, 4, 5]

numbers_iterator = iter(ls)

while True:
    try:
        print(next(numbers_iterator))
    except StopIteration:
        break