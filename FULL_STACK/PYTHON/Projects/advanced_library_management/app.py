import add_books
import update_book
import delete_book
import view_books
import load_books
import borrow_book
import return_book
import view_borrower

all_book = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. Update Books")
    print("3. Delete Books")
    print("4. View All Books")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Borrower Information")

    all_book = load_books.reload_all_books(all_book)

    menu = input("Select any number from the menu: ")

    if menu == "0":
        print("Thanks for using LIBRARY MANAGEMENT SYSTEM")
        break

    # Add book
    elif menu == "1":
        all_book = add_books.add_books(all_book)

    # update books
    elif menu == "2":
        all_book = update_book.update_book(all_book)

    # delete/remove books
    elif menu == "3":
        all_book = delete_book.delete_book(all_book)

    # View all books
    elif menu == "4":
        all_book= view_books.view_all_books(all_book)

    # Borrow Book
    elif menu == "5":
        all_book = borrow_book.borrow_book(all_book)

    # Return Book
    elif menu == "6":
        all_book = return_book.return_a_book(all_book)

    # Borrower Information
    elif menu == "7":
        borrower  = view_borrower.view_borrower()
    else:
        print("Choose a valid number")