def fib_number(n):
    if n == 0 or n == 1:
        return n
    
    return fib_number(n - 1) + fib_number(n - 2)

n = int(input())
print(fib_number(n))
