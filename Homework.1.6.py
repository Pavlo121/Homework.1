def create_calculator(operator):
    def calculator(a, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return "Ділення на нуль!"
            return a / b
        else:
            return "Невідомий оператор!"

    return calculator

add = create_calculator('+')
subtract = create_calculator('-')
multiply = create_calculator('*')
divide = create_calculator('/')

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0))
