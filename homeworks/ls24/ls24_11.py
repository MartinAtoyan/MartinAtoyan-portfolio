def sum_of_digits(n):
    if n / 10 < 1:
        return n
    
    return n % 10 + sum_of_digits(int(n / 10))

print(sum_of_digits(58425)) 
