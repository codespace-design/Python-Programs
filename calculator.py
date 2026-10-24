def calculate(a, b, operation):
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(calculate(10, 5, "+"))
print(calculate(10, 0, "/"))