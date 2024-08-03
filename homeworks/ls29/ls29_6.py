ls = []
for i in range(1, 20, 3):
    ls.append(i)

fn = lambda x: x ** 2

print(list(map(fn, ls)))
