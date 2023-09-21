collection = []


def add_books(isbn, title, author):
    books = {"isbn": isbn, "title": title, "author": author}
    collection.append(books)


def search_books(isbn):
    for books in collection:
        if books["isbn"] == isbn:
            print(
                f"ISBN: {books['isbn']} | Title: {books['title']} | Author: {books['author']}"
            )


while True:
    print("==================")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Exit")
    print("==================")
    option = int(input("Enter an option: "))
    if option == 1:
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter author name: ")
        add_books(isbn, title, author)
        print(f"ISBN {isbn} added.")

    elif option == 2:
        find_isbn = input("Enter ISBN: ")
        search_books(find_isbn)

    else:
        break
