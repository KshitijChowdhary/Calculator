from art import logo

#Calculator

global number1
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operator = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculation(number1):
    operation = input("Pick an operation \n")
    number2 = int(input("What's the second number? \n"))
    result = operator[f"{operation}"](number1, number2)
    print(f"{number1} {operation} {number2} = {result}")
    repeat(result)

def repeat(result):
    choice = input(f"Type \'y\' to continue calculation with {result}, or type \'n\' to start a new calculation: ")
    if choice == "y":
        number1 = result
        calculation(number1)

    else:
        number1 = int(input("What's the first number? \n"))
        calculation(number1)

print(logo)
number1 = int(input("What's the first number? \n"))
calculation(number1)