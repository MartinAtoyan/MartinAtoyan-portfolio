import math
def calculate_area(shape, **kwargs):
    if shape == "circle":
        ls = list(kwargs.values())
        return 3.14 * (ls[0] ** 2)
    elif shape == "square":
        ls = list(kwargs.values())
        return ls[0] ** 2
    elif shape == "rectangle":
        ls = list(kwargs.values())
        return ls[0] * ls[1]
    elif shape == "triangle":
        ls = list(kwargs.values())
        s_2 = sum(ls) / 2
        return math.sqrt(s_2 * (s_2 - ls[0]) * (s_2 - ls[1]) * (s_2 - ls[2]) )
    else:
        return "please give to function other shape (# circle, square, rectangle, triangle)"

print(calculate_area("circle", r = 3))
print(calculate_area("square", r = 3))
print(calculate_area("rectangle", a = 3, b = 4))
print(calculate_area("triangle", a = 3, b = 4, c = 5))

