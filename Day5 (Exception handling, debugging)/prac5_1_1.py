print("Simple Calculator")

def calculation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "ZeroDivisionError: Cannot divide by 0"

while True:
    operation = input("Enter the operation (+, -, *, /, enter ` to exit): ")

    if operation == "`":
        print("Goodbye!")
        break

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break  
        except ValueError:
            print("Value Error: Please enter a valid number.")

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Value Error: Please enter a valid number.")
        continue  

    print(calculation(num1, num2, operation))