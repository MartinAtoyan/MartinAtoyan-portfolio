ls = [5, 9, 10, 6, 8, 50, 36, 3]
size = len(ls)

for i in range(size):
    min_ind = i
    for j in range(i + 1, size):
        if ls[min_ind] > ls[j]:
            min_ind = j

    ls[i], ls[min_ind] = ls[min_ind], ls[i]

print(ls)

"""Time complexity O(n^2)"""
"""Space complexity O(1)"""