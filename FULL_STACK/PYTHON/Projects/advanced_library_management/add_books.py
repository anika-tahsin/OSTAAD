
import save_books
import random, datetime

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    while True:
        try: 
            year = int(input("Enter publishing year: "))
            break
        except ValueError:
            print("Please enter a valid Integer")

    while True:
        try: 
            price = int(input("Enter Book Price: "))
            break
        except ValueError:
            print("Please enter a valid Integer")


    while True:
        try: 
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("Please enter a valid Integer")

    isbn = random.randint(10000,99999)
    bookAddedAt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    

    book = {
        "title":title,
        "author":author,
        "isbn":isbn,
        "year":year,
        "price":price,
        "quantity":quantity,
        "bookAddedAt":bookAddedAt,
        "booklastUpdatedAt": "",
        "bookBorrowedAt": "",
        "bookReturnedAt": ""
    }

    all_books.append(book)
    save_books.save_book(all_books)

    print("Book Added Successfully")

    return all_books