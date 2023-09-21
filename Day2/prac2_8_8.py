number = int(input("Enter a natural number except 1: "))
steps = 0

while number != 1:
    print(number, end="\n")
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    steps += 1

print(f"Steps required: {steps}")
