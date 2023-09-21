word = input("Enter a word: ").upper()
vowels = ["A", "E", "I", "O", "U"]
new_word = " "

for letters in word:
    if letters not in vowels:
        new_word += letters

new_word = new_word.strip()
print(new_word)
