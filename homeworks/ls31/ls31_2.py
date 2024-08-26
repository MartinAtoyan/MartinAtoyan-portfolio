def prime_generator(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(2, n):
        if is_prime(i):
            yield i

for prime in prime_generator(100):
    print(prime)
