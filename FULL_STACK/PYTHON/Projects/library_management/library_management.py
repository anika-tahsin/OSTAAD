import add_books
# import update_books
import delete_books
import view_all_books

all_book = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. Update Books")
    print("3. Delete Books")
    print("4. View All Books")

    menu = input("Select any number: ")

    if menu == "0":
        print("thanks for using lIBRARY MANAGEMENT SYSTEM")
        break
    # Add book
    elif menu == "1":
        all_book = add_books.add_books(all_book)
    # update books
    #elif menu == "2":
        #all_book = update_books.update_books(all_book)
     # delete/remove books
    elif menu == "3":
        all_book = delete_books.delete_book(all_book)
    # View all books
    elif menu == "4":
        view_all_books = view_all_books.view_all_books (all_book)
    else:
        print("Choose a valid number")