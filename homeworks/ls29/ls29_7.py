ls = []
for i in range(1, 55):
    ls.append(i)

fn = lambda x: x % 2 == 0

print(list(filter(fn, ls)))