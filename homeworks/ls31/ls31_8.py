ls = []
for i in range(1, 51):
    ls.append(i)

even = (num for num in ls if num % 2 == 0)
for item in even:
    print(item)
