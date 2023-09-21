number_list = []

while True:
    number = int(input("Enter a number (enter 0 to exit): "))
    number_list.append(number)
    for i in range(0, len(number_list)):
        for j in range(i + 1, len(number_list)):
            if number_list[i] >= number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]

    print(number_list)
    if number == 0:
        print("Goodbye!")
        break
