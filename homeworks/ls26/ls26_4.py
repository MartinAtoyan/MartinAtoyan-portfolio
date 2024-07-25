def operation_with_data(data, operation='sum'):
    def sum(ls):
        res = 0
        for i in ls:
            res += i
        return res
    
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
    
    def product(ls):
        product = 1
        for num in data:
            product *= num
        return product
    
    if operation == 'sum':
        return sum(data)
    elif operation == 'max':
        return max(data) if data else None
    elif operation == 'min':
        return min(data) if data else None
    elif operation == 'average':
        return sum(data) / len(data) if data else 0
    elif operation == 'product':
        return product(data)
    else:
        print("We have some operations: sum, max, min, average, product")


numbers = [1, 2, 3, 4, 5]
print(operation_with_data(numbers))
print(operation_with_data(numbers, operation='max'))
print(operation_with_data(numbers, operation='min'))
print(operation_with_data(numbers, operation='average'))
print(operation_with_data(numbers, operation='product'))
