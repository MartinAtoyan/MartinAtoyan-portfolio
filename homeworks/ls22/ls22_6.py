def max(ls):
    max = ls[0]
    for i in ls:
        if i > max:
            max = i
            return max
        
def min(ls):
    min = ls[0]
    for i in ls:
        if i < min:
            min = i
            return min
        
list = [154, 200, 3, 4, 5, 10]
print(f"The maximum element of list is {max(list)}")
print(f"The minimum element of list is {min(list)}")