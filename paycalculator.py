def basic_math_operation(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# Example usage
result_add = basic_math_operation('add', 5, 3)
print("Addition:", result_add)

result_subtract = basic_math_operation('subtract', 10, 4)
print("Subtraction:", result_subtract)

result_multiply = basic_math_operation('multiply', 6, 2)
print("Multiplication:", result_multiply)

result_divide = basic_math_operation('divide', 8, 2)
print("Division:", result_divide)
