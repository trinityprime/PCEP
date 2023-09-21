print("Simple Calculator")


def calculation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        return num1 / num2


while True:
    operation = input("Enter the operation (+, -, *, /, enter ` to exit): ")

    if operation == "`":
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(calculation(num1, num2, operation))
