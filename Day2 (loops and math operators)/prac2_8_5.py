word = input("Enter a word: ").upper().strip()
vowels = ["A", "E", "I", "O", "U"]
new_word = " "
are_vowels = " "

for letters in word:
    if letters not in vowels:
        new_word += letters
    if letters in vowels:
        are_vowels += letters

print(new_word)
print(are_vowels)
