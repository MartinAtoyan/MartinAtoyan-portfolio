list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []
for num in list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
result = even + odd

print(result) 


