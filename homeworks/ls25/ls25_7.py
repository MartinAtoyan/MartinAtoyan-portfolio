def pow_of_two(n):
    if n <= 0:
        return False
    
    return n & 1 == 0

def pow_of_two_recursive(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    
    if n % 2 != 0:
        return False
    return pow_of_two_recursive(n // 2)

print(pow_of_two(16))
print(pow_of_two_recursive(17))


