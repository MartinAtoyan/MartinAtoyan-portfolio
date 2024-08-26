def custom_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        try:
            yield tuple(next(it) for it in iterators)
        except StopIteration:
            break



list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

print("Test 1:")
for item in custom_zip(list1, list2):
    print(item)

list3 = [10, 20, 30, 40, 50]
list4 = ['x', 'y', 'z']
list5 = [100, 200]

for item in custom_zip(list3, list4, list5):
    print(item)
