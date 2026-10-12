def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


choice = input("Which operation do you want (+, -, *, /)? ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if choice == "+":
    result = add(num1, num2)

elif choice == "-":
    result = subtract(num1, num2)

elif choice == "*":
    result = multiply(num1, num2)

elif choice == "/":
    result = divide(num1, num2)

else:
    result = "Invalid operation"


print("Result:", result)
             
