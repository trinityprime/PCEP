import random

number = 0
secret_num = random.randint(1, 10)

while number != secret_num:
    print("Haha! You are stuck in my loop!")
    number = int(input("Enter a number: "))
    if number == secret_num:
        print("You are free...?")
        break
