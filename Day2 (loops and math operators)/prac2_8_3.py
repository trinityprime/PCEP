secret_word = "chupacabra"
word = " "

while word != secret_word:
    print("Haha! You are stuck in my infinte loop!!")
    word = input("Enter a word: ").lower()
    if word == secret_word:
        print("You have done it?!?")
        break
