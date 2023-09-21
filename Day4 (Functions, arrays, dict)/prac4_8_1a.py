total_reservations = []


def add_reservation(name, guests, table_number):
    reservations = {"name": name, "guests_no": guests, "table_no": table_number}
    total_reservations.append(reservations)


def display_reservations():
    for reservations in total_reservations:
        print(
            f"Reservations: \nName: {reservations['name']} \nNo. of Guests: {reservations['guests_no']} \nTable Number: {reservations['table_no']} \n------------"
        )


while True:
    name = input("Enter guest name: ")
    guests = int(input("Enter number of guests: "))
    table_number = int(input("Enter table number: "))

    add_reservation(name, guests, table_number)
    if input("Do you still want to continue? (y/n): ") == "n":
        break

display_reservations()
