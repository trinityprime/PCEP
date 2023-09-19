sentence = input("Input a string: ")

if sentence == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif sentence == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {sentence}!")


income = float(input("Enter the annual income: "))
tax = 0

if income <= 85528:
    tax += income * 0.18 - 556
if income <= 0:
    tax = 0
elif income > 85528:
    surplus = income - 85528
    tax += 14839 + surplus * 0.32

tax = round(tax, 0)
if tax < 0:
    tax = 0
print("The tax is:", tax, "thalers")


year = int(input("Enter a year: "))

if year < 1582:
    result_year = "nil"
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    result_year = "common year"
elif year % 100 != 0:
    result_year = "leap year"
elif year & 400 != 0:
    result_year = "common year"
else:
    result_year = "leap year"

print(result_year)
