correct_password = "secret_password"
attempts = 3

print("Welcome to the Password Guessing Game!\n")
print(f"You have {attempts} attempts to guess the password.\n")

guess = input("Enter your guess: ")

while (guess != correct_password):
    attempts -= 1
    if (attempts == 0):
        print(f"You have {attempts} attempts left, game over!")
        break
    print(f"Incorrect guess! You have {attempts} attempts left!")
    guess = input("Enter your guess: ")
    if (guess == correct_password):
        print("Correct guess!")
        break
