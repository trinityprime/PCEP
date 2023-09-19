age = int(input("Enter your age: "))

# Check if the player is eligible to play
if age < 18:
    print("Sorry, you are too young to play.")
elif age > 65:
    print("Sorry, you are too old to play.")
else:
    print("You are eligible to play!")
