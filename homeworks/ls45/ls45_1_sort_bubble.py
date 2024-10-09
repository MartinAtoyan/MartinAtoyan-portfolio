ls = [5, 9, 10, 6, 8, 50, 36, 3]
size = len(ls) - 1

def swap_implement(x,y):
    x ^= y
    y ^= x
    x ^= y
    return x, y

a = 5
b = 10
# print(swap_implement(a,b))

for item in range(size):
    for i in range(size):
        if ls[i] > ls[i + 1]:
            ls[i] ^= ls[i + 1]
            ls[i + 1] ^= ls[i]
            ls[i] ^= ls[i + 1]

print(ls)
"""Bubble sort time complexity is O(n^2), because we have two loops in list."""
"""Bubble sort space complexity is O(1). It depends on length of list. """