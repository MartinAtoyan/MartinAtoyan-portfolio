def max_of_three(a, b, c):
    def max_of_two(a, b):
        if a > b:
            return a
        else:
            return b
        
    return max_of_two(a, max_of_two(b, c))

print(max_of_three(5, 9, 2))
