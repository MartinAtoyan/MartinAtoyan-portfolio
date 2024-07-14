def sum_of_digits(n):
    sum = 0
    while(n != 0):
        temp = int(n % 10)
        sum += temp
        n /= 10
    return sum

n = int(input())
print()
res = sum_of_digits(n)
print(res)      