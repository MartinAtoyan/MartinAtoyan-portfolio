
# square, cube, square root, factorial)

def square(number):
    return number * number

def cube(number):
    return number * number * number

def square_root(number):
    return number ** 0.5

def factorial(number):
    temp = 1
    for i in range(1, number + 1):
        temp *= i
    return temp
def math_operations(number, operation):
    dict = {
        "square": square,
        "cube": cube,
        "square_root": square_root,
        "factorial": factorial
    }
    if operation in dict.keys():
        return dict[operation](number)

print(math_operations(5, "square"))
print(math_operations(5, "cube"))
print(math_operations(25, "square_root"))
print(math_operations(5, "factorial"))