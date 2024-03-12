import operator
from replit import clear



operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }


def calculator(num1, op, num2):
    operation = operators[op]
    result = operation(num1, num2)
    print(f"{num1} {op} {num2} = {result}")
    decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if decision == 'n':
        clear()
        calculate_new()
    else:
        print("+\n", "-\n", "*\n", "/\n")
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculator(num1=result, op=operation, num2=num2)









def calculate_new():
    first_number = float(input(f"What's the first number?: "))
    print("+\n", "-\n", "*\n", "/\n")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    calculator(num1=first_number, op=operation, num2=second_number)





calculate_new()

