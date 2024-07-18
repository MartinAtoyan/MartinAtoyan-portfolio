def sum(x):
    if x < 1:
        return x
    return x + sum(x - 1)

n = int(input())
print(sum(n))