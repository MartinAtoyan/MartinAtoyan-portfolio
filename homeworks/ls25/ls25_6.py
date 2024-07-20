def fibonacci(n):
    def fib(n, a = 0, b = 1):
        if n == 0:
            return []
        return [a] + fib(n - 1, b, a + b)

    return fib(n)


print(fibonacci(5))  
print(fibonacci(10)) 