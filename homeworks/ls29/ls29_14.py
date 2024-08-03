def calculate(operand1, operand2, operator):
    if operator == "/" and operand2 == 0: print("ZerodivisionError")

    def add(operand1, operand2):
        return operand1 + operand2

    def sub(operand1, operand2):
        return operand1 - operand2

    def mul(operand1, operand2):
        return operand1 * operand2

    def div(operand1, operand2):
        if operand2 == 0: return ZeroDivisionError
        return operand1 / operand2

    dict_of_operators = {"+": add(operand1, operand2),
                         "-": sub(operand1, operand2),
                         "*": mul(operand1, operand2),
                         "/": div(operand1, operand2)}

    if operator in dict_of_operators.keys():
        return dict_of_operators.get(operator)


print(calculate(10, 2, "/"))
print(calculate(10, 2, "+"))
print(calculate(10, 2, "-"))
print(calculate(10, 2, "*"))
print(calculate(10, 0, "/"))



