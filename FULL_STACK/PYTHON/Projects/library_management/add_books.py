# title, author(s), ISBN, publishing year, price, quantity

from save_books import save_books

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = int(input("Enter ISBN Number: "))
    year = int(input("Enter publishing year: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity Number: "))

    book = {
        "title":title,
        "author":author,
        "isbn":isbn,
        "year":year,
        "price":price,
        "quantity":quantity
    }

    all_books.append(book)
    save_books(all_books)

    print("Books Added Successfully")

    return all_books