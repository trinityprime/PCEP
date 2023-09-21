total_reservations = []


def add_reservation(name, guests, table_number):
    reservations = {"name": name, "guests_no": guests, "table_no": table_number}
    total_reservations.append(reservations)


def update_reservations(name_update, guests, table_number):
    for reservations in total_reservations:
        if reservations["name"] == name_update:
            reservations["name"] = name
            reservations["guests_no"] = guests
            reservations["table_no"] = table_number
            print(f"Reservation for {name_update} updated.")
        else:
            print(f"{name_update} is not found!")


def display_reservations():
    for reservations in total_reservations:
        print(
            f"Reservations: \nName: {reservations['name']} \nNo. of Guests: {reservations['guests_no']} \nTable Number: {reservations['table_no']} \n------------"
        )


while True:
    print("1. Add reservations")
    print("2. Update reservations")
    print("3. Display reservations")
    print("4. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        name = input("Enter guest name: ")
        guests = int(input("Enter number of guests: "))
        table_number = int(input("Enter table number: "))
        add_reservation(name, guests, table_number)
    elif option == 2:
        update_name = input("Enter guest name to update: ")
        update_guest = int(input("Enter number of guests: "))
        update_table_number = int(input("Enter table number: "))
    elif option == 3:
        display_reservations()
    else:
        print("Goodbye!")
        break
